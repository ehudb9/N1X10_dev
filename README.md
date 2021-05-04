# N1X10_dev

# N1X10 - Document analyze

![Image of BUD](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpYY9MPXT0EkmuJi3_Zdxt7LjHDgwLmLrY1Q&usqp=CAU)



This project get a pattient documet as an input.
And returns EXELE table with the relevant data for N1X10 system.

* Configuration - the abillity to change settings such as robot ip, game model, letter slates, and so on.
* Gestures & Animations - the abillity to instantly play animations that were deployed to the robot using "Butter API"
* Play Game Models - initiate any of the existing 'game models' to conduct experiments.
* Derive Data - collect data that was gathered during the experiment, for later analysis.

## Getting Started

These instructions will represent the flow of the project.

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
* Make sure you are connected to the "milab_idc" wifi network.
* run the file 'app.py'
* click on the link that appears in the terminal and looks like:
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Your default browser should pop up the interface !

### What Now?

Now you are ready to go. Read the overview page thoroughly and then start using the app.
If you want to stop the server, go to the VS porject and press 'control + C'.

## Built With

* [flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Butter](https://bennymeg.github.io/Butter.MAS.PythonAPI/) - Robot Prototyping Platform

## Authors

* **Ron Gissin** - *Initial work* - (https://github.com/RonGissin)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
