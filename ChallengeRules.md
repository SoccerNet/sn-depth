# Guidelines for the SoccerNet 2025 Challenge on Monocular Depth Estimation 

We are excited to announce the **Monocular Depth Estimation (MDE)** task as part of the SoccerNet challenges! This challenge focuses on estimating depth from **football** video sequences, encouraging participants to develop state-of-the-art methods for depth estimation in team sports.

## Challenge Overview

The **objective** of this task is to assign a depth value to each pixel in every frame of a football video sequence. The generated depth maps will be evaluated by comparing them to ground truth data sourced from video games. For this challenge, a new dataset will be constructed in a similar way to the existing dataset.

To learn more, visit: [SoccerNet Challenges](https://www.soccer-net.org/tasks)  
[Monocular Depth Estimation Task](https://www.soccer-net.org/tasks/monocular-depth-estimation)

## Dataset Details

The Monocular Depth Estimation dataset includes **7,073 frames** from football videos, split into training, testing, and validation sets in a 60/20/20 distribution. Each game appears in only one set to ensure separation.

- **Football Frames**: 7,073 frames  
  - Training: 4,071 frames  
  - Testing: 1,423 frames  
  - Validation: 1,579 frames  

## Evaluation Metrics

To assess the effectiveness of depth estimation methods, we use the following five metrics, averaged across the dataset predictions and ground truths:

1. **Absolute Relative Error (Abs Rel)**
2. **Squared Relative Error (Sq Rel)**
3. **Root-Mean-Square Error (RMSE)**
4. **Root-Mean-Square Error on Logarithm (RMSE log)**
5. **Scale Invariant Log Error (SILog)**

The evaluation code calculates these metrics to compare depth estimations from the proposed methods against the ground truth data.

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

- **TBD:** Open evaluation server on the test set.
- **TBD:** Open evaluation server on the challenge set.
- **TBD:** Close evaluation server.
- **TBD:** Report submission deadline.
- **TBD:** CVSports Workshop at CVPR 2025 (awards ceremony).

For questions or concerns, please open an issue in the repository or contact us on [Discord](https://discord.gg/SM8uHj9mkP).

## Challenge
This work contributes to the SoccerNet project. We are pleased to announce that, this year again, the SoccerNet challenges will be organized and, this time, Monocular Depth Estimation will be one of the 4 tasks proposed !

The objective of the task will be to assign, to each pixel of each frame of a team sports video sequence, a depth value. The different depth maps reconstructed will then be compared to the ground truth obtained from two video games. 
A new challenge set of data will be extracted in the same way as the already provided data for this challenge. To evaluate the different methods, we will use the 5 same metrics mentioned above. 

We hope to see new methods built to enhance the baseline and bring the field even further ! Be creative, and enjoy the journey!

To have more information: [SoccerNet challenges](https://www.soccer-net.org/tasks)
[Depth Challenge](https://www.soccer-net.org/tasks/monocular-depth-estimation) 
![image](https://github.com/user-attachments/assets/ea0eb063-d122-4288-b17b-c1a0db1ff42b)
