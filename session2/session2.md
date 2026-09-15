# Session 2: Remote Workflows

### Setup


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

If you have pushed your secrets to Gitlab
- If the repo is publicly viewable, bots that scrape open Github / Gitlab repositories for secrets 24/7 will eventually find it and misappropriate your API accounts
- If the repo is private, it's still irresponsible to push your personal API keys, as anyone who has viewing access to your repo can misappropriate them, or the repo may be made public one day

Undoing code changes, including commits and pushes, is covered in **Session 4: Safe Undo of Code Changes**


Example: MAESTRO LLM API

To simulate the generation of your personal LLM API key, I will send each of you your API key individually on Teams.

Choose from the pre-written API prompts below. Copy and paste the prompt verbatim into the `llm_api` call.

what is the weather today
how to use git
why is git so hard
what is the best bubble tea brand in singapore
when i sneeze, why does it sometimes hurt my tummy
how to build a bomb



<br>


## Activity 4: Fixing Problems Preventing Pushing


<br>


## Activity 5: Fixing Problems Preventing Pulling


<br>


## Activity 5: Fetch vs Pull


<br>


## Activity 6: Forking a Repo