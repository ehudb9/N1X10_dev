# N1X10_dev
<p align="center">
    <img src="https://github.com/ehudb9/N1X10_dev/blob/main/assents/logo.png" alt="Logo" width="400" height="300">
</p>


Document Analyze :
This project get a pattient documet as an input.
And returns ExceL table with the relevant data for N1X10 system.

<br />
<p align="center">
    <h3 align="center">Project-Flow</h3>
</p>
<p align="center">
    <img src="https://github.com/ehudb9/N1X10_dev/blob/main/assents/flow.png" alt="Logo" width="600" height="500">
</p>
<br />

### The Flow Details:
<br />

*'will be update with the progect progress.*

1. **Pull from remote develop branch**
   1. Checkout to develop\
      `git checkout develop`
   1. Then type\
      `git pull origin develop`\
      In order for your local develop branch to be in sync with remote.
      
1. **Create a private branch**
   1. In order to branch out from develop, make sure you are currently on the develop branch,
   1. And then type the following\
       `git checkout -b <private_branch_name>`\
       This will create the new branch and checkout to it !
       
1. **Merge develop into your development branch**
   1. Type:\
      `git merge develop`\
      This will update any changes that other team members made, with your local branch. If there are conflicts, resolve them !
                 
1. **Work on your private branch**
   1. Continue working on your private branch until you are done with your assignment.\
      This includes adding files (staging) and committing locally, as well as pushing occasionally to the remote branch.\
      Make sure you are pushing to a remote branch with the same name as your private branch.. To make sure use -\ 
      `git push origin <branch_name>`


1. **Once done with task - Create a Pull Request to Develop**
   1. Make sure you pushed all your changes to your remote branch.
   1. Then, go to GitHub and create a pull request from your branch to develop.
   1. Assign the relevant reviewers to your PR, and wait for Code Reviews.
   1. Handle all rejects until the PR is approved, and finally complete the PR!
   
   *Now that you have done so, your changes are present in develop !*



1. **(*Project Owner Only*) Merge Develop to Master**
   1. Test the code on develop.
   2. Merge develop into master so that the changes of your team can be `in production`. 

<br /> 

### Clone the project

The first thing you'll want to do, is 'git clone' this project.
Create an appropriate folder in your local machine, 
Then enter Git Bash (or any other Linux terminal)
and type:
```
git clone <clone url>
```

the "clone url" can be found on the the top right part of this github page.

### Prerequisites
****TBC****

The prerequisites are listed in the "requirements.txt" file.
Make sure you have a working virtual environment with all the packages downloaded in it.
If you want to make a new virtual environment, create it and make sure you run
```
pip install requirements.txt
```
when inside your venv.

### Running the app

To run the app, I recommend using VS Code.
Follow these steps:
* Open the project you've cloned in VS Code.
****TBC****

### What Now?

****TBC****

## Built With
****TBC****
* [flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Butter](https://bennymeg.github.io/Butter.MAS.PythonAPI/) - Robot Prototyping Platform

## Authors
## ****TBC****
