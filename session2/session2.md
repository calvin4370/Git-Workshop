# Session 2: Remote Workflows
> In Session 1, you cloned a brand new, empty repo you created yourself on GitLab
>
> This time, we will clone a repo that already has files and a commit history, just like joining an ongoing project.


## Setup
>`Minions Visitorship` is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

#### a. Clone the `Minions Visitorship` repo
- Navigate to your home directory using `cd ~`
- Run `git clone https://gitlab.analytics.gov.sg/gcc_jun_jie_chan_from.tp/minions-visitorship.git`
- Navigate into the project folder using `cd minions-visitorship`


#### b. Switch to a different branch
- Run `git switch -c s2` to switch to the `s2` branch of the repo
- This is to prevent you from pushing changes to modify my clean `main` branch (I have also configured the GitLab repo to not accept direct pushes to main).
- Branching will be gone through in detail in the next session


<br>


## Activity 1: Pushing and Pulling Changes


<br>


## Activity 2: Conflict Resolution


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
> 

### Situation B: 
> 


<br>


## Activity 5: Fixing Problems Preventing Pulling


<br>


## Activity 5: Fetch vs Pull


<br>


## Activity 6: Forking a Repo