<!--
FACILITATOR NOTES (hidden when rendered — delete before sharing)

Practice repo this draft assumes (rename freely, then find-and-replace below):
  git-practice/
  ├── README.md
  ├── participants.md          ← one "### Participant NN" section per participant
  ├── favourite_museums.py     ← one `participant_NN = {...}` block per participant
  ├── notebooks/
  │   └── visitor_counts.ipynb ← small notebook: loads a tiny DataFrame, prints a total, plots a bar chart
  └── scripts/
      └── make_junk_files.py   ← generates files for the .gitignore activity (see Activity 7)
  NO .gitignore committed at the start.

Each participant block in favourite_museums.py should look like this (with a deliberate "bug"):
  # ===== Participant 01 =====
  participant_01 = {
      "name": "",
      "favourite_museum": "",
      "visits_last_year": "0",  # BUG: this should be an int, not a string
  }

scripts/make_junk_files.py should create:
  .env                          (FAKE_API_KEY=abc123)
  pipeline.log, scripts/debug.log
  data/raw/visitors.csv, data/raw/visitors_2024.csv, data/keep_this.csv
  2025 output/summary.csv
  config.json, scripts/config.json
  __pycache__/  (e.g. by importing favourite_museums)

Heads-up for Session 2 (pushing):
  - Everyone creating their own .gitignore at the repo root will conflict when pushed.
  - Notebook metadata/outputs conflict easily even when people edit different cells.
  Consider telling participants these commits stay local, or pre-plan how Session 2 handles them.

Assign each participant a number (NN) before the session.
-->

# Session 1: Local Workflows

### Overview

In Session 0, you set up Git and created your first repos. In this session, we will learn the **local workflow**: the everyday cycle of making changes, reviewing them, staging them and committing them to your local repo.

Everything in this session happens on **your own machine only**. Nothing you do today will be seen by your teammates yet. We will learn how to push our work to GitLab in Session 2.

> **Required**:
> - Session 0 completed (Git identity configured, GitLab PAT set up)
> - `git-practice` repository on GitLab (link provided by the facilitator)
> - Your participant number (provided by the facilitator), referred to as `NN` below

| Activity | Topic | Est. time |
| --- | --- | --- |
| 1 | Cloning the practice repo | 10 min |
| 2 | The three areas of a Git repo | 10 min |
| 3 | Reviewing, staging and committing changes | 15 min |
| 4 | Writing good commit messages | 15 min |
| 5 | Multi-line commits and amending commits | 10 min |
| 6 | Git with Jupyter notebooks | 10 min |
| 7 | Ignoring files with `.gitignore` | 20 min |
| — | Recap | 5 min |

<br>

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
      <td>Show <strong>unstaged</strong> changes (working directory vs staging area)<br>Show unstaged changes for a specific file</td>
    </tr>
    <tr>
      <td><code>git diff --staged</code><br><code>git diff --staged &lt;file&gt;</code></td>
      <td>Show <strong>staged</strong> changes, i.e. what will go into your next commit<br>Show staged changes for a specific file</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git add file1 file2 file_n</code><br><code>git add .</code></td>
      <td>Stage a specific file<br>Stage a variable number of files at once<br>Stage everything in the present working directory</td>
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


## Activity 1: Cloning the Practice Repo

In Session 0, you cloned a brand new, empty repo. This time, we will clone a repo that already has files and a commit history, just like joining an ongoing project.

> **Terms:**
> - **Remote repo**: The version of your repository hosted on GitLab / Github. This is the central copy that your whole team pushes to and pulls from.
> - **Local repo**: The version of your repository on your own machine. This is where you make changes before pushing them up to the remote.

#### a. Navigate to your home directory
```
cd ~
```

#### b. Clone the practice repo
- Go to the `git-practice` repo page on GitLab and copy the HTTPS address
- Run:
    ```
    git clone <HTTPS_address>
    ```
- This saves the repo as a folder in your current working directory

#### c. Navigate into the repo and look around
```
cd git-practice
ls -a
```
- You should see `README.md`, `participants.md`, `favourite_museums.py`, `notebooks/`, `scripts/`, and the hidden `.git` folder
- Open each file in the UI and have a quick look at what's inside. Find **your** participant section (`Participant NN`) in `participants.md` and `favourite_museums.py`
    - ⚠️ Throughout this session, only edit **your own** section. This will matter in Session 2 when we start pushing our changes.

