## Description
The Git workshop is organised into 7 (or 8?) sessions, each taking up to 1 hour.

The sessions are designed to build off from the previous one and should be done sequentially. 

The sessions should be done as close to one another as possible such that participants do not completely forget what was gone through previously.


## Sessions
- Session 1: Intro to Git Basics and GitLab Setup
- Session 2: Local Workflows
- Session 3: Remote Workflows
- Session 4: Branching
- Session 5: Safe Undo of Code Changes
- Session 6: Merge Requests and Code Review
- Session 7: Team Workflow Standards
- Session 8: Reinforcement Lab?

For each session, participants will access this repo to read the session materials (e.g. `session1.md`). Some sessions may require them to access a separate repo concurrently, to practice git commands (e.g. `git clone`).


## Content
Each session's content was derived from my [Git Summary Notes](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link) on Notion. I group related activities into each session.


## Datasets and materials
`Minions Visitorship` repo
- This is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.
- `minions.csv` contains transaction-level data on visitorship to NHB's museums by the minions
    - It was originally generated using Mirage
    - I then used Python to make hourly transactions follow a more natural distribution throughout the day (Mirage only generates uniform distribution)
- `analysis.ipynb` contains plots and analyses based on the minion visitorship data