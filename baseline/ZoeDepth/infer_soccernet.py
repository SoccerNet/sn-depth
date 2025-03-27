import os
from glob import glob
import torch
from tqdm import tqdm
from PIL import Image
from zoedepth.models.builder import build_model
from zoedepth.utils.config import get_config
from zoedepth.utils.misc import save_raw_16bit

if __name__ == "__main__":

    dataset_path = "Test/"
    output_dir = "Predictions/Test/"

    os.makedirs(output_dir, exist_ok=True)
    
    conf = get_config("zoedepth", "infer")
    model_zoe_n = build_model(conf)
    model_zoe_n.load_state_dict(torch.load("ZoeDepthN_football.pt", map_location='cpu')["model"])

    
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    zoe = model_zoe_n.to(DEVICE)

    list_games = glob(os.path.join(dataset_path,"*"))
    for game in tqdm(list_games):
        game_id = game.split("_")[-1]
        print("Processing Game_ID: ", game_id)
        list_images = glob(os.path.join(game,"video_1","color","*.png"))
        for image_path in tqdm(list_images):
            if os.path.basename(image_path)[0] == ".":
                print("Skipping hidden file: ", image_path)
                continue

            image = Image.open(image_path).convert("RGB") 
            depth = zoe.infer_pil(image)
            output_path = os.path.join(output_dir, "foot_game_" + str(game_id) + "_video_1_depth_r_" + str(os.path.basename(image_path)[:-4]) +".png")
            save_raw_16bit(depth, output_path)
