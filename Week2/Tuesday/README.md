# Getting Started with Git and Github
 
## Official Documentations
- [git](https://git-scm.com/doc) 
- [Github](https://docs.github.com/en)

## Git

1. Installation
    - https://git-scm.com/downloads
    ```
    git --version
    ```
2. Configuration and help
```
git config --global user.name "an-awesome-pic16b-student"
git config --global user.email "an-awesome-pic16b-student@ucla.edu"
```
```
git help
git <command> help
```
3. Initializaion
```
git init
```
4. Check status
```
git status
```
5. Adding files for staging
```
git add file.py
git add .
```
6. The `.gitignore` file
```
touch .gitignore
```
7. Commit files
```
git commit -m "This is a commit message"
```
8. View commit logs
```
git log
```
9. Checking branch
```
git branch
```
10. Creating a branch
```
git branch <branch_name>
```
11. Checking out branches
```
git checkout <branch_name>
```
12. Merge branches
```
git merge <branch_name>
```

## Github
### git local vs remote
Local repositories are on your PC, accessible only by you. 
Remote repositories are hosted on a server that is accessible by *all*.
One such server provider is Github


1. Create an account
    - https://github.com/
2. Create remote repository
    - https://github.com/new
3. Add remote
```
git remote add <remote-name> <remote-url>
```
4. Push to github
```
git push <remote-name> <branch-name>
```
5. Pull other people's changes
```
git pull <remote-name> <branch-name>
```
6. Clone someone's repo
```
git clone <remote-url>
```