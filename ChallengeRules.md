# Guidelines for the SoccerNet 2025 Challenge on Monocular Depth Estimation 

We are excited to announce the **Monocular Depth Estimation (MDE)** task as part of the SoccerNet challenges! This challenge focuses on estimating depth from **football** video sequences, encouraging participants to develop state-of-the-art methods for depth estimation in team sports.

## Challenge Overview

The **objective** of this task is to assign a depth value to each pixel in every frame of a football video sequence. The generated depth maps will be evaluated by comparing them to ground truth data sourced from video games. For this challenge, a new dataset will be constructed in a similar way to the existing dataset.

To learn more, visit: [SoccerNet Challenges](https://www.soccer-net.org/tasks)  
[Monocular Depth Estimation Task](https://www.soccer-net.org/tasks/monocular-depth-estimation)

## Dataset Details

The Monocular Depth Estimation dataset includes **7,073 frames** from football videos, split into training, testing, and validation sets in a 60/20/20 distribution. Each game appears in only one set to ensure separation.

- Training: 4,071 frames  
- Validation: 1,579 frames  
- Testing: 1,423 frames
- Challenge: TBD

## Evaluation Metrics

To assess the effectiveness of depth estimation methods, we use the following five metrics, averaged across the dataset predictions and ground truths:

1. **Absolute Relative Error (Abs Rel)**
2. **Squared Relative Error (Sq Rel)**
3. **Root-Mean-Square Error (RMSE)**
4. **Root-Mean-Square Error on Logarithm (RMSE log)**
5. **Scale Invariant Log Error (SILog)**

The evaluation code calculates these metrics to compare depth estimations from the proposed methods against the ground truth data.

It is necessary to respect the following format for naming the different predictions: if it is the prediction for the x th frames of video y from football game z, it should be named *foot_game_z_video_y_depth_r_x.png*. 

Furthermore, the depth maps need to be saved as 16-bit PNG files. Before being saved, the depth maps are normalized within the range of 0 to 1 and then multiplied
by 65,535. 

Finally, depth maps must be such that the smaller values for the pixels corresponds to the closest point to the camera and inversely.


## Participation Rules

- Open to anyone except the organizers.
- We recommend forming teams, but individual participation is also welcome.
- Each participant/team can only submit to one account per task.
- Only the video stream (visual and/or audio) may be used as input for this task.
- Participants can use custom models trained on publicly available datasets, with clear citation of any external datasets used.

## Submission and Winning Criteria

- The winner is the team with the highest performance on the **challenge** dataset, based on the above metrics.
- Submission deadlines and additional details will be announced soon.
- To be eligible for prizes, teams must submit a short report (CVPR format, max 2 pages) detailing their methodology.

## Important Dates

*Note: Dates are tentative and subject to change.*

- **November 20:** Open evaluation server on the test set.
- **November 20:** Open evaluation server on the challenge set.
- **April 24:** Close evaluation server.
- **May 1:** Report submission deadline.
- **TBD:** CVSports Workshop at CVPR 2025 (awards ceremony).

For questions or concerns, please open an issue in the repository or contact us on [Discord](https://discord.gg/SM8uHj9mkP).
