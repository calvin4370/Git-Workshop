# Session 2: Remote Workflows and Conflict Resolution

### Reference Table

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
      <td>Copy a remote repo onto your machine as a new folder</td>
    </tr>
    <tr>
      <td><code>git status</code></td>
      <td>See what has changed, what is staged, and which files have merge conflicts</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git add .</code></td>
      <td>Stage a specific file<br>Stage everything in the present working directory</td>
    </tr>
    <tr>
      <td><code>git commit -m "commit message"</code></td>
      <td>Commit staged changes with a single-line message</td>
    </tr>
    <tr>
      <td><code>git commit</code></td>
      <td>Open nano to write a commit message. After resolving a conflict, the merge message is pre-filled</td>
    </tr>
    <tr>
      <td><code>git push</code></td>
      <td>Upload your local commits to the remote branch</td>
    </tr>
    <tr>
      <td><code>git log --oneline</code></td>
      <td>View commit history, one line per commit</td>
    </tr>
    <tr>
      <td><code>git pull</code></td>
      <td>Download remote changes and merge them into your current branch (<code>git fetch</code> + <code>git merge</code>)</td>
    </tr>
    <tr>
      <td><code>git push -u origin &lt;branch&gt;</code></td>
      <td>First push of a new branch. Links it to the remote branch, so later pushes and pulls only need <code>git push</code> / <code>git pull</code></td>
    </tr>
    <tr>
      <td><code>git merge --abort</code></td>
      <td>Cancel a merge in progress and return to how things were before you pulled</td>
    </tr>
    <tr>
      <td><code>git log --oneline --graph</code></td>
      <td>Commit history, with lines showing where work split and merged</td>
    </tr>
    <tr>
      <td><code>git fetch</code></td>
      <td>Download remote branches and commits <strong>without</strong> merging them or touching your working directory</td>
    </tr>
    <tr>
      <td><code>git branch</code><br><code>git branch -a</code></td>
      <td>List local branches (current branch highlighted)<br>List all branches, including remote ones</td>
    </tr>
    <tr>
      <td><code>git switch &lt;branch&gt;</code></td>
      <td>Switch to another branch (covered in Session 3)</td>
    </tr>
    <tr>
      <td><code>git restore &lt;file&gt;</code></td>
      <td>Discard uncommitted changes to a file. <strong>These changes cannot be recovered</strong> (covered in Session 4)</td>
    </tr>
  </tbody>
</table>

<br>

## Overview

> In Session 1, you cloned a brand new, empty repo you created yourself on GitLab
>
> This time, we will clone a repo that already has files and a commit history, just like joining an ongoing project.

<br>

## Setup

> `Minions Visitorship` is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

#### a. Clone the `Minions Visitorship` repo

- Navigate to your home directory using `cd ~`
- Run `git clone https://gitlab.analytics.gov.sg/gcc_jun_jie_chan_from.tp/minions-visitorship.git`
- Navigate into the project folder using `cd minions-visitorship`

#### b. Switch to a different branch (`minions-visitorship` repo)

> Branching lets you create a separate line of work that diverges from `main` without affecting it. This allows you to work on something unfinished without breaking what already works, and lets many people work in parallel without getting in one another's ways.
>
> `main` should always be in a working state (production). Branches are for work-in-progress changes.
>
> We will go through branching in detail in Session 3 Branching.

- Run `git switch s2` to switch to the `s2` branch of the repo
- This is to prevent you from pushing changes to modify my clean `main` branch (I have also configured the GitLab repo to not accept direct pushes to main).

#### c. Install the workshop dependencies

- From the root of the `minions-visitorship` repo, run:

  ```bash
  pip install -r requirements.txt
  ```

<br>

## Activity 1: Pushing and Pulling Changes

> Repo: `minions-visitorship`
> Branch: `s2`

> We will demonstrate pushing and pulling with 4 participants. Each person will push changes to the repo, and pull the updated state of the repo

- Open the Jupyter notebook at `minions-visitorship/session2_lab/analysis.ipynb`

<br>

#### a. Participant 1 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- You should see:
  ![Output of git pull](../../assets/already.png)
- Find the cell under **Config** with the code `YEAR = 2024`
    - Edit the code into `YEAR = 2025`
    - Rerun the notebook to regenerate the plot outputs for 2025
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: rerun notebooks for 2025 data"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### b. Participant 2 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- You should see:
  ![Output of git pull](../../assets/pull-part2.png)
    - This time, `git pull` lists the files that changed, as it is pulling in Participant 1's commit