#### d. Check your remote is configured correctly
```
git remote -v
```
- The two lines of output should match the URL of the repo on GitLab
- `origin` is the alias Git gave the remote repo when you cloned it, so you don't have to type out the whole URL in future

#### e. Check the state of the repo
```
git status
```
- You should see `nothing to commit, working tree clean`. This means your local files match the latest commit exactly

#### f. Look at the commit history
```
git log
git log --oneline
git log -n 2
```
- `git log` shows the full details of each commit: hash, author, date and message
- `git log --oneline` condenses each commit into one line: a short hash and the message
- `git log -n 2` only shows the 2 most recent commits. You can combine flags, e.g. `git log --oneline -n 2`
- Remember to press `q` to exit if the output fills your screen

<hr>

Cloning gives you the **entire history** of the project, not just the latest files. Every commit you see in `git log` is now stored in the `.git` folder on your machine.

<br>


## Activity 2: The Three Areas of a Git Repo

Before we start committing, it helps to understand where your changes "live" at each step. Git has three areas:

```
 Working Directory          Staging Area              Local Repo (commits)
 (your files)               (next commit)             (history)
 ─────────────────          ─────────────             ─────────────────────
   edit files   ── git add ──►  staged   ── git commit ──►  committed
```

- **Working directory**: the actual files in your folder. Any edits you make in the UI happen here
- **Staging area**: a "draft" of your next commit. You choose which changes go into it using `git add`
- **Local repo**: the permanent history of commits, stored in `.git`. `git commit` takes everything in the staging area and saves it as a new commit

Why have a staging area at all? It lets you **choose** exactly what goes into each commit, even if you have changed many files at once.

`git status` tells you which area each change is in. Let's see it in action.

#### a. Make a change
- Open `participants.md` and fill in your name under `### Participant NN`. Save the file

#### b. Check the status
```
git status
```
- `participants.md` is listed under **`Changes not staged for commit`**
- This means Git has noticed the file changed in your working directory, but the change is not staged yet

#### c. Create a new file
- In the repo's root folder, create a new file named `notes_NN.md` (replace `NN` with your number) and type a sentence in it. Save it
- Run `git status` again
- `notes_NN.md` appears under **`Untracked files`**. Git has never seen this file before, so it is not tracking it at all yet

#### d. Stage one file
```
git add participants.md
git status
```
- `participants.md` has moved to **`Changes to be committed`**. It is now staged
- `notes_NN.md` is still untracked, since we did not stage it

#### e. Stage the other file
```
git add notes_NN.md
git status
```
- Both files are now under `Changes to be committed`
- Notice `new file:` next to `notes_NN.md` and `modified:` next to `participants.md`
- Don't commit yet, we will do it in the next activity

<hr>

Read the hints in `git status` output. Git often tells you the exact command to run next, e.g. `(use "git add <file>..." to update what will be committed)`. We will cover how to unstage and undo changes in Session 4.

<br>


## Activity 3: Reviewing, Staging and Committing Changes

**Git commands (main)**

```bash
git add <file>                    # stage a specific file
git add file1 file2 file_n        # stage a variable number of files at once
git add .                         # stage everything
git commit -m "commit message"    # commit staged changes
```

Before staging and committing, it is good practice to **review your changes** using `git diff`:

```bash
git diff             # changes NOT yet staged (working directory vs staging area)
git diff --staged    # changes that ARE staged (what will go into your next commit)
```

#### a. Commit your staged changes from Activity 2
- First, check what is about to be committed:
    ```
    git diff --staged
    ```
    - Lines starting with `+` (green) were added, lines starting with `-` (red) were removed
- Commit the staged changes:
    ```
    git commit -m "docs: add my name and notes file"
    ```
    - We will explain the `docs:` part of the message in Activity 4
- Run `git status`: the working tree is clean again
- Run `git log --oneline`: your commit is at the top

#### b. See the difference between `git diff` and `git diff --staged`
- Open `favourite_museums.py`. In **your** `participant_NN` block, fill in `"name"` and `"favourite_museum"`. Save the file
- Run:
    ```
    git diff
    ```
    - You see your changes, because they are **not staged** yet
