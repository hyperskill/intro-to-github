# intro-to-github
This is a demo repository to practice using GitHub.

It has two files in the **Code** tab:
- **README.md** is a file that describes this repo (you are currently reading it)
- **.gitignore** is a file that specifies which files and directories must be ignored by Git

You cannot directly modify files in this repo because you are not a *collaborator*.

The **Issues** tab is used to discuss ideas, enhancements, bugs, questions, and so on. They are grouped by *Open* and *Closed*.

The **Pull requests** tab contains proposals to make some changes in the files located in the repository. Repo's owners may review a request and put your changes if they look good.

You can create an *Issue* or make a *Pull request (PR)* to contribute to the project.

If you want to propose some changes to this repo, you may *fork* it, modify the content, and create *PR*. A *fork* is just a copy that allows you to change the content without affection the original project.

Branching
Before we start making changes to the content of the repo, we need to learn an important concept called branching. It provides a way to work on different versions of a repository at the same time.

By default, any repository has a branch named master that represents the actual version of a project. If you want to change some content in a repo, first, you need to create a new branch based on master to get an isolated snapshot of the project. Usually, a branch represents a feature or a fix that is developed now. It allows you to protect master from possible unwanted changes and to roll back. You can also create a new branch based on another branch (non-master) that is active.

Branching especially helps organize team development processes. Several programmers work on different features at the same time, each in their own branch. After the job is done, the code is merged together.

Now it may be not so easy for you to understand branching, just follow our recommendation and use special branches rather than working on the master directly. If you want to read more about branches, check out a short article written by GitHub.