- Find the first plot, **Top 10 minions by visits**, and look at the code cell under it: `plot_top_minions(visits, MINION_YELLOW, YEAR)`
    - The 2nd argument is the colour of the bars
    - Replace `MINION_YELLOW` with any other colour from the minion colour scheme, e.g. `EVIL_PURPLE`
    - The full list of colours is at the top of `functions.py`
    - Rerun the notebook
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: change colour of top minions plot"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### c. Participant 3 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- Find the cell under **Config** with the code `YEAR = 2025`
    - Edit the code back into `YEAR = 2024`
    - Rerun the notebook to regenerate the plot outputs for 2024
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: rerun notebooks for 2024 data"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### d. Participant 4 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- Pick any plot(s) in the notebook
    - e.g. **Visits by museum** has the code cell `plot_visits_by_museum(visits, GOGGLE_GREY, YEAR)`
    - Replace the colour argument with any other colour from the minion colour scheme, e.g. `MARGO_GREEN`
    - Rerun the notebook
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: change colour of plots"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase
>
> Run `git log --oneline` to see all 4 commits in the history. Everyone's local repo now has the same commits, in the same order, as the remote `s2` branch on GitLab.

<br>

## Activity 2: Conflict Resolution

> Repo: `minions-visitorship`
> Branch: `s2`
>
> File: `minions-visitorship/session2_lab/activity2.py`

<hr>

> `git pull` is `git fetch` then `git merge`. It fetches the commits on the remote branch, then merges the equivalent **remote branch** into your **local branch**.
>
> A merge happens whenever two lines of development need to be combined: when you run `git pull`, when you accept a MR on GitLab, or when you run `git merge` directly. Most of the time, Git combines them automatically. As long as you and your teammate changed **different files**, or **different parts of the same file**, Git can tell which change belongs where, and it merges them into a new commit automatically.
>
> A **merge conflict** happens when two branches changed the **same part of the same file**, and Git cannot tell which version should be kept. Git will not guess. It stops the merge, marks the conflicting lines in the affected file(s), and leaves it to you to decide what the final version should look like (Conflict Resolution).

> We will work in `minions-visitorship/session2_lab/activity2.py`, which contains 3 empty functions for us to edit.
>
> ⚠️ If your `git push` is rejected with `Updates were rejected because the remote contains work that you do not have locally`, run `git pull` first, resolve anything Git asks you to, then push again. We will go through why this happens in Activity 4.

#### a. Merging without a conflict

> Each participant edits a **different** function, so nobody touches the same lines.

- **Everyone:** run `git pull`, then open `session2_lab/activity2.py`
- Edit the function assigned to you any way you like.
    - Participant 1 → `function1()`
    - Participant 2 → `function2()`
    - Participant 3 → `function3()`
    - Participant 4 → `function4()`
    - etc. (add more functions if there are more participants)
- **Everyone:** stage and commit your change, but do **not** push yet
    - `git add .`
    - `git commit -m "activity2: <a short description of what you did>"`
- Now push **one at a time**, in order of participant number
    - Participant 1 pushes.
    - Participant 2 runs `git pull`, then `git push`
    - and so on, until the last participant
- Notice that `git pull` merged the previous changes into your own commit **without asking you anything**
    - You both changed `activity2.py`, but you changed **different parts** of it, so Git could tell which change belonged where
- **Everyone:** run `git pull`
    - All 3 functions should now be filled in with everyone's changes

<hr>

#### b. Resolving your first merge conflict

> This time, everyone edits the **same** function, so Git cannot tell whose version to keep.

- **Everyone:** run `git pull` first, so everyone starts from the same commit
- **Everyone:** edit `function1()` in `activity2.py`, writing something different from your teammates (e.g. include your own name in a `print()` statement)
- **Everyone:** stage and commit your change, but do **not** push yet
    - `git add .`
    - `git commit -m "feat(activity2): update function1"`
- **Participant 1:** run `git push`. This works as usual
- **Participants 2 and 3:** run `git pull`
    - Git stops with `CONFLICT (content): Merge conflict in session2_lab/activity2.py`
    - Run `git status`. It says `You have unmerged paths`, and lists `activity2.py` as `both modified`

