# Session 1: Local Workflows

In Session 0, you set up Git and your GitLab PAT. In this session, we will learn the **local workflow**: the everyday cycle of making changes, checking them, staging them and committing them to your local repo, then pushing them up to GitLab.

Everything in this session happens in **your own** repo, so you can't break anything for anyone else. We will start working on a shared team repo in Session 2.

> **Required**:
> - Session 0 completed (Git identity configured, GitLab PAT set up)
> - Your GitLab PAT on hand (you may be asked for it the first time you clone / push)
> - The workshop materials' `data/` folder (`analysis.ipynb`, `functions.py`, `minions.xlsx`)

### Reference Table
<!-- Reference Table -->
<table>
  <colgroup>
    <col style="width: 40%">
    <col style="width: 60%">
  </colgroup>
  <thead>
    <tr>
      <th>Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>git clone &lt;HTTPS_address&gt;</code></td>
      <td>Copy a remote repo from GitLab onto your machine as a new folder in your present working directory</td>
    </tr>
    <tr>
      <td><code>git remote -v</code></td>
      <td>Check which remote repo your local repo is linked to</td>
    </tr>
    <tr>
      <td><code>git status</code></td>
      <td>See what has changed, what is staged, and what is untracked. Also tells you if the current folder is a git repo</td>
    </tr>
    <tr>
      <td><code>git status --ignored</code></td>
      <td>Also list files that are being ignored by <code>.gitignore</code></td>
    </tr>
    <tr>
      <td><code>git status -u</code></td>
      <td>List every untracked file individually, instead of collapsing untracked folders into one line (short for <code>--untracked-files=all</code>)</td>
    </tr>
    <tr>
      <td><code>git diff</code><br><code>git diff &lt;file&gt;</code></td>
      <td>Show your <strong>unstaged</strong> changes line by line<br>Same, for a specific file</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git add file1 file2 file_n</code><br><code>git add .</code></td>
      <td>Stage a specific file<br>Stage a variable number of files at once<br>Stage everything in the present working directory</td>
    </tr>
    <tr>
      <td><code>git restore --staged &lt;file&gt;</code><br><code>git restore --staged .</code></td>
      <td>Unstage a specific file (your changes to the file are kept)<br>Unstage everything</td>
    </tr>
    <tr>
      <td><code>git commit -m "commit message"</code></td>
      <td>Commit staged changes with a single-line message</td>
    </tr>
    <tr>
      <td><code>git commit</code></td>
      <td>Opens a nano window for you to write multi-line commit messages</td>
    </tr>
    <tr>
      <td><code>git commit --amend -m "corrected message"</code></td>
      <td>Rewrite the message of the last commit (only if not yet pushed)</td>
    </tr>
    <tr>
      <td><code>git commit --amend --no-edit</code></td>
      <td>Add your currently staged changes into the last commit, keeping its message (only if not yet pushed)</td>
    </tr>
    <tr>
      <td><code>git push</code></td>
      <td>Upload your local commits to the remote repo on GitLab</td>
    </tr>
    <tr>
      <td><code>git log</code><br><code>git log --oneline</code><br><code>git log -n &lt;number&gt;</code></td>
      <td>View commit history<br>View commit history (condense each into one line)<br>Only show the latest <code>&lt;number&gt;</code> commits</td>
    </tr>
    <tr>
      <td><code>git rm --cached &lt;file&gt;</code><br><code>git rm -r --cached &lt;folder&gt;</code></td>
      <td>Stop tracking a file that was already committed, without deleting it from your machine<br>Same, for a whole folder</td>
    </tr>
    <tr>
      <td><code>git check-ignore -v &lt;file&gt;</code></td>
      <td>Show which line of which <code>.gitignore</code> is causing a file to be ignored</td>
    </tr>
  </tbody>
</table>

> **Tip:** `git log` and `git diff` open their output in a scrollable viewer when it does not fit on your screen. Use `↑` / `↓` to scroll and press **`q`** to quit and get back to your terminal.


<br>


