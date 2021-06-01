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

1. **Init**
   1. get a medical document.
       `assume pdf file` 
   1. check if the document is readable or scanner picture send the file to OCR.
      
      
2.1. **OCR**
   * In order to extract the text will transform the file to JPG and then to .txt file
   * returns txt file 

2.2. **pdf object**
   * init python pdf object in order to work on the file


3. **Document classification**
   1. gets txt file from OCR or pdf object.
   2.  *TBC* unbundle the file
   3.  returns a list of each document's attribute:
<p >
<ul>
  <li>name of patient</li>
  <li>date of document</li>
  <li>date of procedure</li>
  <li>doctor’s name</li>
  <li>the department </li>
  <li>the institution</li>
    <li>type of procedure</li>
  <li>num of pages </li>
  <li>reference to the original document</li>
</ul>
</p>

4.1 **imaging**

  * TBC


4.2 **Bood test**
  * TBC
   
4.3 **Dr summaries**

  * TBC
4.4 **Medication prescriptions**

  * TBC

4.5 **Pathology**

  * TBC

4.6 **Surgery reports**

  * TBC

4.7 **Hospital release forms**

  * TBC

4.8 **Genomic-molecular profiles**

  * TBC

5 **Assemble the results to excel**

  * TBC



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