<hr>

**Resolving the conflict**

- Open `activity2.py`. Git has marked the conflicting lines:

    ```python
    <<<<<<< HEAD
        print("this is my version")
    =======
        print("this is my teammate's version")
    >>>>>>> a1b2c3d
    ```

    - `HEAD` is **your** version (the commit you are merging into)
    - The part below `=======` is the **incoming** version from the remote

- Decide what the final version should look like, then remove **all** the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
    - In VSCode, you do not have to delete them by hand. Buttons appear above the conflict: `Accept Current Change`, `Accept Incoming Change`, `Accept Both Changes`
    - You can also ignore the buttons and simply edit the file into whatever you want the final version to be
- Save the file, then complete the merge:

    ```
    git add session2_lab/activity2.py
    git commit
    ```

    - Git pre-fills the commit message for you, e.g. `Merge branch 's2' of ...`. Just save and exit nano to accept it

- Run `git push`
- Participant 3 does the same. Your conflict will be against the version Participant 2 just merged and pushed

> **Tip:** If you get lost in the middle of a merge, run `git merge --abort`. This cancels the merge and puts your repo back exactly as it was before you pulled, so you can try again. Nothing is lost.

<hr>

#### c. One more round, in a different order

> So that everyone gets to resolve a conflict, we repeat the exercise with the push order rotated.

- **Everyone:** run `git pull`, then edit `function2()` in `activity2.py` with something different from your teammates
- **Everyone:** stage and commit, but do **not** push
- Push in this order: **Participant 2**, then **Participant 3**, then **Participant 1**
    - Participant 2 pushes as usual
    - Participants 3 and 1 will need to `git pull`, resolve the conflict, `git add`, `git commit`, then `git push`
- **Everyone:** run `git pull`, then `git log --oneline --graph`
    - The `--graph` flag draws the lines of work splitting and joining back together at each merge commit

<hr>

<span style="color:salmon">A merge conflict is not an error, and it is not dangerous. Git is simply asking you to decide which version to keep, because it cannot know. The merge is only complete once you remove the conflict markers, `git add` the file and commit.</span>

- Conflicts are much easier to avoid than to resolve. `git pull`/`git pull origin main` often, especially before starting any chunk of work, so that you are always editing the latest version of the code
- Conflicts in Jupyter notebooks are far worse, as the markers land in the middle of the JSON, and the notebook will not open in the UI until you have removed them. This is another reason to keep reusable logic in `.py` files

<br>

## Activity 3: Working with API keys

> Other than rebuildable outputs, large binaries, and clutter which should not be committed for various reasons, there are some environmental variables / files required by your code but still should never be committed to Git.
>
> What to NEVER commit to your Git repositories:
>
> - API keys / tokens
> - Passwords
> - Sensitive personal identifying information (PII)
>
> These should be stored locally on each user's devices or on a secure tool.
>
> If you have pushed your secrets to Gitlab
>
> - If the repo is publicly viewable, bots that scrape open Github / Gitlab repositories for secrets 24/7 will eventually find it and misappropriate your API accounts
> - If the repo is private, it's still irresponsible to push your personal API keys, as anyone who has viewing access to your repo can misappropriate them, or the repo may be made public one day
>
> Undoing code changes, including commits and pushes, is covered in **Session 4: Safe Undo of Code Changes**

<table><tr><td>

**Working Example: MAESTRO LLM API**

- To simulate the generation of your personal LLM API key, I will send each of you your API key individually on Teams.
- Copy and paste it into the relevant code section when prompted

</td></tr></table>

#### a. Navigate into the `minions-visitorship/session2_lab` folder

- While in `/home/jovyan/minions-visitorship`, run `cd session2_lab`

#### b. Try running the program which calls an LLM API

> Note: This is a simulated LLM API, with hardcoded prompts and responses. But I have implementing tracking of users and their prompts, and a dashboard that shows all LLM call logs.

- Run `python api_testing.py "<prompt>"` where \<prompt\> is anything you want to ask an LLM
    - e.g. `python api_testing "what is the weather today"`

- You will see that, as most APIs do, this LLM API requires an API key

#### c. Open the `api_testing.py` file

- You may want to keep this `session2.md` open, and have `api_testing.py` open in split screen

#### d. Copy and paste your personal API key into `api_testing.py`

