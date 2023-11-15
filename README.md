# Homework Task

**Check out https://github.com/ubsuny/CompPhys/Calculus and generate a library `calculus.py` with functions / methods needed for Task 1 and 2**.

In particular fullfill three tasks (one for each group member):

**Task 1:**
Use the four integral algorithms (simpson, adaptive trapezoid, trapezoid) to create a Jupyter notebook that imports the functions from `calculus.py` and use them to calculate and plot the integral of:

- $\exp(-1/x)$
- $\cos(1/x)$
- $x^3 + \frac 1{\textrm{GroupNumber}}$

with different boundaries: 

$$
[0,10\cdot\textrm{GroupNumber}],]0,\pi\cdot\textrm{GroupNumber}],[-1,1]
$$

(Pay attention to the boundary brackets ][)

Additionally, compare the accuracies (how many digits are correct) and efficiencies (how many steps does it take to reach a given accuracy).

**Task 2:**
Compare the accuracies (how many digits are correct) and efficiencies (how many steps does it take to reach a given accuracy) for any two root-finding algorithms on the two functions

$$
y(x) = \tan(x) \textrm{ and}
$$

$$
y(x) = \tanh(x).
$$

**Task 3:**
- Compare the numpy integration functions to the ones found in compphys
- Add missing docstrings in `calculus.py`
- Reuse github actions for linting and unit tests for `calculus.py`
- write unit tests for functions in `calculus.py`
  
---

For this you have to complete the following steps:

- Discuss in this repository using issues who will do which task (specified above)
- Discuss who should be the main responsible for the repository (the one that can accept merge requests, let me know in discord so I can adjust rights)
- Work together by generating `calculus.py` with functions for task 1 and 2 from compphys
- Discuss and generate milestone for your project to optimize the timeline of your project
- Discuss and generate labels for your issues
- Fork this repository
- Merge the necessary fies from the original homework project into your fork
- commit
- create merge requests for your work

Also use discord for discussing solutions to any issues popping up.

## Grading

| Homework Points                  |                |              |            |
| -------------------------------- | -------------- | ------------ | ---------- |
|                                  |                |              |            |
| Interaction on own project       |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 6              | 1            | 6          |
| Merge requests                   | 3              | 1            | 3          |
| Merge Accepted                   | 1              | 1            | 1          |
| Branches                         | 2              | 0.5          | 1          |
| Issues                           | 10             | 0.5          | 5          |
| Closed Issues                    | 5              | 0.2          | 1          |
| \# Conversations                 | 30             | 0.2          | 6          |
|                                  |                |              |            |
| Total                            |                |              | 23         |
|                                  |                |              |            |
| Shared project points            |                |              |            |
| \# Label                         | 5              | 0.2          | 1          |
| \# Milestones                    | 2              | 1            | 2          |
| \# Tags                          | 0              | 1            | 0          |
|                                  |                |              |            |
| Total                            | 7              |              | 5          |
|                                  |                |              |            |
|                                  |                |              |            |
| Interaction on others project(s) |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 3              | 1            | 3          |
| Branches                         | 1              | 0.5          | 0.5        |
| Issues                           | 9              | 0.5          | 4.5        |
| \# Conversations                 | 15             | 0.2          | 3          |
|                                  |                |              |            |
| Total                            | 22             |              | 11         |
|                                  |                |              |            |
| Result                           |                |              |            |
| Task completion                  | 5              | 1            | 5          |
|                                  |                |              |            |
| Sum                              |                |              | 42         |