- Now run:
    ```
    git diff --staged
    ```
    - You see **nothing**, because nothing is staged yet
- Stage the file, then run both commands again:
    ```
    git add favourite_museums.py
    git diff
    git diff --staged
    ```
    - Now `git diff` shows nothing and `git diff --staged` shows your changes. The changes moved from the working directory to the staging area

#### c. Edit a file that is already staged
- Without committing, go back to `favourite_museums.py` and change `"visits_last_year": "0"` to any other number, still in quotes, e.g. `"5"`. Save the file
- Run `git status`
    - `favourite_museums.py` appears **twice**: under `Changes to be committed` AND `Changes not staged for commit`
- Run `git diff` and `git diff --staged` to see which change is where
    - **Staging takes a snapshot of the file at the moment you run `git add`.** Any edits after that are not included unless you `git add` again
- Stage the new edit and commit:
    ```
    git add favourite_museums.py
    git commit -m "feat: add my favourite museum details"
    ```

#### d. Stage multiple files at once
- Make a small edit to **your** section in `participants.md`, e.g. add a line about your role
- Create another new file `todo_NN.md` with a line of text
- Stage both files in one command, then commit:
    ```
    git add participants.md todo_NN.md
    git status
    git commit -m "docs: add role and todo list"
    ```

#### e. Stage everything with `git add .`
- Make any small edit to `notes_NN.md` and `todo_NN.md`
- Run `git status` to check exactly what has changed, then:
    ```
    git add .
    git status
    git commit -m "docs: update notes and todo list"
    ```
- ⚠️ `git add .` stages **everything** that changed in your present working directory (and its subfolders). Always run `git status` first so you don't accidentally commit files you didn't mean to, like data files or credentials. We will learn how to prevent this with `.gitignore` in Activity 7

<hr>

`git status` shows which files have been staged or committed. Use this to check which files will be affected before you commit (and later, before you push).

A good habit before every commit: **`git status` → `git diff` → `git add` → `git diff --staged` → `git commit`**

<br>


## Activity 4: Writing Good Commit Messages

**Commit messages**

Convention for writing commit messages (See [Conventional Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/)):

```html
<type>(<optional scope>): <description>
empty line as separator
<optional body>
empty line as separator
<optional footer>
```

- **Why follow a standard for commit messages?**
    - A commit message is a note to your future self and your teammates explaining what changed and why. When you're debugging a problem weeks later or onboarding someone new to the project, a well-written commit history is invaluable.
    - Following a standard structure makes the repo's commit history easier to parse by the whole team, and makes it easier to understand what each commit changed without having to read all the actual code changes.
- **For example, if you are committing the addition of a new model to a ML pipeline**

    **Minimally include the commit type and a short description**

    ```html
    feat: add GBT Classifier to ML pipeline
    ```

    **Most descriptive (summary + body + footer)**

    ```html
    feat(pipeline): add GBT Classifier to ML pipeline

    Added Gradient Boosted Trees (GBT) Classifier as an additional model
    in the training pipeline. The model is trained with default
    hyperparameters as a baseline and evaluated alongside existing models
    using the same train-test split and metrics.

    Closes #42
    ```

**Industry-standard Commit Types**

| **Type** | **Use for** |
| --- | --- |
| `feat` | Adding, modifying or removing a feature or analysis<br>E.g. `feat(auth): add password reset function` |
| `fix` | Bug fix<br>E.g. `fix(api): correct NA handling in cleaning script` |
| `refactor` | Restructure code without changing behaviour<br>E.g. `refactor: rewrite function to be more concise` |
| `style` | Code style changes without changing behaviour<br>E.g. `style: run prettier` |
| `chore` | Cleanup, renaming, formatting of folder structure. Maintenance tasks not affecting source or tests.<br>E.g. `chore: rearrange files` |
| `docs` | Changes to documentation or README<br>E.g. `docs: update README` |

**Data-oriented Commit Types**