- You should replace line {edit-here} with your API key
- e.g. `API_KEY = git-ws-123abc456def...`

#### e. Now try running the program again

- You may only choose from the pre-written API prompts below. Copy and paste the prompt as written into your command.
- e.g. `python api_testing.py "what is the weather today"`

<table>
  <!-- <thead>
    <tr>
      <th>Prompts</th>
    </tr>
  </thead> -->
  <tbody>
    <tr><td>what is the weather today</td></tr>
    <tr><td>how to use git</td></tr>
    <tr><td>why is git so hard</td></tr>
    <tr><td>what is the best bubble tea brand in singapore</td></tr>
    <tr><td>when i sneeze, why does it sometimes hurt my tummy</td></tr>
    <tr><td><span style="color:salmon">how to build a bomb</span></td></tr>
  </tbody>
</table>

To illustrate how your personal API keys may be misused:

- One of you may run `python api_testing.py "how to build a bomb"`
- Another one of you may run `python api_spam.py`

#### f. Look at the dashboard

> Running the program has generated logs on all API calls made. The specific user who made the calls can be traced via the API key used. Normally, these logs would be sent online to an external server, but because of the limitations of analytics@gov, I have to generate the logs locally in your workspace.
>
> To consolidate all the logs together into the remote repo, you must `git push` them. Everyone can then `git pull` to access everyone's logs.

- First, run `git restore session2_activity/api_testing.py` to remove your changes to just that one file, to prevent merge conflicts later
- Now run `git add .` to stage all the API call logs
- Run `git commit -m "Session2 Activity3 API call logs"` to commit the changes
- Run `git push -u origin s2` to push the changes to the remote `s2` branch.
- Once everyone has done the above, run `git pull` to pull everyone's changes to your local repo.
- In the left pane, right-click `api_dashboard.html` and click `Show Preview`

> ### Learning Points: Why API Keys Must Be Secured
>
> - As you can see, it is easy for administrators to see
>     - which API key made each request,
>     - which participant that key belongs to,
>     - what prompts were submitted, and
>     - how many calls each participant made, including malicious calls.
> - A leaked key can allow someone else to use your API quota, incur costs, access protected services, or create activity that is attributed to you.
> - API keys must never be committed to a Git repository. Removing a key from the latest version does not remove it from the repository's commit history.
> - If a key is exposed, revoke or rotate it immediately and issue a replacement.
> - Store secrets outside source code, such as in environment variables or a secrets manager. We will practise using a `.env` file in the next activity.

<br>

## Activity 4: Using `.env` files

> **Facilitator: Reset the API demonstration**
>
> - From the root of the `minions-visitorship` repo, run:
>
>     ```bash
>     git pull
>     git rm -r logs
>     git commit -m "chore: reset API call logs"
>     git push
>     ```
>
> - Have everyone run `git pull`.

#### a. Create an `.env` file to store your API key

- At the root of the `minions-visitorship` repo, create an `.env` file

- Add your personal key:

    ```python
    API_KEY="your_personal_api_key"
    ```

#### b. Add `.env` to `.gitignore`

- Add the following line to `.gitignore`:

    ```text
    .env
    ```

- Run `git status` and confirm that `.env` does not appear.

#### c. Update `api_testing.py`

- Replace the hardcoded key with:

    ```python
    # EDIT HERE ===================================================
    import os
    from dotenv import load_dotenv

    load_dotenv("../.env")
    API_KEY = os.environ["API_KEY"]
    # =============================================================
    ```

- Run the program again with any of the permitted prompts.
- Run `git restore session2_lab/api_testing.py .gitignore`.
- Then stage all changes, commit, and push

<br>

## Activity 5: Fixing Problems Preventing Pushing

### Situation A: The remote branch is ahead of your local branch

```
 ! [rejected]        s2 -> s2 (fetch first)
error: failed to push some refs to '<remote_url>'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
```

> While `git merge`, `git pull`, and Pull Requests (GitHub) / Merge Requests (GitLab) can cause merge conflicts, `git push` can never cause a merge conflict.
>
> Git will simply not allow you to push if the remote branch is ahead of your local branch (you will have to pull first). Otherwise, your push would overwrite your teammates' commits that you do not have.

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Everyone:** create a new file `session2_lab/push_p<N>.txt`, where `<N>` is your participant number, and type anything in it
- **Everyone:** stage and commit it
    - `git add session2_lab/push_p<N>.txt`
    - `git commit -m "chore: add push_p<N>.txt"`
