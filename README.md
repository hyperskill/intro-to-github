Before we start making changes to the content of the repo, we need to learn an important concept called branching. It provides a way to work on different versions of a repository at the same time.

By default, any repository has a branch called main that represents the actual version of a project. If you want to change some content in a repo, first, you need to create a new branch based on main to get an isolated snapshot of the project. Usually, a branch represents a feature or a fix that is being developed at the moment. It allows you to protect main from possible unwanted changes and to make a rollback. You can also create a new branch based on another branch (non-main) that is active.

Branching especially helps organize team development processes. Several programmers work on different features at the same time, each in their own branch. After the job is done, the code is merged together.

Now it may not be easy for you to understand branching, so just follow our recommendation and use special branches rather than work on the main directly. If you want to read more about branches, check out a short article written by GitHub.