| **Type** | **Use for** |
| --- | --- |
| `data` | Adding, updating or removing data sources or raw files.<br>E.g. `data: add 2025 vouch ticketing data` |
| `analysis` | Exploratory or ad-hoc analysis.<br>E.g. `analysis: explore invalid order rows with non-NA Refunded At, Refunded Amount, Cancelled At` |
| `model` | Changes to model architecture, hyperparameters or evaluation.<br>E.g. `model: add GBT Classifier pipeline` |
| `pipeline` | Changes to data pipeline or workflow steps.<br>E.g. `pipeline: add feature engineering step before model training` |

We don't have to stick to the above commit types strictly. We can come up with our own ones as a team. We will discuss this further in Session 6: Team Workflow Standards.

#### a. Quick exercise: pick the commit type
For each change below, decide which commit type fits best. Discuss with the person next to you.

1. You corrected a column name typo that was causing a `KeyError` in the cleaning script
2. You added a new section to the README explaining how to run the analysis
3. You added this month's raw visitor CSV to the `data/` folder
4. You renamed and moved notebooks into a `notebooks/` folder
5. You added a chart comparing visitorship across museums
6. You split one long function into three shorter functions, with the same output

<details>
<summary>Answers</summary>

1. `fix`
2. `docs`
3. `data`
4. `chore`
5. `feat` or `analysis`
6. `refactor`

</details>

#### b. Make one change per commit (atomic commits)
When possible, a commit should encompass a single feature, change, or fix. This makes it much easier to undo specific changes later on, and makes your project easier to review. Let's practise by making two **unrelated** changes, then committing them **separately**.

- **Change 1 (a bug fix):** In your `participant_NN` block in `favourite_museums.py`, `"visits_last_year"` is stored as a string (e.g. `"5"`), but it should be a number. Remove the quotes (e.g. `5`) and delete the `# BUG` comment. Save the file
- **Change 2 (documentation):** In **your** section of `participants.md`, add a line `Favourite commit type: <type>`. Save the file
- Run `git status`: both files are modified
- Stage and commit **only** the bug fix:
    ```
    git add favourite_museums.py
    git commit -m "fix: store visits_last_year as an integer"
    ```
- Then stage and commit the documentation change:
    ```
    git add participants.md
    git commit -m "docs: add favourite commit type"
    ```
- Run `git log --oneline` and read your commit history. Notice how easy it is to tell what each commit did without opening any files

<hr>

This is exactly why the staging area exists: even if you changed many files, you choose which ones go into each commit.

<br>


## Activity 5: Multi-line Commits and Amending Commits

**Other commit commands**

```bash
git commit       # opens a nano window for you to write multi-line commit messages
git commit --amend -m "corrected message"    # rewrite message for the last commit
```

`git commit -m` is fine for short messages. When you want to include a body explaining **why** you made a change, use `git commit` without `-m` to write your message in the nano text editor.

#### a. Make a change to commit
- In your `participant_NN` block in `favourite_museums.py`, add a new key `"favourite_exhibit"` with any value. Save the file
- Stage it:
    ```
    git add favourite_museums.py
    ```

#### b. Write a multi-line commit message
- Run `git commit` just like that to open a nano window for writing the commit message

    ![nano window opened by git commit](notion-notes/image%203.png)

- Write your multi line message in the space provided, above the lines starting with `#`, following the convention from Activity 4. For example:
    ```
    feat: add favourite exhibit for participant NN

    Added a favourite_exhibit field so we can later analyse which
    exhibits are most popular across participants.
    ```

    ![multi-line commit message written in nano](notion-notes/image%204.png)

    - Lines starting with `#` are ignored, so you don't need to delete them
    - An empty message aborts the commit
- Save and exit nano:
    1. Press `Ctrl + X` to exit the nano window
    2. nano asks `Save modified buffer?`. Press `Y`
    3. nano shows the file name to save to. Press `Enter` to confirm
- Once you exit, Git automatically creates the commit
- Run `git log` (not `--oneline`) to see your full multi-line message. Press `q` to exit

#### c. Fix a typo in your last commit message
- Make a small change to your section in `participants.md` and commit it with a deliberate typo:
    ```
    git add participants.md
    git commit -m "docs: updaet participant detials"
    ```
- Oops. Rewrite the message of the last commit:
    ```
    git commit --amend -m "docs: update participant details"
    ```