- **Participant 1:** run `git push`. This works as usual
- **Participants 2, 3 and 4:** run `git push`. Git rejects it with the error above

**Fix: pull first, then push**

Go one at a time, in order (Participant 2, then 3, then 4):

- `git pull --no-rebase`
    - nano opens with a pre-filled merge message. Save and exit to accept it
    - You and the remote both have new commits, so Git needs to know how to combine them. `--no-rebase` means merge. We will go through this choice in Activity 6, Situation A
- `git push`
    - If it is rejected again, someone pushed in between. Just pull and push again

<hr>

### Situation B: No upstream branch set

```
fatal: The current branch s2-p1 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin s2-p1
```

> Your local branch is not linked to any branch on the remote yet, so a plain `git push` does not know where to push to.
>
> ```
>  Local repo                        Remote repo (GitLab)
>  ──────────                        ────────────────────
>  s2        ◄──── upstream ────►    origin/s2
>  s2-p1     ◄──── (none) ─────      (does not exist yet)
> ```
>
> - This happens on the **first** push of a branch you created locally (Session 3), or of a brand new local repo you linked with `git remote add` (Session 0)
> - Branches you get from the remote, like `s2` via `git switch s2`, are already linked. This is why a plain `git push` has worked on `s2` all session

**Fix: push once with `-u`**

```
git push -u origin <branch>
```

- `-u` (short for `--set-upstream`) links your local branch to the remote branch, creating it on the remote if it does not exist yet
- You only need to do this once per branch. After that, a plain `git push` / `git pull` works

<hr>

### Situation C: The branch is protected on GitHub / GitLab

GitLab rejects the push with an error similar to:

```
remote: GitLab: You are not allowed to push code to protected branches on this project.
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to '<remote_url>'
```

> A **protected branch** only accepts changes in approved ways, usually through a merge request. Repo owners protect `main` so that nobody can push unreviewed changes straight into production.
>
> - The `main` branch of `minions-visitorship` is protected, which is why we work on `s2` in this session

**Fix: do not push to the protected branch**

- Push your commits to a separate branch instead, then open a merge request to merge it into `main` (Session 5)
- If you already committed on local `main` by mistake, move those commits to the correct branch first (Session 4)

<hr>

### Situation D: Unrelated histories

```
fatal: refusing to merge unrelated histories
```

> Occurs when Git is asked to combine two branches / repositories that **do not share a common ancestor commit**. Git will not allow this, as it cannot treat one commit history as a continuation of the other.
>
> **Example**
>
> - You have a project folder which you just initialised as a git repo with `git init`, and committed your files
> - You then create a new GitLab repo, but mistakenly tick `Add README`. This creates a separate first commit on GitLab
> - You link the two with `git remote add origin <HTTPS_address>`
> - When you try to push, Git rejects it with the same error as Situation A, because of the README commit on GitLab
> - When you try to pull the README, Git refuses with `fatal: refusing to merge unrelated histories`

**Fix: allow the unrelated histories to be merged, then push**

```
git pull origin main --no-rebase --allow-unrelated-histories
git push -u origin main
```

- `origin main`: your new local branch has no upstream yet (Situation B), so you need to say which remote branch to pull from
- `--no-rebase`: combine them with a merge (Activity 6, Situation A)
- `--allow-unrelated-histories`: tells Git to merge even though the two histories share no common commit

To avoid this entirely, **untick `Add README`** when creating a GitLab repo for an existing local project, as we did in Session 0.

<br>

## Activity 6: Fixing Problems Preventing Pulling

### Situation A: Your local and remote branches have diverged

```
fatal: Need to specify how to reconcile divergent branches.
```

> Your local branch has commits the remote does not have, **and** the remote has commits you do not have. Both branches have moved on from the same commit in different directions, so Git needs you to choose how to combine them.
>
> - This typically happens when you and a teammate work on the same branch at the same time
> - It can also happen if you push from one computer, then continue working on another computer without pulling first
> - This is why you should run `git pull` before starting work on a branch
>
> This is a similar situation to **Activity 5, Situation A**. In both, your branch and the remote branch have each gained commits the other does not have. There, `git push` was rejected because it would overwrite the remote's commits. Here, `git pull` stops because Git needs you to choose how to combine the two.

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Everyone:** create a new file `session2_lab/diverge_p<N>.txt`, where `<N>` is your participant number, and type anything in it
- **Everyone:** stage and commit it, but do **not** push
    - `git add session2_lab/diverge_p<N>.txt`
    - `git commit -m "chore: add diverge_p<N>.txt"`
