# Session 0: Intro to Git Basics and GitLab Setup

## Activity 1: Analytics.gov Environment Setup

Check if necessary TODO


<br>


## Activity 2: Learning the Terminal

The **terminal** (aka command line or shell) is a text-based interface for interacting with your computer, as opposed to a graphical interface like Windows Explorer where you click on folders to navigate.

A **shell** is the program that reads the commands you type, interprets them, and tells the operating system to execute them. We use the **Bash** shell, which is both a command interpreter and a programming language — meaning you can also write `.sh` scripts to automate sequences of commands.

<hr>

**Reference table:**
<!-- Reference Table -->
<table>
  <colgroup>
    <col style="width: 30%">
    <col style="width: 70%">
  </colgroup>
  <thead>
    <tr>
      <th>Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>pwd</code></td>
      <td>Show the path to your <strong>present</strong> working directory</td>
    </tr>
    <tr>
      <td><code>ls</code></td>
      <td>List files in current directory</td>
    </tr>
    <tr>
      <td><code>ls -a</code></td>
      <td>List all files including hidden ones (e.g. <code>.git</code> folder)</td>
    </tr>
    <tr>
      <td><code>ls -la</code></td>
      <td>List all files with details (permissions, size, date)</td>
    </tr>
    <tr>
      <td><code>cd &lt;folder&gt;</code></td>
      <td>Move into a folder or path</td>
    </tr>
    <tr>
      <td><code>cd ..</code></td>
      <td>Move up (back) one folder</td>
    </tr>
    <tr>
      <td><code>cd ../&lt;folder&gt;</code></td>
      <td>Move up (back) one folder then enter a folder or path there</td>
    </tr>
    <tr>
      <td><code>cd ~</code></td>
      <td>Go back to your home directory (e.g. <code>/home/jovyan</code>)</td>
    </tr>
    <tr>
      <td><code>cd -</code></td>
      <td>Go back to the previous directory you were in (back button)</td>
    </tr>
  </tbody>
</table>


Current working directory (aka present working directory / `pwd`) is the folder your terminal is currently working in. Most terminal commands need to be ran from a specific location to ensure they do what you want.