## Activity 1: Initialise a git repo on GitLab and clone it locally
>**Terms**
>- Remote repo: The version of your repository hosted on GitLab / GitHub. This is the central copy that your whole team pushes to and pulls from.
>- Local repo: The version of your repository on your own machine. This is where you make changes before pushing them up to the remote.

#### a. Go to GitLab and create a new GitLab repository
- You can name it whatever you want e.g. `Local Git Practice`
- GitLab will give it a machine-readable slug e.g. `Local-Git-Practice`
- You can just create it under your own GitLab account. No need to put it in the SPDM group.
- Tick `Add README`

#### b. Clone the remote repo locally
- In the repo page, click `Code` and copy the address under `Clone with HTTPS`
- In your terminal, ensure you are in the home directory. If not, navigate there using `cd ~`
- Run `git clone <HTTPS_address>` from the home directory
- If you are asked for a username and password, enter your GitLab username, and paste your **PAT** as the password
    - Note: the terminal does not show anything as you paste or type your password. This is normal, just press `Enter`

#### c. You now have a local copy of the remote repo you created on GitLab
- The repo will be initialised locally as a folder in your home directory e.g. named `Local-Git-Practice`
- Navigate into this folder using `cd Local-Git-Practice`
- Running `ls -a` should show the `.git` hidden folder
- You can also run `git status` to verify the current folder is a git repo
    - If you run `git status` outside a git repo, you get `fatal: not a git repository`

#### d. Check your remote is configured correctly
```
git remote -v
```
- The two lines of output should match the URL of the repo on GitLab
- `origin` is the alias Git gave the remote repo when you cloned it, so you don't have to type out the whole URL in future

#### e. Look at your commit history
```
git log
git log --oneline
```

- `git log` shows the full details of each commit: hash, author, date and message
- `git log --oneline` condenses each commit into one line: a short hash and the message
- Right now, you should only see 1 commit (`Initial commit`), which GitLab made when it created your `README.md`
- Cloning gives you the **entire history** of the project, not just the latest files. Every commit is stored in the `.git` folder on your machine


<br>


## Activity 2: Staging, Committing and Pushing Changes
>**Background info:**
>
>- **Untracked** files are files that Git has never tracked, such as a new file or new pipeline outputs.
>    - Git doesn't track their changes, and `git restore` ignores them.
>    - Once you stage a new file (`git add`), it becomes **tracked** by Git
>- **Unstaged** changes are edits to tracked files that you have not staged yet. They exist only in your working directory.
>- **Staged** changes are changes you have added to the *staging area* with `git add`, but not committed yet. The staging area holds everything that will go into your next commit
>- **Committed** changes are saved permanently in your local repo's history as a snapshot.
>- **Pushed** changes are commits uploaded to a remote repo such as one hosted on GitLab, where other people can pull them.

![The 4 areas of Git](../../assets/git-4-areas.png)

#### a. Edit the README
- Delete all the default text in `README.md`
- You may add whatever text you want to it, e.g. `This is a README`. Save the file
- If you are using VSCode, observe that in the left sidebar, your file explorer highlights `README.md` in yellow with an `M` (a tracked file that has been **m**odified)

<hr>

- Run `git status`
  - You should see:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
    	modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    ```
  - This is an <u>unstaged change</u> <span style="color:skyblue">(the change is only in your working directory)</span>

#### b. Stage your change
- Run `git add README.md` to stage your change
- Then, run `git status`
  - You should see:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
    	modified:   README.md
    ```
  - This is now a <u>staged change</u> <span style="color:skyblue">(the change is now in the staging area, waiting to be committed)</span>

#### c. Commit your change
- Run `git commit -m "docs: update README"` to commit your staged change
    - We will go through what `docs:` means in Session 6: Team Workflow Standards