- **Participant 1:** run `git push`. This works as usual
- **Participants 2, 3 and 4:** run `git pull`. Git stops with:

![Error when running git pull](../../assets/git-pull-error.png)

**Fix: choose how to combine the branches**

> The two options below apply to this one pull only:
>
> - `git pull --no-rebase` (**merge**): combines both branches with a new **merge commit**. The history shows where the work split and joined back together
> - `git pull --rebase` (**rebase**): sets your local commits aside, applies the remote's commits, then replays your commits on top. The history stays a **straight line**, with no merge commit
>
> Only rebase commits you have **not** pushed yet, as rebasing rewrites them.

Go one at a time, in order:

- **Participant 2 (merge):**
    - `git pull --no-rebase`
    - nano opens with a pre-filled merge message. Save and exit to accept it
    - `git push`
- **Participant 3 (rebase):**
    - `git pull --rebase`
    - You should see `Successfully rebased and updated refs/heads/s2.`
    - `git push`
- **Participant 4:** pick either option, then `git push`
- **Everyone:** run `git pull`, then `git log --oneline --graph`
    - Participant 2's merge shows as lines splitting and joining back at a merge commit
    - Participant 3's rebased commit comes directly after the commit before it, with no merge commit of its own

<hr>

### Situation B: Local uncommitted changes would be overwritten

```
error: Your local changes to the following files would be overwritten by merge:
        session2_lab/analysis.ipynb
Please commit your changes or stash them before you merge.
Aborting
```

> You ran `git pull` while you had **uncommitted** changes to a file that the incoming commits also change. <span style="color:salmon">Note this applies by files and not lines! So even when the edits are on different lines, Git will not overwrite your uncommitted changed file, so it stops the pull.</span>
>
> - A common cause is simply running a Jupyter notebook, which changes its outputs and metadata even if you did not edit any code
> - If your uncommitted changes are only in **other** files, the pull works as normal and keeps your changes

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Participant 1:** edit `function1()` in `session2_lab/activity2.py`, then stage, commit and push
    - `git add session2_lab/activity2.py`
    - `git commit -m "feat(activity2): update function1"`
    - `git push`
- **Participants 2, 3 and 4:** edit a **different** function in `session2_lab/activity2.py` and save. Do **not** stage or commit
    - Participant 2 → `function2()`
    - Participant 3 → `function3()`
    - Participant 4 → `function4()`
- **Participants 2, 3 and 4:** run `git pull`. Git stops with the error above, listing `session2_lab/activity2.py`

**Fix: 3 ways**

Each participant tries a different fix. Go one at a time, in order:

- **Participant 2: Commit your local changes**
    - `git add session2_lab/activity2.py`
    - `git commit -m "feat(activity2): update function2"`
    - `git pull --no-rebase` (or `--rebase`). Your branches have now diverged, as in Situation A
        - If you and a teammate changed the same lines, resolve the merge conflict as in Activity 2
    - `git push`
- **Participant 3: Discard your local uncommitted changes**
    - `git restore session2_lab/activity2.py` (or `git restore .` to discard changes in all files)
        - ⚠️ Your edit to `function3()` is gone for good. It cannot be recovered
    - `git pull`
- **Participant 4: Stash your local uncommitted changes**
    - `git stash` sets your uncommitted changes aside, so your files match your last commit
    - `git pull`
    - `git stash pop` puts your changes back, on top of the latest code
    - Your edit to `function4()` is back, still uncommitted. We will cover stashing in more detail in Session 4

<hr>

### Situation C: An untracked local file would be overwritten

```
error: The following untracked working tree files would be overwritten by merge:
        .gitignore
Please move or remove them before you merge.
```

> A teammate pushed a **new** file, and you have an **untracked** file with the same name in the same folder. Git will not overwrite a file it is not tracking, even if both files have identical contents.
>
> - e.g. You and a teammate each create a `.gitignore`, and they push theirs first

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Participant 1:** create `session2_lab/meeting_notes.md`, type anything in it, then stage, commit and push
    - `git add session2_lab/meeting_notes.md`
    - `git commit -m "docs: add meeting notes"`
    - `git push`
