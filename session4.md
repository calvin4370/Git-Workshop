# Session 4: Safe Undo of Code Changes

### Overview
> **Required**:
> - `Minions Visitorship` repository on GitLab

`Minions Visitorship` is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

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
      <td><code>git restore --staged &lt;file&gt;</code><br><code>git restore --staged .</code></td>
      <td>Unstage a specific file (keep changes)<br>Unstage all files</td>
    </tr>
    <tr>
      <td><code>git restore &lt;file&gt;</code><br><strong><code>git restore .</code></strong></td>
      <td>Discard changes in a specific file<br><strong>Discard all changes in working directory</strong></td>
    </tr>
    <tr>
      <td><code>git reset --soft HEAD~1</code></td>
      <td>Undo last commit (keep changes staged) *</td>
    </tr>
    <tr>
      <td><code>git reset --mixed HEAD~1</code></td>
      <td>Undo last commit (keep changes unstaged) *</td>
    </tr>
    <tr>
      <td><code>git switch --detach &lt;hash&gt;</code></td>
      <td>View the state of the repo at a previous commit</td>
    </tr>
    <tr>
      <td><strong><code>git revert &lt;hash&gt;</code></strong></td>
      <td>Revert a pushed commit by adding a new commit that inverses it — safe on shared branches since history isn't rewritten</td>
    </tr>
  </tbody>
</table>


<br>

<aside>

**Background info:**

- **Untracked** files are files that have never been staged to Git (`git add`), such as a new file or new pipeline outputs.
    - Git doesn't track their changes, and `git restore` ignores them.
    - Once you stage a new file, they become **tracked** by Git
- **Staged** files are changes you've marked with `git add` to go into your next commit. They're held in the *staging area* until you commit them
- **Unstaged changes** are edits to tracked files that you have not staged yet. They exist only in your working directory.
- **Committed changes** are saved permanently in the repo's history as a snapshot.
- **Pushed changes** are commits uploaded to a remote repo such as one hosted on GitHub, where other people can pull them.
</aside>



<br>


## Activity 1: Viewing the State of the Repo at a Particular Commit

#### a. Switch to the main branch of your local repo
- Run `git branch` to list out the branches on your local repo
- Run `git switch main` to switch to the main branch

#### b. View the State of the Repo at a Particular Commit
- Open the list of commits using `git log --oneline`

```python
git checkout <hash>
```

- This moves HEAD to that commit and updates your working directory to that snapshot. This is useful for quickly inspecting an old version of your project. 
- You land in a **detached HEAD** state (where HEAD points at a commit instead of a branch, so any new commits you make here aren't on any branch). 
- To leave and go back, run `git switch -`


<br>


## Activity 2: Discarding all commits after a particular commit


<br>


## Activity 3: Reverting ONE commit

#### a. Open the list of commits


#### b. Revert the commit `"TODO"`

```python
git revert <hash>
```

- This creates a new commit that cancels out the changes made in the original commit
- Use the flag `--no-edit` to skip the commit-message editor


#### c. Revert the revert


<br>


## Activity 4: Reverting the last commit without deleting your changes

#### a. Make a minor change to `"TODO"`

#### b. Stage the change

#### c. Commit the change with a message

#### d. Revert the last commit but **KEEP the changes staged**

#### e. Repeat parts b. to c. to commit the change again

#### f. Revert the last commit but KEEP the changes unstaged

<hr>

Note: In this activity, we explored 2 ways to revert the last commit, but retain the changes in our working directory. The difference between this and Activity 4 is that the changes were reverted without leaving them in your working directory


<br>


## Activity 5: Discard uncommited changes in your working directory