- Then, run `git status`
  - You should see:
    ```
    On branch main
    Your branch is ahead of 'origin/main' by 1 commit.
      (use "git push" to publish your local commits)

    nothing to commit, working tree clean
    ```
  - This is now a <u>committed change</u> <span style="color:skyblue">(the change is now saved to your local git repo)</span>
  - `ahead of 'origin/main' by 1 commit` means your local repo has 1 commit that GitLab does not have yet
  - `working tree clean` means your files match the latest commit exactly, so there is nothing left to stage or commit
- Run `git log --oneline` to see your commit at the top of the history
- Go on GitLab and find your repo.
  - Look at the code.
  - You will not see the changes you made above, as GitLab hosts the remote Git repo, while your changes are still only on your local Git repo

#### d. Push your change
- Run `git push` to push all committed changes to remote
    - If you are asked for a username and password, enter your GitLab username and your PAT, like in Activity 1
- Then, run `git status`
  - You should see:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```
  - The change has now been <u>pushed</u> <span style="color:skyblue">(to the remote git repo hosted on GitLab)</span>
- Now look at your GitLab repo (refresh the page)
  - The updated README should now be visible on GitLab

<hr>

<span style="color:salmon">Get into the habit of running `git status` before and after every Git command. It tells you which area each change is in, and its hints (e.g. `use "git add <file>..."`) often tell you exactly what to run next.</span>


<br>


## Activity 3: Staging and Committing Multiple Files at a Time
>In a real project, you will usually change or create many files between commits. In this activity, we will add the `Minions Visitorship` analysis into your repo.
>
>`Minions Visitorship` simulates an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

#### a. Copy the analysis files into your repo
- From the workshop materials' `data/` folder, copy these 3 files into your `Local-Git-Practice` folder:
    - `analysis.ipynb`: the analysis notebook
    - `functions.py`: helper functions the notebook imports
    - `minions.xlsx`: the minion visitorship dataset
- You can copy them using the UI, or from the terminal, e.g.
    ```
    cp ~/Git-Workshop/data/analysis.ipynb ~/Git-Workshop/data/functions.py ~/Git-Workshop/data/minions.xlsx ~/Local-Git-Practice/
    ```
- ⚠️ Don't open or run the notebook yet, we will do that in Activity 7

#### b. Check the status
- Run `git status`
  - You should see:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    	analysis.ipynb
    	functions.py
    	minions.xlsx

    nothing added to commit but untracked files present (use "git add" to track)
    ```
  - These are <u>untracked files</u> <span style="color:skyblue">(Git has never seen these files before)</span>

#### c. Stage multiple specific files at once
- The notebook and its helper functions belong together, so let's commit them together first
    ```
    git add analysis.ipynb functions.py
    git status
    ```
  - `analysis.ipynb` and `functions.py` are listed under `Changes to be committed` as `new file`
  - `minions.xlsx` is still under `Untracked files`, as we did not stage it
- Commit them:
    ```
    git commit -m "feat: add minions visitorship analysis notebook and functions"
    ```

#### d. Stage everything with `git add .`
- Run:
    ```
    git add .
    git status
    ```
  - `.` means "everything in the present working directory (and its subfolders)", so `minions.xlsx` is now staged
- Commit it:
    ```
    git commit -m "data: add minions visitorship dataset"
    ```
- Run `git log --oneline`. You should now see 4 commits
- Run `git push`, and check that all 3 files are now on GitLab

<hr>

⚠️ `git add .` stages **everything** that changed, which makes it very easy to accidentally commit files you didn't mean to, e.g. data files, outputs or credentials. **Always run `git status` before `git add .`**

In fact, we just committed and pushed a data file, which you usually shouldn't do in a real project. We will learn how to prevent this with `.gitignore`, and how to fix it after the fact, in Activity 8.


<br>


## Activity 4: Other useful commands and arguments for local workflows
#### a. Unstaging files
- Open `README.md` and add a short description of the project, e.g.
    ```
    # Minions Visitorship
    Analysis of museum visitorship by minions.
    ```
- Create a new file in the repo named `notes.md` and type anything in it. Save both files
- Run `git add .` then `git status`
  - Both files are staged. But say you only wanted to commit the README change
