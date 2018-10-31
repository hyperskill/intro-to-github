# intro-to-github
This is a demo repository to practice using GitHub.

It has two files in the **Code** tab:
- **README.md** is a file that describes this repo (you are currently reading it)
- **.gitignore** is a file that specifies which files and directories must be ignored by Git

You cannot directly modify files in this repo because you are not a *collaborator*.

The **Issues** tab is used to discuss ideas, enhancements, bugs, questions, and so on. They are grouped by *Open* and *Closed*.

The **Pull requests** tab contains proposals to make some changes in the files located in the repository. Repo's owners may review a request and put your changes if they look good.

You can create an *Issue* or make a *Pull request (PR)* to contribute to the project.

If you want to propose some changes to this repo, you may *fork* it, modify the content, and create *PR*.
A *fork* is just a copy that allows you to change the content without affection the original project.
Navigate to the directory of the repository and look at the content. The local repo includes all of the files, branches and commits history like the remote repository. Type the special command to verify the state of your repo:

git status

Now your working copy is actually on the master branch of your local repo. And it does not have differences with the origin (fork) master branch.

On branch master
Your branch is up-to-date with 'origin/master'.

To make changes in your repo, first, you will create a branch to protect your master branch. Type the command below:

git branch edit-readme

After the command is executed, the branch exists, a new branch will be created, but you are still on master. You may check it using status as above.

To get another branch, use checkout with the branch name:

git checkout edit-readme

Now you are on the created branch.

git status

The result:

On branch edit-readme
nothing to commit, working tree clean