- Run `git log --oneline`. The commit with the typo is gone, replaced by one with the corrected message
- Tip: run `git commit --amend` without `-m` to edit the last commit message in nano instead

#### d. Add a forgotten file to your last commit
- Make an edit to `todo_NN.md` **and** `notes_NN.md`, but only stage and commit one of them:
    ```
    git add todo_NN.md
    git commit -m "docs: update todo list and notes"
    ```
- You realise you forgot to include `notes_NN.md`. Instead of making a separate commit, stage it and add it into the last commit:
    ```
    git add notes_NN.md
    git commit --amend --no-edit
    ```
    - `--no-edit` keeps the existing commit message
- Run `git log --oneline -n 3` and `git status` to confirm there is still only one commit, and it now includes both files

<hr>

⚠️ **Only amend commits that you have NOT pushed yet.** `--amend` does not edit a commit, it *replaces* it with a new one. If you have already pushed the commit, rewriting remote history is dangerous and messy when working in a team. For a minor typo in a pushed commit message, just leave it. We will cover what to do about pushed commits in Session 2 and Session 4.

<br>


## Activity 6: Git with Jupyter Notebooks

So far, we have worked with `.py` and `.md` files, which are plain text. When you change one line, `git diff` shows exactly one line changed.

Jupyter notebooks (`.ipynb`) look like cells in the UI, but underneath they are one large **JSON** file that stores your code **and** cell outputs, execution counts, and metadata. Let's see what that means for Git.

#### a. Look at what a notebook really is
- Open `notebooks/visitor_counts.ipynb` in a plain text editor instead of the notebook UI
    - In JupyterLab: right-click the file → **Open With** → **Editor**
- Notice the notebook is stored as JSON, with `"cell_type"`, `"source"`, `"outputs"`, `"execution_count"` and `"metadata"` fields. Close it without saving

#### b. Run the notebook without changing any code
- Open the notebook normally, and run all cells (**Run** → **Run All Cells**). Save the notebook
- Run:
    ```
    git status
    git diff notebooks/visitor_counts.ipynb
    ```
- Even though you did not change a single line of code, Git reports the notebook as **modified**
- Scroll through the diff (press `q` to exit). The changes are `execution_count` numbers, outputs, and possibly metadata, and the bar chart shows up as a long block of encoded image data

#### c. Now make a one-line code change
- In the notebook, change the chart title in the plotting cell to include your participant number. Run the cell again and save
- Run `git diff notebooks/visitor_counts.ipynb` again
- Try to find your one-line change. It is buried among the output and metadata changes
- Compare this with the `git diff` of `favourite_museums.py` in Activity 3, where your change was obvious

#### d. Clear outputs, then commit
- In the notebook: **Kernel** → **Restart Kernel and Clear Outputs of All Cells**, then save
- Run `git diff notebooks/visitor_counts.ipynb` again
    - The diff is much smaller, and your actual code change is easy to find
- Stage and commit:
    ```
    git add notebooks/visitor_counts.ipynb
    git commit -m "analysis: add participant number to chart title"
    ```

<hr>

**Tips for working with notebooks in Git:**
- Simply opening and running a notebook creates changes, even with no code changes. Always check `git status` and `git diff` before running `git add .`
- Clearing outputs before committing keeps diffs small and readable, and keeps large images out of your commit history
- Keep reusable logic (e.g. cleaning functions) in `.py` files and import them into your notebooks. `.py` files are much easier to review and track with Git
- Notebook changes are also much more likely to cause **merge conflicts** when working in a team. We will see this in Session 2

<br>


## Activity 7: Ignoring Files with `.gitignore`

**Ignoring Files**

We can tell Git which files and directories to ignore in a given repository, using a `.gitignore` file. This is useful for files you know you NEVER want to commit, including:

- Secrets, API keys, credentials (e.g. `.env`)
- Operating System files (`.DS_Store` on Mac)
- Log files (`*.log`)
- Dependencies & packages (e.g. `node_modules/` for node applications, `__pycache__/` for python)
- `.venv/` , `.ipynb_checkpoints/`

For data teams, this also often includes **data files**, which may be large or contain sensitive information that should not be stored in GitLab.

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