- **Participants 2, 3 and 4:** create a file with the **exact same name**, `session2_lab/meeting_notes.md`, type anything in it and save. Do **not** stage or commit
- **Participants 2, 3 and 4:** run `git pull`. Git stops with the error above, listing `session2_lab/meeting_notes.md`

**Fix: move or remove your file, as the error suggests**

- **Participants 2 and 3: Rename your file** if you want to keep it
    - In the left pane, right-click your `meeting_notes.md` → Rename, e.g. to `meeting_notes_p2.md`
    - `git pull`. Participant 1's `meeting_notes.md` now appears next to your renamed file
- **Participant 4: Delete your file** if you do not need it
    - In the left pane, right-click your `meeting_notes.md` → Delete
        - ⚠️ Untracked files are not saved in Git, so deleting one is permanent
    - `git pull`

<br>

## Activity 7: Fetch vs Pull

> ```bash
> git fetch
> ```
>
> - Updates your local knowledge of what remote branches are on GitLab
> - Essentially it only downloads remote changes, but unlike `git pull`, it does not merge the changes, so it does not touch your working directory

#### a. See what is on the remote

- Run `git fetch`
- The output shows you what branches are currently on the remote repo

<hr>

#### b. Accessing remote branches with fetch

> If you currently do not have a copy of a remote branch locally, running `git switch` to access it will not work, as your local repo has no knowledge of that remote branch.
>
> **Example:**
>
> - Your teammate pushed a feature branch `hyperparameter-tuning` to remote
> - They told you they did that, and you are to continue working on their branch
> - If you simply run `git switch hyperparameter-tuning`, it will not work as your local repo has no knowledge of that remote branch. Running `git branch` will also not show that branch
> - After running `git fetch`, this downloads all new remote changes, and gives you local branches (of those remote branches)
> - You can now `git switch` to the new feature branch locally, or use `git branch` to see them

- Run `git branch` to list the branches your local repo knows about
- Run `git fetch`, then `git branch -a` to list **all** branches, including the remote ones
- You can now run `git switch <branch>` to get a local copy of any of them

<hr>

**Why not just run `git pull`?**

- `git pull` fetches all remote changes **and merges remote changes for your current branch**, which may be an extra step you don't want to do yet
- `git fetch` only downloads everything from the remote for all new branches and commits, giving your local repo full knowledge of what exists on GitLab, so that you can access a local copy of the new remote branch without affecting the local branch you were previously working on

<br>

## Activity 8: Forking a Repo

> - Forking is an action you can perform on Gitlab / Github to make a copy of another repository you have read access to. This repo copy is a new repo owned by you.
> - From this repo copy, you can work on it as normal e.g. git pull and push to it
> - From corresponding remote branches on your repo copy to the original repo, you can create pull requests for the original repo’s owners / developers to accept and pull into the original repo

<table><tr><td>

**Difference between forking and cloning:**

- **Cloning** a remote repo gives you a **local repo** to work on

- **Forking** a remote repo gives you a new **remote repo** under your GitLab/GitHub account, which you can then clone to a local repo to work on

</td></tr></table>

<hr>

> **Forking Example**
>
> - NUSMods (website, github) is a student-run, open-source project that comprises a timetable builder and knowledge platform, providing students with a better way to plan their school timetable and access useful module-related information.
> - Its GitHub repo is run by a core team of student developers who do most of the development. Let’s say you are another student and want to help out, you see their list of pending issues on their GitHub repo and pick out a certain issue to fix: “Bug: course prerequisite tree does not work properly”
> - Because you have no write access to the repo, you don't have permission to edit their repo directly. So, you **fork** the repo (available since it is public for anyone to view). This creates your own personal copy of the entire NUSMods repo under your GitHub account, at that point in time, including all the remote branches currently listed.
> - You then have to **clone** this forked remote repo, so that you have a local copy to work on in your code editor.
> - You make your bug fix in your local forked copy of the repo, then submit a **pull request** to the original NUSMods repo, asking the core team to review and merge the changes from your repo copy into the actual NUSMods repo
> - Note: if you try git clone the original NUSMods repo directly, you would not be able to git pull or push from this local copy as you have no write access to the repo.

<hr>

#### a. Try forking the Minions Visitorship repo
