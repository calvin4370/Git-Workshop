# Session 2: Remote Workflows and Conflict Resolution
> In Session 1, you cloned a brand new, empty repo you created yourself on GitLab
>
> This time, we will clone a repo that already has files and a commit history, just like joining an ongoing project.


## Setup
>`Minions Visitorship` is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

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

<br>


## Activity 1: Pushing and Pulling Changes
> Repo: `minions-visitorship`
> Branch: `s2`

> We will demonstrate pushing and pulling with 4 participants. Each person will push changes to the repo, and pull the updated state of the repo

#### a. Participant 1 pushes their changes
- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- You should see:
  ![Output of git pull](../../assets/already.png)
- Open the Jupyter notebook at `minions-visitorship/session2-lab/analysis.ipynb`
- Find the cell under **Config** with the code `YEAR = 2024`
  - Edit the code into `YEAR = 2025`
  - Rerun the notebook to regenerate the plot outputs for 2025
- Stage, commit and push your changes to remote
  - `git add .`
  - `git commit -m "analysis: rerun notebooks for 2025 data"`
  - `git push`

> Everyone should now run `git pull` to pull the changes.
> 
> Your working directories should now all reflect the updated codebase



<br>


## Activity 2: Conflict Resolution
> `git pull` is `git fetch` then `git merge`. It fetches the commits on the remote branch, then merges the equivalent **remote branch** into your **local branch**.
>
> A merge happens whenever two lines of development need to be combined: when you run `git pull`, when you accept a MR on GitLab, or when you run `git merge` directly. Most of the time, Git combines them automatically. As long as you and your teammate changed **different files**, or **different parts of the same file**, Git can tell which change belongs where, and it merges them into a new commit automatically.
>
> A **merge conflict** happens when two branches changed the **same part of the same file**, and Git cannot tell which version should be kept. Git will not guess. It stops the merge, marks the conflicting lines in the affected file(s), and leaves it to you to decide what the final version should look like (Conflict Resolution).

<br>


## Activity 3: Working with .env files
> Other than rebuildable outputs, large binaries, and clutter which should not be committed for various reasons, there are some environmental variables / files required by your code but still should never be committed to Git.
>
> What to NEVER commit to your Git repositories:
>- API keys / tokens
>- Passwords
>- Sensitive personal identifying information (PII)
>
>These should be stored locally on each user's devices or on a secure tool.
>
>If you have pushed your secrets to Gitlab
>- If the repo is publicly viewable, bots that scrape open Github / Gitlab repositories for secrets 24/7 will eventually find it and misappropriate your API accounts
>- If the repo is private, it's still irresponsible to push your personal API keys, as anyone who has viewing access to your repo can misappropriate them, or the repo may be made public one day
>
>Undoing code changes, including commits and pushes, is covered in **Session 4: Safe Undo of Code Changes**

<table><tr><td>

**Working Example: MAESTRO LLM API**

- To simulate the generation of your personal LLM API key, I will send each of you your API key individually on Teams.
- Copy and paste it into the relevant code section when prompted

</td></tr></table>

#### a. Navigate into the `minions-visitorship/session2_activity` folder
- While in `/home/jovyan/minions-visitorship`, run `cd session2_activity`

#### b. Try running the program which calls an LLM API
> Note: This is a simulated LLM API, with hardcoded prompts and responses. But I have implementing tracking of users and their prompts, and a dashboard that shows all LLM call logs.
- Run `python api_testing.py "<prompt>"` where \<prompt\> is anything you want to ask an LLM
    - e.g. `python api_testing "what is the weather today"`

- You will see that, as most APIs do, this LLM API requires an API key


#### c. Open the `api_testing.py` file
- You may want to keep this `session2.md` open, and have `api_testing.py` open in split screen

#### d. Copy and paste your personal API key into `api_testing.py`
- You should replace line {edit-here} with your API key
- e.g. `API_KEY = JJ11M26N1H2B3LV4EVR`

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



<br>


## Activity 4: Fixing Problems Preventing Pushing

### Situation A: 
> While `git merge`, `git pull`, and Pull Requests (GitHub) / Merge Requests (GitLab) can cause merge conflicts, `git push` can never cause a merge conflict. 
> 
> Git will simply not allow you to push if the remote branch is ahead of your local branch (you will have to pull first).

### Situation B: 
> 


<br>


## Activity 5: Fixing Problems Preventing Pulling

### Situation A: When your local and remote branches have diverged
> - This typically happens when you're working on a branch at the same time as or after a teammate working on the same branch.
> - It could also happen if you were working on the branch on one computer, push changes, then switch to another computer and continue working without first pulling the changes. (this is essentially the same situation as the one with different teammates)
> - This is why running `git pull` before starting on a branch is a good habit to ensure you are working on the latest state of the codebase

![Error when running git pull](../../assets/git-pull-error.png)

- Show the Git graph where local and remote branches have diverged from one point

### Situation B: 
<br>


## Activity 5: Fetch vs Pull


<br>


## Activity 6: Forking a Repo
>- Forking is an action you can perform on Gitlab / Github to make a copy of another repository you have read access to. This repo copy is a new repo owned by you.
>- From this repo copy, you can work on it as normal e.g. git pull and push to it
>- From corresponding remote branches on your repo copy to the original repo, you can create pull requests for the original repo’s owners / developers to accept and pull into the original repo

<table><tr><td>

**Difference between forking and cloning:**

- **Cloning** a remote repo gives you a **local repo** to work on

- **Forking** a remote repo gives you a new **remote repo** under your GitLab/GitHub account, which you can then clone to a local repo to work on

</td></tr></table>

<hr>

> 
>**Forking Example**
>
>- NUSMods (website, github) is a student-run, open-source project that comprises a timetable builder and knowledge platform, providing students with a better way to plan their school timetable and access useful module-related information.
>- Its GitHub repo is run by a core team of student developers who do most of the development. Let’s say you are another student and want to help out, you see their list of pending issues on their GitHub repo and pick out a certain issue to fix: “Bug: course prerequisite tree does not work properly”
>- Because you have no write access to the repo, you don't have permission to edit their repo directly. So, you **fork** the repo (available since it is public for anyone to view). This creates your own personal copy of the entire NUSMods repo under your GitHub account, at that point in time, including all the remote branches currently listed.
>- You then have to **clone** this forked remote repo, so that you have a local copy to work on in your code editor.
>- You make your bug fix in your local forked copy of the repo, then submit a **pull request** to the original NUSMods repo, asking the core team to review and merge the changes from your repo copy into the actual NUSMods repo
>- Note: if you try git clone the original NUSMods repo directly, you would not be able to git pull or push from this local copy as you have no write access to the repo.

<hr>