#### a. Generate some files you should not commit
- Make sure you are in the root folder of the repo (`git-practice`), then run:
    ```
    python scripts/make_junk_files.py
    ```
- Run `git status`. You should see a long list of untracked files and folders, including:
    - `.env` (a fake API key)
    - `pipeline.log` and `scripts/debug.log`
    - `data/` (containing raw CSVs and a `keep_this.csv`)
    - `2025 output/` (containing `summary.csv`)
    - `config.json` and `scripts/config.json`
    - `__pycache__/`
    - `notebooks/.ipynb_checkpoints/` (created automatically by JupyterLab when you opened the notebook in Activity 6)
- Imagine running `git add .` now. All of these would be committed, including your API key 😱

#### b. Create a `.gitignore` file
- In the **root folder** of the repo, create a new file named exactly `.gitignore` (note the leading dot, and no file extension)
    - Or, from the terminal: `touch .gitignore`
- Tip: files starting with `.` are hidden. Use `ls -a` to see it in the terminal. In JupyterLab's file browser, you can open it using **File** → **Open from Path...**, or enable **View** → **Show Hidden Files**

#### c. Ignore a specific file
- Add this line to `.gitignore` and save:
    ```
    # Secrets
    .env
    ```
- Run `git status`. `.env` has disappeared from the untracked files list
- Notice `.gitignore` itself now appears as an untracked file. The `.gitignore` file **should** be committed, so the whole team shares the same ignore rules

#### d. Ignore all files of a specific file type
- Add:
    ```
    # Log files
    *.log
    ```
- Run `git status`. Both `pipeline.log` **and** `scripts/debug.log` are gone
    - A pattern without a `/` matches files in **any** folder of the repo

#### e. Ignore a whole folder
- Add:
    ```
    # Python and Jupyter generated folders
    __pycache__/
    .ipynb_checkpoints/
    ```
- Run `git status`. Both folders are gone
    - The trailing `/` means "a folder with this name", wherever it is in the repo

#### f. Ignore a folder's contents, except one file
- First, try adding:
    ```
    # Data
    data/
    !data/keep_this.csv
    ```
- Run `git status`. `data/keep_this.csv` is **still ignored**!
    - When you ignore a whole folder with `data/`, Git does not even look inside it, so the `!` exception never gets a chance to apply
- Change those two lines to:
    ```
    # Data
    data/*
    !data/keep_this.csv
    ```
- Run `git status`. Now `data/` shows up as untracked again
    - `git status` collapses untracked folders into one line. To see the individual files, run `git status -u`: only `data/keep_this.csv` is listed, while the other CSVs in `data/` stay ignored
    - `data/*` ignores the folder's **contents**, so Git still looks inside the folder and can apply the exception
- Now try swapping the order of the two lines, putting `!data/keep_this.csv` **above** `data/*`. Run `git status`
    - `keep_this.csv` is ignored again. Order of entries DOES matter: later lines override earlier ones, so put your exceptions after the wide ignore
- Swap them back before continuing

#### g. Ignore a file only in the root directory
- Add:
    ```
    # Local config
    /config.json
    ```
- Run `git status`. The root `config.json` is ignored, but `scripts/config.json` still shows up
    - A leading `/` means "only in the same folder as this `.gitignore`"
- Change the line to `**/config.json` and run `git status`. Now both are ignored
    - `**/` matches any folder depth
    - Note: `config.json` on its own (no slashes) would also match in any folder, like `*.log` in step d. `**/` makes that intent explicit

#### h. Which rule is ignoring my file?
When your `.gitignore` gets longer, it can be hard to tell why a file is being ignored (or not). Try:
```
git status --ignored
git check-ignore -v data/raw/visitors.csv
git check-ignore -v data/keep_this.csv
```
- `git status --ignored` adds a section listing all ignored files
- `git check-ignore -v <file>` prints the `.gitignore` file, line number and pattern that ignores the file. If it prints nothing, the file is not ignored

#### i. A realistic `.gitignore` for data projects
Here is the sample `.gitignore` from the notes. Read through it and predict what happens to `2025 output/summary.csv`:

```bash
__pycache__/

# Do not save input data
*.csv
*.xlsx

# But DO save output data
# Output data is usually exported to a folder named f"{YEAR} output"
!*output/*.csv
!*output/*.xlsx

# Note: *output/ refers to any folder with name ending in "output"
# so a folder named "2024 output" would get caught
```

- Add the `*.csv` and `!*output/*.csv` lines to the **bottom** of your `.gitignore` and run `git status -u` to check your prediction
    - `2025 output/summary.csv` is **not** ignored: `*.csv` ignores it, then `!*output/*.csv` un-ignores it
- But look again: `data/keep_this.csv` has disappeared from the list! Find out why:
    ```
    git check-ignore -v data/keep_this.csv
    ```
    - The new `*.csv` line comes **after** `!data/keep_this.csv`, so it ignores the file again
    - Fix it by moving `!data/keep_this.csv` to the bottom of the file, and run `git status -u` again
- Your `.gitignore` is now fairly complete. Run `git status -u` one last time: only `.gitignore`, `data/keep_this.csv` and `2025 output/summary.csv` should be left as untracked
- Commit only the `.gitignore`:
    ```
    git add .gitignore
    git commit -m "chore: add .gitignore"
    ```

#### j. ⚠️ `.gitignore` does not affect files that are already tracked
`.gitignore` only stops **untracked** files from being added. If a file was already committed before you ignored it, Git keeps tracking it.

- Simulate this mistake. Create a file `secrets.txt` with some fake text, then commit it:
    ```
    git add secrets.txt
    git commit -m "chore: add secrets file"
    ```
- Now add `secrets.txt` to your `.gitignore` and save. Then edit `secrets.txt` and save
- Run `git status`. `secrets.txt` still shows as **modified**, since it is already tracked
- To stop tracking it **without deleting it from your machine**:
    ```
    git rm --cached secrets.txt
    git status
    ```
    - `secrets.txt` is staged as `deleted`, but the file is still in your folder. From now on, the `.gitignore` rule applies
    - For a folder, use `git rm -r --cached <folder>`
- Commit the change:
    ```
    git add .gitignore
    git commit -m "chore: stop tracking secrets.txt"
    ```

<hr>

The file is no longer tracked, but it **still exists in earlier commits** in your history. Anyone with access to the repo can still see it there. This is why you should set up your `.gitignore` at the **start** of a project, before your first `git add .`. If a real password or API key is ever committed and pushed, treat it as leaked and change it immediately.

<br>


## Recap

In this session, we learnt the local workflow:

1. **Review** your changes with `git status` and `git diff`
2. **Stage** the changes you want with `git add` (and review them again with `git diff --staged`)
3. **Commit** them with a clear, conventional message using `git commit -m` or `git commit`
4. **Fix** your last unpushed commit with `git commit --amend`
5. **Check** your history with `git log --oneline`
6. **Prevent** files from being committed with `.gitignore`

**Check your understanding**
<details>
<summary>1. You edited a file, ran <code>git add</code>, then edited it again. What will <code>git commit</code> include?</summary>

Only the version of the file at the moment you ran `git add`. The later edit is still unstaged, and needs another `git add` to be included.
</details>

<details>
<summary>2. <code>git diff</code> shows nothing, but <code>git status</code> says there are changes to be committed. Why?</summary>

`git diff` only shows **unstaged** changes. The changes have already been staged, so use `git diff --staged` to see them.
</details>

<details>
<summary>3. You added <code>*.csv</code> to <code>.gitignore</code>, but <code>data.csv</code> still shows as modified in <code>git status</code>. Why?</summary>

`data.csv` was already committed (tracked) before you ignored it. Run `git rm --cached data.csv` and commit to stop tracking it.
</details>

<details>
<summary>4. Why does <code>git status</code> say your notebook is modified even though you didn't change any code?</summary>

Running a notebook changes its execution counts, outputs and metadata, which are all stored in the `.ipynb` file.
</details>

Refer to [Git Summary Notes](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link), Section 2. Cloning a repository and Section 3. Local Workflow for more information.

<br>

## End of Session 1
- In this session, all our commits were saved to our **local repo** only. If you go to the `git-practice` repo on GitLab now, none of your commits are there
- In the next session, we will push our commits to GitLab, pull our teammates' changes, and learn what happens when our changes conflict