- Unstage `notes.md`:
    ```
    git restore --staged notes.md
    git status
    ```
  - `notes.md` is back under `Untracked files`, and `README.md` is still staged
  - Unstaging does **not** delete or undo your edits. Open `notes.md`, your text is still there
- Try unstaging `README.md` too, then run `git status`
  - `README.md` is now back under `Changes not staged for commit`, since it was already a tracked file
- Stage `README.md` again with `git add README.md`

#### b. Rewriting commit messages
- Commit your README change with a deliberate typo:
    ```
    git commit -m "docs: add projcet descritpion to READNE"
    ```
- Oops. **Before pushing**, rewrite the message of the last commit:
    ```
    git commit --amend -m "docs: add project description to README"
    ```
- Run `git log --oneline`
  - The commit with the typo is gone, and replaced by one with the corrected message
  - Notice the corrected commit has a **different hash**. `--amend` does not edit a commit, it **replaces** it with a new one
- Tip: run `git commit --amend` without `-m` to edit the last commit message in nano instead

#### c. Adding forgotten changes to your last commit
- Open `README.md` again. Say you forgot to add a line to your description. Add another line, e.g. `Data: minions.xlsx`. Save the file
- Instead of making a separate commit for this, add it into your last commit:
    ```
    git add README.md
    git commit --amend --no-edit
    ```
  - `--no-edit` keeps the existing commit message
- Run `git log --oneline -n 3` and `git status`
  - There is still only one README commit, and it now includes your extra line
  - `git log -n 3` only shows the 3 most recent commits. You can combine flags like this

#### d. Commit the other file, then push
- `notes.md` is unrelated to the README, so it gets its own commit:
    ```
    git add notes.md
    git commit -m "docs: add notes"
    git push
    ```

<hr>

⚠️ **Only amend commits that you have NOT pushed yet.** Since `--amend` replaces the commit with a new one, amending a pushed commit rewrites history that your teammates may already have pulled. That causes a Git mess for everyone. If there is a minor typo in a commit message you have already pushed, just leave it.


<br>


## Activity 5: Writing Multi-line Commits
>- Note: We will go through conventions for writing commit messages in depth in Session 6: Team Workflow Standards

`git commit -m` is fine for short messages. When you want to explain **why** you made a change, use `git commit` without `-m` to write a longer message in the nano text editor.

#### a. Make a change to commit
- Open `README.md` and add a section on how to run the analysis, e.g.
    ```
    ## How to run
    Open `analysis.ipynb` and run all cells.
    ```
- Save the file, then stage it with `git add README.md`

#### b. Write a multi-line commit message
- Run `git commit` just like that to open a nano window for writing the commit message

    ![nano window opened by git commit](../../notion-notes/image%203.png)

- Write your multi-line message in the space provided, above the lines starting with `#`. For example:
    ```
    docs: add instructions to run the analysis

    Added a "How to run" section to the README so new team
    members know where to start.
    ```
    - The first line is the **summary**. Leave an empty line between the summary and the **body**
    - Lines starting with `#` are ignored, so you don't need to delete them
    - If you leave the message empty, the commit is cancelled

    ![multi-line commit message written in nano](../../notion-notes/image%204.png)

#### c. Save and exit nano
1. Press `Ctrl + X` to exit the nano window
2. nano asks `Save modified buffer?`. Press `Y`
3. nano shows the file name it will save to. Press `Enter` to confirm

- Once you exit, Git automatically creates the commit
- Run `git log -n 1` (not `--oneline`) to see your full multi-line message
- Run `git push`, then go to your repo's commit history on GitLab (`Code` → `Commits`) and click on your latest commit to see the full message there too


<br>


## Activity 6: Using the VSCode IDE for a more user-friendly UI
>Everything we have done in the terminal so far can also be done by clicking buttons in VSCode's **Source Control** panel. Both do the exact same thing, so you can mix and match.
>
>Note: This activity requires the VSCode (code-server) environment on Analytics@Gov.

