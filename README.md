# SoccerNet-Depth


*SoccerNet-Depth* is the largest public dataset to provide depth estimation from team sports videos, with *12.4K* frames. Unlike other MDE sport datasets, SoccerNet-Depth contains scene-centric data from in-match scenarios. 
The dataset contains synthetic video sequences that makes it valuable for temporally consistent depth estimation. The color-depth pairs are collected from two popular video games, *NBA2K22 and EFootball*, through an automated extraction process. 
The synthetic nature and automated extraction process makes the dataset scalable and the methodology transferable to any other sports video game.

This repository contains:

- **SoccerNet-Depth**: A new synthetic dataset for monucular depth estimation in sports videos.
- **Evaluation code**: The evaluation code used to benchmark the dataset using 5 state-of-the-art methods.
- **Automated extraction code**: The code used to extract autonomously the depth data from the games leveraging the NVIDIA Nsight Graphics software as well as [PyAutoGUI](https://github.com/asweigart/pyautogui), [PyDirectInput](https://github.com/learncodebygaming/pydirectinput), and [ImageSearch](https://github.com/drov0/python-imagesearch/blob/master/README.md).

If you are interested for more information, refer to the paper:
[Paper](https://orbi.uliege.be/handle/2268/316221?&locale=en)

<img src="./images/graphical_abstract.jpg" width="700">

## SoccerNet-Depth dataset 
The dataset structure is designed as follows:
```
SoccerNet-Depth/
├── Efootball/
│ ├── Train/
│ | ├── game_1.ext
| | | |── video_1
| | | | |── color
| | | | | |── 1.png
| | | | | |── ...
| | | | | |── n.png
| | | | |── depth 
| | | | | |── 1.png
| | | | | |── ...
| | | | | |── n.png
| | | | |── depth_r 
| | | | | |── 1.png
| | | | | |── ...
| | | | | |── n.png
| | | | |── depth_buffer
| | | | | |── 1.csv
| | | | | |── ...
| | | | | |── n.csv
| | | |── ...
| | | |── video_i
| | | | |── ...
| | |── ...
│ | ├── game_m.ext
| │ | ├── ...
│ ├── Test/
| │ ├── ...
│ └── Validation/
| │ ├── ...
└── Nba2K22/
│ ├── ...
```

As a first step, follow this [link](https://pypi.org/project/SoccerNet/) to obtain the instructions to download the SoccerNet pip package.

A quick summary of those instructions is:
```
conda create -n SoccerNet python pip
conda activate SoccerNet
pip install SoccerNet==0.1.57
```

Once this is done, use the following lines to access our data. Football and basketball data are downloaded separatey.
```
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader=SoccerNetDownloader(LocalDirectory="path/to/SoccerNet")
mySoccerNetDownloader.downloadDataTask(task="depth-basketball", split=["train","valid","test"]) # to access the basketball part of the dataset
mySoccerNetDownloader.downloadDataTask(task="depth-football", split=["train","valid","test"]) # to access the football part of the dataset
```

In total, the dataset encompasses a total of $12{,}398$ frames, split following a $60/20/20$ distribution with each game only appearing in one set. 
For football, there are $7{,}073$ football frames in total, $4{,}071$ for training, $1{,}423$ for testing, and $1{,}579$ for the validation set. 
For basketball, we provide a total of 
$5{,}325$ basketball frames, $3{,}270$ for training, $1{,}064$ for testing, and $991$ for validation.

All RGB images and depth maps are at a resolution of $1080p$. Examples of video sequences that constitute the dataset is given hereafter:

<img src="./images/Data_examples.jpg" width="800">


## Evaluation code
The files associated to this evaluation code can be found [here](./evaluation/). 

To evaluate different state-of-the-art methods, we chose to use 5 different metrics: the absolute relative error (Abs Rel), the squared relative error (Sq Rel), the root-mean-square-error (RMSE), the root-mean-square error on the logarithm (RMSE log) and a scale invariant metric called SILog. The evaluation code computes the average metric between the predictions obtained using a method and the ground truths from our dataset. 

To use our evaluation code, simply run the following command:
```
python evaluation.py  --sport <foot|basket> --path_pred </path/to/predictions>  --gt_path </path/to/gt>
```

All the arguments are mandatory. 
- **--gt_path**: Path to the directory that contains the ground truths depth maps. 
- **--path_pred**: Path to the predictions. Make sure to save your predictions as 16-bits PNG files with pixel depth values between 0 and 65,535.
- **--sport**: either foot or basket

Since the code sorts the predictions and ground truths alphabetically, make sure that the files from a pair gt/prediction are given a name that will ensure a correct ordering.  

## Extraction code
The files associated to this evaluation code can be found [here](./extraction/).

The scripts extract the depth information from the games NBA2K22 and EFootball in an automated fashion. Despite their important similarities a distinct script is provided for each game. This is mainly explained by the fact that the game menus are different and required tailored actions.

To run the code for NBA2K22, enter the following command:
```
python script_2K.py
```
To run the code for Efootball, enter the following command:
```
python script_efootball.py
```

The code included in this repository is the version that we used for our project. As such, it is tailored to our specific setup, which consists of two monitors, one on the left at $1920 \times 1080$ and the other one at $1680 \times 1050$. To facilitate data extraction, we opted to run the game on the left side of the screen, while NVIDIA Nsight was positioned on the right side. Both software applications were run in full-screen mode.

To customize the code to your specific setup, we have included an auxiliary file named check_pos.py. This file contains a function that allows you to determine the pixel location of the elements you wish to automate a particular action with, like a click on a button for example.
To use this function, run the following command:
```
python check_pos.py
```
Then, once it is launched, move your mouse to the object you want to retrieve the pixel location, and press your *Enter* key. This will output a (x,y) value corresponding to the pixel location that you can specify to the method that requires it.

Before launching the script, it is necessary to launch Steam using the connection option of Nvidia Nsight. From there, you can launch the video games you want to extract frames from and Nvidia Nsight will be connected, through Steam, to the game. When launching the game, make sure that you don't put the "Command Prompt" interface at the location of the first automated click (on our case, at the middle right of the right screen) as it would lead to unexpected behaviour.

For Efootball, launch the script when you are on the "Trial Match" menu. For "NBA2k22", the script can be launched as soon as you gain access of the menus.

Also, the code excludes the buffers associated to the color images and the depth maps. These buffers take a significant amount of place that can fill up your hard disk pretty fast and lead to running issues. Therefore, it is beneficial to use a external disk to store the data extracted and remove periodically data saved from your hard disk.

## License
...

## Citation

For further information check out our [paper](https://orbi.uliege.be/handle/2268/316221?&locale=en).

Please cite our work if you use our dataset or code:

```bibtex
@inproceedings{Leduc2024SoccerNetDepth,
        title = {{SoccerNet-Depth}: a Scalable Dataset for Monocular Depth Estimation in Sports Videos},
        author = {Leduc, Arnaud and Cioppa, Anthony and Giancola, Silvio and Ghanem, Bernard and Van Droogenbroeck, Marc},
        booktitle = cvsports,
        month = Jun,
        year = {2024},
        address = city-seattle,
        keywords = {}
}
```