#### a. Check your present working directory
- Open your terminal
    - If you are using JupyterLab, click the terminal tab to open the terminal
    - Otherwise, if you are on the VSCode server, you can `` Ctrl + ` `` to open the terminal at the bottom of your screen
- Run `pwd` in your terminal
    - You should see something like `/home/jovyan`
- Run `ls` in your terminal
    - You should see a list of all the files and folders in your present working directory

#### b. Navigate to the home directory
- Run `cd ~` to ensure you are in the home directory. Every time you open Analytics@Gov, you will be put in the home directory (`/home/jovyan`)

#### c. Navigate to the folder named `session0`
- From the home directory, run `cd sessions` to navigate into the folder containing all session materials for this workshop
- Run `pwd` to show your new location
- Run `cd session0` to navigate into Session 0's folder
- Run `pwd` again to show your new location

#### d. Navigate to the folder named `session1`
- Try running `cd session1` from your current pwd.
- You will notice that will not work, as there is no folder named "session1" in your current folder (You can verify this by running `ls` to show the files and folders in your current directory)
- You will need to walk back up one folder to find it. Run `cd ..` to do so
- Then run `cd session1` to navigate into the correct folder

#### e. Navigate to the previous folder
- Run `cd -` to navigate to the folder you were previously in.
- This is like the "back button" on your web browser. It does not necessarily always work like `cd ..` as you can input entire paths to `cd` to jump many folders at a time

#### f. Try using longer paths with `cd`
- Navigate to the home directory using `cd ~`
- Run `cd sessions/session1` to navigate straight into session 1's folder
- From there, run `cd ../session1` to navigate out one folder and immediately navigate into session 1's folder

#### g. Other useful commands and keyboard shortcuts in the terminal

| Keyboard Shortcut | Description |
| --- | --- |
| `Tab` | Autocomplete a file or folder name |
| `↑` / `↓` | Scroll through previous commands |
| `Ctrl + C` | Cancel a running command |
| `Ctrl + L` | Clear the screen (scrolls your view down, keeps the lines) |
| `Ctrl + LeftArrow` | Move cursor to the left of the terminal line |
| `Ctrl + RightArrow` | Move cursor to the right of the terminal line |

| Useful Commands | Description |
| --- | --- |
| `clear` | Clear the terminal screen (deletes all lines) |
| `history` | Show your command history |

<hr>

Try running `python scripts/infinite_loop.py` and interrupting it mid run using `Ctrl + C`. Then clear the terminal log with `clear`.

<hr>

<span style="color:salmon">This activity went through the terminal commands you will need to know to work effectively with Git. They are necessary to ensure you are in the correct directory before running git commands.</span>

There are many more terminal commands like `touch` (for creating empty files) and `mkdir` (for creating empty folders) that allow you to do everything a programmer needs to do from the terminal, but since we have a UI in analytics@gov / other IDEs, we do not need to use them.

Refer to [Git Summary Notes](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link), Section 0. Linux and the Terminal for more information.

<br>

## Activity 3: Git Environment Setup

**Configure your Git identity**

Git stamps every commit with a name and email. Without this, your first commit will either fail or be attributed to nobody, so we set it before creating any repos.

#### a. Set your name and email
```
git config --global user.name "short_username"
git config --global user.email "your_email@agency.gov.sg"
```
- You can use any short name for your `user.name`
- You will need to use your NHB email for `user.email` as that is required for Analytics@Gov authentication
- `--global` applies this across every repo on your account, so you only need to do this once

#### b. Set your default terminal text editor
```
git config --global core.editor nano
```

- Git opens this editor when a command needs you to write a message e.g. `git commit`
- Note: nano is already the default terminal text editor (and ONLY available one) on analytics@gov, but on your personal device, you may want to set this to your IDE of choice for a more user-friendly UI/UX (e.g. For VSCode, run `git config --global core.editor code`)

#### c. Verify your config
```
git config --list
```

- Look for `user.name`, `user.email` and `core.editor` in the output

<hr>

**Next, set up your GitLab Personal Access Token (PAT)**

Analytics@Gov requires you to configure your PAT before you can push / pull from Analytics@Gov GitLab

#### d. Go to Analytics@Gov GitLab and log in
- TODO

<hr>

We will test our PATs to ensure they are working in the next activity.

<br>

## Activity 4: Initialising a folder as a local Git repo and linking it to GitLab

This is the first of two ways to initialise a local git repo to start tracking your changes. You can do this if:

- You are about to start a new project from scratch (Note: In this case, it is preferred to use the 2nd method, shown in Activity 5)

- Or if you have an ongoing / completed project in a folder but have not yet tracked it with Git. In this case, start from step `c.`

> **Required**:
> 
> - `minions.csv`
> - `eda.ipynb`

#### a. Navigate to your home directory
```
cd ~
```

#### b. Create a new directory
- You can click the folder icon in the UI to create a folder in the current working directory. Name it anything you want e.g. `session0_repo_1`
- Alternatively, run this terminal command to create a folder in the current working directory
    ```
    mkdir session0_repo_1
    ```
- Navigate into the folder using `cd session0_repo_1`

#### c. Initialise the current folder as a Git repository locally
```
git init
```
- Check that the folder has been properly initialised as a local Git repo by running `ls -a`
    - `ls -a` shows all files including hidden ones
    - We are looking for a hidden folder named `.git` which stores information about your git repo
- Check the names of the branches on your git repo using `git branch`
    - We are expecting to see only 1 branch named `master`, which is the main branch in the repo


#### d. Rename the main branch
- Note: By default `git init` initialises the local repo with its 1st branch named `master`. 
- This is an old convention, and nowadays developers name the main branch "main"
- Run `git branch -m master main` to rename the "master" branch to "main"

#### e. Link the local repo to a remote repo on GitLab
- Go to GitLab and create a new repository.
    - You can create it under your own namespace which places it under your account's ownership (no need to place it in SPDM's group)
    - Make sure to untick `Add README`
- From the repo page, copy the HTTPS address of the remote repo
- Ensure that you are in your new repo's folder in the terminal here, then run `git remote add origin <HTTPS_address>` to link your local repo to the remote repo on GitLab

#### f. Set the default name for the main branch
- While `master` is the default name for the main branch when you run `git init` to initialise a git repo, nowadays the convention is to name the main branch "`main`"
- You can configure git to change the default name to main by running `git config --global init.defaultBranch main`


<br>

## Activity 5: Creating a new remote repo on GitLab and cloning it locally

#### a. Go to GitLab and create a new GitLab repository
- You can name it whatever you want e.g. `Session 0 Repo 2`
- GitLab will give it a machine-readable slug e.g. `Session-0-Repo-2`
- You can just create it under your own GitLab account. No need to put it in the SPDM group.
- Now you can tick `Add README` and add a license if you want

#### b. Clone the remote repo locally
- In the repo page, copy the HTTPS address again
- In your terminal, ensure you are in the home directory. If not, navigate there using `cd ~`
- Run `git clone <HTTPS_address>` from the home directory

#### c. You now have a local copy of the remote repo you created on GitLab
- The repo will be initalised locally as a folder in your home directory e.g. named `Session-0-Repo-2
`
- Navigate into this folder
- Running `ls -a` should show the `.git` hidden folder
- You can also run `git status` to verify the current folder is a git repo

<br>

## End of Session 0
- In the previous activity, we created a brand new remote repo on GitLab, and cloned a local copy so that we can start a new project from scratch
- In the next session, we will clone an ongoing project from GitLab, so that we can learn how to collaborate within a team