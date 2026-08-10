# Session 1: Intro to Git Basics and GitLab Setup

## Activity 1: Analytics@Gov Environment Setup


## Activity 2: Learning the Terminal

> **Required**:
> 
> - 

Current working directory (aka present working directory / pwd) is the folder your terminal is currently working in. Most terminal commands need to be ran from a specific location to ensure they do what you want.


## Activity 3: Git Environment Setup

**Set up your GitLab Personal Access Token (PAT)**
- Go to 
- 

We will test our PATs to ensure they are working in a later activity.


## Activity 4: Initialising a folder as a local Git repo

This is 1 of the ways to initialise a local git repo to start tracking your changes. You can do this if:

- You are about to start a new project from scratch (Note: In this case, it is preferred to use the 2nd method, shown in Activity 5)

- Or if you have an ongoing / completed project in a folder but have not yet tracked it with Git. In this case, start from step `c.`

> **Required**:
> 
> - `minions.csv`
> - `eda.ipynb`

a. Navigate to your home directory
```
cd ~
```

b. Create a new directory
- You can click the folder icon in the UI to create a folder in the current working directory. Name it anything you want e.g. `session1_repo_1`
- Alternatively, run this terminal command to create a folder in the current working directory
    ```
    mkdir session1_repo_1
    ```

c. Navigate into the folder
```
cd session1_repo_1
```

d. Initialise the current folder as a Git repository locally
```
git init
```

e. Check that the folder has been properly initialised as a local Git repo



## Activity 5: Linking a local Git repo to GitLab



## Activity 6: Creating a new remote repo on GitLab and cloning it locally
a. Go to GitLab and create a new GitLab repository
- You can just create it under your own GitLab account. No need to put it in the SPDM group.


## End of Session 1
- In the previous activity, we created a brand new remote repo on Github, and cloned a local copy so that we can start a new project from scratch
- In the next session, we will clone an ongoing project from GitLab, so that we can learn how to collaborate within a team