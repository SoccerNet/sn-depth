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

## Clarifications on data usage

**1. On the restriction of private datasets and additional annotations**

SoccerNet is designed to be a research-focused benchmark, where the primary goal is to compare algorithms on equal footing. This ensures that the focus remains on algorithmic innovation rather than data collection or annotation effort. Therefore:
* Any data used for training or evaluation must be publicly accessible to everyone to prevent unfair advantages.
* By prohibiting additional manual annotations (even on publicly available data), we aim to avoid creating disparities based on resources (e.g., time, budget, or manpower). This aligns with our commitment to open-source research and reproducibility.

**2. On cleaning or correcting existing data**

We recognize that publicly available datasets, including SoccerNet datasets, might have imperfections in their labels (around 5% usually). Cleaning or correcting these labels is allowed outside of the challenge period to ensure fairness:
* Participants can propose corrections or improvements to older labels before the challenge officially starts. Such changes will be reviewed and potentially integrated into future versions of SoccerNet. Label corrections can be submitted before or after the challenge for inclusion in future SoccerNet releases, ensuring a fair and consistent dataset during the competition.
* During the challenge, participants should not manually alter or annotate existing labels, as this introduces inconsistency and undermines the benchmark's fairness.
* Fully automated methods for label refinement or augmentation, however, are encouraged. These methods should be described in the technical report to ensure transparency and reproducibility.

**3. Defining “private datasets”**

A dataset is considered “private” if it is not publicly accessible to all participants under the same conditions. For example:
* Older SoccerNet data are not private, as they are available to everyone.
* However, manually modifying or adding annotations (e.g., bounding boxes or corrected labels) to older SoccerNet data during the challenge creates a disparity and would be considered "private" unless those modifications are shared with the community in advance.

**4. Creative use of public data**

We fully support leveraging older publicly available SoccerNet data in creative and automated ways, as long as:
* The process does not involve manual annotations.
* The methodology is clearly described and reproducible.
* For instance, if you develop an algorithm that derives additional features or labels (e.g., bounding boxes) from existing data, this aligns with the challenge's goals and is permitted.

**5. Data sharing timeline:**

To ensure fairness, we decided that any new data must be published or shared with all participants through Discord at least one month before the challenge deadline. This aligns with the CVsports workshop timeline and allows all teams to retrain their methods on equal footing.


For questions or concerns, please open an issue in the repository or contact us on [Discord](https://discord.gg/SM8uHj9mkP).
