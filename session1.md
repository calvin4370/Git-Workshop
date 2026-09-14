# Session 1: Local Workflows

## Activity 1: Initialise a git repo on Gitlab and clone it locally
>Setup
>- This session continues straight from Session 0
>- You may reuse the GitLab repo you created in the previous session, or making one again

#### a. Go to GitLab and create a new GitLab repository
- You can name it whatever you want e.g. `Local Git Practice`
- GitLab will give it a machine-readable slug e.g. `Local-Git-Practice`
- You can just create it under your own GitLab account. No need to put it in the SPDM group.
- Now you can tick `Add README` and add a license if you want

#### b. Clone the remote repo locally
- In the repo page, copy the HTTPS address again
- In your terminal, ensure you are in the home directory. If not, navigate there using `cd ~`
- Run `git clone <HTTPS_address>` from the home directory

#### c. You now have a local copy of the remote repo you created on GitLab
- The repo will be initalised locally as a folder in your home directory e.g. named `Local-Git-Practice`
- Navigate into this folder
- Running `ls -a` should show the `.git` hidden folder
- You can also run `git status` to verify the current folder is a git repo


<br>


## Activity 2: Staging and Commiting Changes


<br>


## Activity 3: Writing Multi-line Commits

- Note: We will go through conventions for writing commit messages in Session 6: Team Workflow Standards


<br>


## Activity 4: Other useful commands and arguments for local workflows


<br>


## Activity 5: Using the VSCode IDE for a more user-friendly UI


<br>


## Activity 6: Interaction with Jupyter Notebooks


<br>


## Activity 7: Writing .gitignore


#### What if the file you want to gitignore has already been pushed?