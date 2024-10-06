# Tokio Marine
## API test

### Flask API application served in AWS instance

### Characteristics
- Flask API web application
- AWS EC2 Linux server
- PostgresQL database (SQlite3 locally for development)

*IMPORTANT: Adjust `python` commands to `python3` if necessary*

# Development setup
## Requirements
### Install in your computer (if not already installed)
- pyhon >= 3.9 https://www.python.org/downloads/
- Docker https://docs.docker.com/engine/install/
- Git https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Clone repository and setup local environment
- clone repository `git clone https://github.com/GuiFV/tm-test`
- create .env file on root directory and insert `DATABASE_URL=sqlite:///database.db` on top of file
- Optional: open project on your IDE of choice (VSCode, Pycharm, etc.)

## Run application
on project folder (main folder):

- create virtual environment with python `python -m venv .venv`
- activate .venv `.\.venv\Scripts\activate` (for mac/linux: `source .venv/bin/activate`)
- upgrade pip `python -m pip install --upgrade pip`
- install dependencies `pip install -r requirements.txt`
- run tests `python -m unittest`
- run application `python app.py`
- go to http://127.0.0.1:5000 on your browser to access the application

# Development

## Before development
- activate .venv on terminal `.\.venv\Scripts\activate` (on mac or linux: `python -m venv .venv`)
- go to main branch `git checkout main`
- pull updated codebase `git pull`
- verify branch and changes `git status`
- run tests `python -m unittest`
- checkout into working branch `git checkout branch_name` or create and checkout into new one `git checkout -b new_branch`

## After development
- create / update tests
- insert new installed libraries into requirements.txt manually (don't use pip freeze)
- verify branch and changes `git status`
- update .gitignore if necessary
- update README.md and CHANGELOG.md if necessary
- merge current main branch into working branch `git pull origin main`
- fix git merge conflicts
- verify what will be commited `git status`
- stage changes `git add .`
- verify changes `git status`
- commit changes `git commit -m "short description of changes made"`
- verify commit `git status`
- push branch `git push` (if this is a new branch, `git push –set-upstream origin new_branch`)
- open a pull request
- delete branch once merged with main

# Server operation

## Locally
- copy provided .pem file to .ssh folder (optional)
- run `chmod 400 file-name.pem` on file directory
- open terminal and run provided SSH command (similar to `ssh -i ~/.ssh/file-name.pem ec2-user@ip`)
- *IMPORTANT* if .pem file not in .ssh folder, change the path to `~/folder-where-pem-file-is/file-name.pem`
- type 'yes' and hit Enter

## Once on server
- run `./up-and-run.sh`
this script will start docker, pull new codebase form main and start application

## Server maintenance
- run `./down-and-update.sh`
this script will shut application down, run server basic updates, clear docker images and reboot

- run `./up-and-run.sh` after reboot

