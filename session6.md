# Session 6: Merge Requests and Code Review

As we learnt from Session 3 on Branching, we do not commit our changes straight to `main` to prevent any bad changes from making it straight into production.

Instead, we work on feature branches, until we finish a feature or set of specific changes. Once we are happy with it, we will merge our feature branch into main to merge in our changes.

The workflow for doing this is as follows:

1. We create a feature branch off main, say `pipeline/add-models`
2. We work on our changes in the branch, staging and committing changes locally as we go
    - By commiting changes, they are tracked locally in your local git repo
    - Your teammates cannot see them yet, as all they can see is their own local repo, and the remote repo on GitLab
3. Once we are done (or any time in between commits), we can push our commits to remote
    - This pushes the feature branch to the remote repo on GitLab where everyone in the team can see the code
    - They can now see the changes on the web, or even pull the branch to work on the code locally
4. To merge the feature branch into main (or any other branch), we initiate a merge review on GitLab from our browser.
5. A reviewer, typically someone else on the team, will go through the changes in the feature branch
    - They can leave comments, approve or disapprove the merge request
    - If the merge request is approved, the feature branch's changes can be merged into main
    - This updates the main branch remotely, and other team members need to pull the main branch to get the changes locally.


<br>


## Activity 1: 