#### a. Make some changes
- Edit `README.md` and `notes.md`, adding any text to both. Save both files
- Open the Source Control panel by clicking the branch icon in the left sidebar (or `Ctrl + Shift + G`)
- Under `Changes`, you should see both files marked with `M` (modified)
    - New untracked files would be marked with `U`

### Staging and Unstaging Changes
#### b. See your changes
- Click `README.md` in the Source Control panel
- This opens a side-by-side view of the last committed version (left) and your current version (right), with your changes highlighted
    - This is the same information as `git diff README.md`, but easier to read

#### c. Stage a file
- Hover over `README.md` and click the `+` icon
- `README.md` moves under `Staged Changes`
- Run `git status` in the terminal. It shows the exact same thing: `README.md` is staged and `notes.md` is not

#### d. Unstage a file
- Hover over `README.md` under `Staged Changes` and click the `−` icon
- It moves back under `Changes`. This is the same as `git restore --staged README.md`
- Stage `README.md` again with `+`

### Committing Changes
#### e. Commit using the UI
- Type a commit message in the message box at the top of the Source Control panel, e.g. `docs: update README`
- Click `Commit` (or `Ctrl + Enter`)
- Only `README.md` was committed. `notes.md` is still under `Changes`
- ⚠️ If you click `Commit` when **nothing** is staged, VSCode asks whether you want to stage all your changes and commit them directly. This is the same as `git add .` + `git commit`, so be careful when you click `Yes`

#### f. Push using the UI
- Stage and commit `notes.md` using the UI
- Click the `...` menu at the top of the Source Control panel → `Push`
    - You may also see a `Sync Changes` button. This does a `git pull` **and** a `git push`, which we will cover in Session 2
- Run `git log --oneline` in the terminal to confirm both commits are there

<hr>

<span style="color:salmon">The UI is especially useful for reviewing your changes before staging them. But the terminal commands are what you will see in most guides and troubleshooting answers online, so it is important to know both.</span>


<br>


## Activity 7: Interaction with Jupyter Notebooks
>So far, we have worked with `.md` files, which are plain text. When you change one line, Git shows exactly one line changed.
>
>Jupyter notebooks (`.ipynb`) look like cells in the UI, but underneath, they are one large **JSON** file that stores your code **and** cell outputs (including charts), execution counts and metadata. Let's see what that means for Git.

#### a. Look at what a notebook really is
- Open `analysis.ipynb` as plain text instead of in the notebook UI
    - JupyterLab: right-click the file → `Open With` → `Editor`
    - VSCode: right-click the file → `Open With...` → `Text Editor`
- Notice the notebook is stored as JSON, with `"cell_type"`, `"source"`, `"outputs"`, `"execution_count"` and `"metadata"` fields
- Close it without saving

#### b. Run the notebook without changing any code
- Open `analysis.ipynb` normally and run all cells. Save the notebook
- Run `git status`
    - Even though you did not change a single line of code, Git reports `analysis.ipynb` as **modified**
    - You may also see new untracked folders like `__pycache__/` and `.ipynb_checkpoints/`. Ignore them for now, we will deal with them in Activity 8
- Run `git diff analysis.ipynb` and scroll through it (press `q` to exit)
    - The changes are execution counts, metadata, and the charts, which are saved as very long blocks of encoded image data

#### c. Now make a one-line code change
- In the `Config` cell, change `YEAR = 2024` to `YEAR = None` (this plots all years instead of only 2024)
- Run all cells again and save
- Run `git diff analysis.ipynb` again
    - Try to find your one-line change. It is buried among all the output changes

#### d. Clear outputs, then commit
- Clear all outputs, then save the notebook
    - JupyterLab: `Edit` → `Clear Outputs of All Cells`
    - VSCode: click `Clear All Outputs` in the notebook toolbar
- Run `git diff analysis.ipynb` again
    - The diff is much smaller, and your actual code change is easy to find
- Stage and commit **only the notebook**, then push:
    ```
    git add analysis.ipynb
    git commit -m "analysis: plot all years instead of 2024 only"
    git push
    ```

<hr>

