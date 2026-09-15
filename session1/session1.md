# Session 1: Local Workflows

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


## Activity 1: Initialise a git repo on Gitlab and clone it locally
>Setup
>- This session continues straight from Session 0
>- You may reuse the GitLab repo you created in the previous session, or making one again

#### a. Go to GitLab and create a new GitLab repository
- You can name it whatever you want e.g. `Local Git Practice`
- GitLab will give it a machine-readable slug e.g. `Local-Git-Practice`
- You can just create it under your own GitLab account. No need to put it in the SPDM group.
- Now you can tick `Add README` and add a license if you want

#### b. Clone the remote repo locally
- In the repo page, copy the HTTPS address again
- In your terminal, ensure you are in the home directory. If not, navigate there using `cd ~`
- Run `git clone <HTTPS_address>` from the home directory

#### c. You now have a local copy of the remote repo you created on GitLab
- The repo will be initalised locally as a folder in your home directory e.g. named `Local-Git-Practice`
- Navigate into this folder
- Running `ls -a` should show the `.git` hidden folder
- You can also run `git status` to verify the current folder is a git repo


<br>


## Activity 2: Staging and Commiting Changes


<br>


## Activity 3: Writing Multi-line Commits

>- Note: We will go through conventions for writing commit messages in Session 6: Team Workflow Standards


<br>


## Activity 4: Other useful commands and arguments for local workflows


<br>


## Activity 5: Using the VSCode IDE for a more user-friendly UI
### Staging and Unstaging Changes


### Committing Changes


<br>


## Activity 6: Interaction with Jupyter Notebooks


<br>


## Activity 7: Writing .gitignore


#### What if the file you want to gitignore has already been pushed?