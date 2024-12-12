import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset


class ImageDataset(Dataset):
    def __init__(self, image_files):
        self.image_files = image_files
        self.transform = transforms.ToTensor()

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img = Image.open(self.image_files[idx])
        img_mode = img.mode
        if img.mode != 'I':
            # raise ValueError(f"Image {self.image_files[idx]} is not a 16-bit PNG image")
            img = img.convert('I')
        img_data = np.array(img)
        tensor = torch.from_numpy(img_data).float()
        return tensor
        #return self.transform(img)

"""
Licence MIT

Copyright (c) 2022 Intelligent Systems Lab Org

The following classes and methods have been adapted from ZoeDepth to our application. It has originally been written by author Shariq Farooq Bhat.

The original code: https://github.com/isl-org/ZoeDepth/tree/main
"""
class RunningAverage:
    def __init__(self):
        self.avg = 0
        self.count = 0

    def append(self, value):
        self.avg = (value + self.count * self.avg) / (self.count + 1)
        self.count += 1

    def get_value(self):
        return self.avg


class RunningAverageDict:
    """A dictionary of running averages."""
    def __init__(self):
        self._dict = None

    def update(self, new_dict):
        if new_dict is None:
            return

        if self._dict is None:
            self._dict = dict()
            for key, value in new_dict.items():
                self._dict[key] = RunningAverage()

        for key, value in new_dict.items():
            self._dict[key].append(value)

    def get_value(self):
        if self._dict is None:
            return None
        return {key: value.get_value() for key, value in self._dict.items()}



def compute_scale_and_shift(prediction, target, mask):
    """
    Compute scale and shift to align the 'prediction' to the 'target' using the 'mask'.

    This function solves the system Ax = b to find the scale (x_0) and shift (x_1) that aligns the prediction to the target. 
    The system matrix A and the right hand side b are computed from the prediction, target, and mask.

    Args:
        prediction (torch.Tensor): Predicted values.
        target (torch.Tensor): Ground truth values.
        mask (torch.Tensor): Mask that indicates the zones to evaluate. 

    Returns:
        tuple: Tuple containing the following:
            x_0 (torch.Tensor): Scale factor to align the prediction to the target.
            x_1 (torch.Tensor): Shift to align the prediction to the target.
    """
    # system matrix: A = [[a_00, a_01], [a_10, a_11]]
    a_00 = torch.sum(mask * prediction * prediction, (0, 1))
    a_01 = torch.sum(mask * prediction, (0, 1))
    a_11 = torch.sum(mask, (0, 1))

    # right hand side: b = [b_0, b_1]
    b_0 = torch.sum(mask * prediction * target, (0, 1))
    b_1 = torch.sum(mask * target, (0, 1))

    # solution: x = A^-1 . b = [[a_11, -a_01], [-a_10, a_00]] / (a_00 * a_11 - a_01 * a_10) . b
    x_0 = torch.zeros_like(b_0)
    x_1 = torch.zeros_like(b_1)

    det = a_00 * a_11 - a_01 * a_01
    # A needs to be a positive definite matrix.
    valid = det > 0
    
    x_0[valid] = (a_11[valid] * b_0[valid] - a_01[valid] * b_1[valid]) / det[valid]
    x_1[valid] = (-a_01[valid] * b_0[valid] + a_00[valid] * b_1[valid]) / det[valid]

    return x_0, x_1

def compute_errors(gt, pred):
    """
    Compute the 5 error metrics between the ground truth and the prediction:
    - Absolute relative error (abs_rel)
    - Squared relative error (sq_rel)
    - Root mean squared error (rmse)
    - Root mean squared error on the log scale (rmse_log)
    - Scale invariant log error (silog)

    Args:
        gt (numpy.ndarray): Ground truth values.
        pred (numpy.ndarray): Predicted values.

    Returns:
        dict: Dictionary containing the following metrics:
            'abs_rel': Absolute relative error
            'sq_rel': Squared relative error
            'rmse': Root mean squared error
            'rmse_log': Root mean squared error on the log scale
            'silog': Scale invariant log error
    """


    abs_rel = np.mean(np.abs(gt - pred) / gt)
    sq_rel = np.mean(((gt - pred) ** 2) / gt)

    rmse = (gt - pred) ** 2
    rmse = np.sqrt(rmse.mean())
    rmse_log = (np.log(gt) - np.log(pred)) ** 2
    rmse_log = np.sqrt(rmse_log.mean())

    err = np.log(pred) - np.log(gt)
    silog = np.sqrt(np.mean(err ** 2) - np.mean(err) ** 2) * 100

    return dict(abs_rel=abs_rel, rmse=rmse, rmse_log=rmse_log,
                silog=silog, sq_rel=sq_rel)

def compute_metrics(gt, pred, mask_score, sport):
    """
    This code creates a mask of the same size as the ground truth and prediction, 
    and then modifies the mask based on the sport and the values in the ground truth and prediction. 
    The mask is used to exclude certain areas from the evaluation analysis.

    Args:
        pred (torch.Tensor): Predicted values.
        gt (torch.Tensor): Ground truth values.
        sport (str): The sport to evaluate the predictions on. Can be "basket" or "foot".
        mask_score (bool): Whether to mask the score area in football images.

    Returns:
        dict: Dictionary containing the error metrics computed by the 'compute_errors' function, 
        applied to the areas of the ground truth and prediction indicated by the mask.
    """
    mask = np.ones((1080, 1920), dtype=np.bool_)

    if sport == "basket":
        print("here")
        mask[870:1016, 1570:1829] = False
    if sport == "foot" and mask_score:
        print("in the problem")
        mask[70:122, 95:612] = False


    pred = pred.squeeze().cpu().numpy()
    mask[pred <= 0] = False
    mask[np.isinf(pred)] = False
    mask[np.isnan(pred)] = False

    gt = gt.squeeze().cpu().numpy()
    mask[gt <= 0] = False
    mask[np.isinf(gt)] = False
    mask[np.isnan(gt)] = False


    return compute_errors(gt[mask], pred[mask])