**Tips for working with notebooks in Git:**
- Simply opening and running a notebook creates changes, even if you changed no code. Always check `git status` before running `git add .`
- Clearing outputs before committing keeps diffs small and readable, and keeps large images out of your commit history. Whether to commit outputs is a team decision, which we will discuss in Session 6
- Keep reusable logic in `.py` files (like `functions.py`) and import them into your notebooks. `.py` files are much easier to review and track with Git
- Notebook changes also cause **merge conflicts** very easily when working in a team. We will see this in Session 2


<br>


## Activity 8: Writing .gitignore
We can tell Git which files and folders to ignore in a repo using a `.gitignore` file. This is useful for files you know you NEVER want to commit, including:

- Secrets, API keys, credentials (e.g. `.env`). We will cover these in Session 2
- Log files (`*.log`)
- Auto-generated folders, e.g. `__pycache__/` for Python, `.ipynb_checkpoints/` for Jupyter, `.venv/` for virtual environments
- Operating system files (`.DS_Store` on Mac)
- For data teams, **data files**, which may be large or contain sensitive information that should not be stored on GitLab

**Syntax**

```bash
# This is a comment

# Ignore a specific file
test.py

# Ignore all files of a specific file type (.csv)
*.csv

# Ignore a whole folder
data/

# Ignore a folder's contents but not the folder itself
data/*

# Ignore everything in a folder except one file
# (order of entries DOES matter, put your exceptions after the wide ignore)
data/*
!data/keep_this.csv

# Ignore a file only in the root directory
/config.json

# Ignore a file in any subdirectory
**/config.json
```

#### a. Create an output file
- Our analysis usually exports results to a folder named `{YEAR} output`. Simulate this by running:
    ```
    mkdir "2024 output"
    touch "2024 output/summary.xlsx"
    ```
- Run `git status`. You should see these untracked folders:
    - `2024 output/`
    - `__pycache__/` (created by Python when the notebook imported `functions.py`)
    - `.ipynb_checkpoints/` (created by JupyterLab when you opened the notebook. You may not see this if you used VSCode)

#### b. Create a `.gitignore` file
- In the **root folder** of your repo, create a new file named exactly `.gitignore` (note the leading dot, and no file extension)
    - Or, from the terminal: `touch .gitignore`
- Files starting with `.` are hidden. Use `ls -a` to see it in the terminal
    - In JupyterLab's file browser, you can open it using `File` → `Open from Path...`
- Notice `.gitignore` itself now shows up in `git status` as untracked. The `.gitignore` file **should** be committed, so that your whole team shares the same ignore rules

#### c. Ignore auto-generated folders
- Add these lines to `.gitignore` and save:
    ```
    # Python and Jupyter generated folders
    __pycache__/
    .ipynb_checkpoints/
    ```
- Run `git status`. Both folders have disappeared from the list
    - The trailing `/` means "a folder with this name", wherever it is in the repo

#### d. Ignore all files of a specific file type
- Add:
    ```
    # Do not save input data
    *.xlsx
    ```
- Run `git status`. `2024 output/` has disappeared too, since the only file in it is an `.xlsx` file
    - A pattern without a `/` matches files in **any** folder of the repo

#### e. Make an exception
- We don't want to commit input data, but we **do** want to share output data with our team. Add below the `*.xlsx` line:
    ```
    # But DO save output data
    !*output/*.xlsx
    ```
    - `*output/` matches any folder with a name ending in `output`, so `2024 output` gets caught
- Run `git status`. `2024 output/` is back
    - `git status` collapses untracked folders into one line. Run `git status -u` to see `2024 output/summary.xlsx` listed individually
- Now try moving the `!*output/*.xlsx` line **above** `*.xlsx`, and run `git status` again
    - `2024 output/` is ignored again. Later lines override earlier ones, so always put your exceptions **after** the wide ignore
- Move it back before continuing

#### f. Which rule is ignoring my file?
When your `.gitignore` gets longer, it can be hard to tell why a file is being ignored (or not). Try:
```
git status --ignored
git check-ignore -v __pycache__
```
- `git status --ignored` adds a section listing all ignored files and folders
- `git check-ignore -v <file>` prints the `.gitignore` file, line number and pattern that ignores the file. If it prints nothing, the file is not ignored

#### g. Commit and push your `.gitignore`
```
git add .gitignore
git commit -m "chore: add .gitignore"
git push
```

<hr>

#### What if the file you want to gitignore has already been pushed?
`.gitignore` only stops **untracked** files from being added. If a file was already committed before you ignored it, Git keeps tracking it.

Remember `minions.xlsx`, which we committed and pushed in Activity 3? Our new `*.xlsx` rule should ignore it, but:

- Run `git check-ignore -v minions.xlsx`
    - It prints **nothing**. Tracked files are not affected by `.gitignore` at all
- Check your repo on GitLab. `minions.xlsx` is still there
- To stop tracking it **without deleting it from your machine**, run:
    ```
    git rm --cached minions.xlsx
    git status
    ```
    - `minions.xlsx` is staged as `deleted`, but run `ls` and you will see the file is still in your folder
    - For a whole folder, use `git rm -r --cached <folder>`
- Commit and push:
    ```
    git commit -m "chore: stop tracking minions.xlsx"
    git push
    ```
- Run `git check-ignore -v minions.xlsx` again. Now it shows the `*.xlsx` rule, as the file is untracked and the rule applies
- Check your repo on GitLab. `minions.xlsx` is gone from the files list

<hr>

⚠️ The file is no longer tracked, but it **still exists in your commit history**. On GitLab, go to `Code` → `Commits`, open the `data: add minions visitorship dataset` commit, and you can still find `minions.xlsx` there. Anyone with access to the repo can still see it.

This is why you should set up your `.gitignore` at the **start** of a project, before your first `git add .`. If a real password or API key is ever pushed, treat it as leaked and change it immediately. We will cover this in Session 2.


<br>


## Recap

In this session, we learnt the local workflow:

1. **Check** your changes with `git status` (and `git diff`, or the VSCode Source Control panel)
2. **Stage** the changes you want with `git add`, and unstage with `git restore --staged`
3. **Commit** them with a clear message using `git commit -m` or `git commit`
4. **Fix** your last unpushed commit with `git commit --amend`
5. **Push** your commits to GitLab with `git push`
6. **Prevent** files from being committed with `.gitignore`

**Check your understanding**
<details>
<summary>1. <code>git status</code> says <code>Your branch is ahead of 'origin/main' by 2 commits</code>. What does this mean?</summary>

You have 2 commits in your local repo that have not been pushed to GitLab yet. Run `git push` to upload them.
</details>

<details>
<summary>2. You ran <code>git add .</code> and realised it staged a file you didn't want to commit. How do you fix it?</summary>

Run `git restore --staged <file>` to unstage it. Your changes to the file are kept.
</details>

<details>
<summary>3. You spotted a typo in a commit message you pushed yesterday. Should you use <code>git commit --amend</code>?</summary>

No. `--amend` replaces the commit, which rewrites history your teammates may have already pulled. For a minor typo in a pushed commit, just leave it.
</details>

<details>
<summary>4. Why does <code>git status</code> say your notebook is modified even though you didn't change any code?</summary>

Running a notebook changes its execution counts, outputs and metadata, which are all stored in the `.ipynb` file.
</details>

<details>
<summary>5. You added <code>*.csv</code> to <code>.gitignore</code>, but <code>data.csv</code> still shows as modified in <code>git status</code>. Why?</summary>

`data.csv` was already committed (tracked) before you ignored it. Run `git rm --cached data.csv` and commit to stop tracking it.
</details>

Refer to [Git Summary Notes](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link), Section 2. Cloning a repository and Section 3. Local Workflow for more information.

<br>

## End of Session 1
- In this session, we worked in our own repo, so only we could see and change it
- In the next session, we will clone the shared `Minions Visitorship` repo, push and pull changes alongside our teammates, and learn what happens when our changes conflict
