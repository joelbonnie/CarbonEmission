<h1> Carbon Emission Tracker </h1>

The main aim of this program is to create a visual representation of the different Carbon emission sources and to compare the carbon emission of various countries.

First, an SQL database is created using a CSV file for the information. After extracting and importing values once, it needn’t be done again. 

Using the graphical interface, the user can specify whether to compare the carbon emissions of two specific countries, that of a particular country and the global average, or the various sources of a given country. The user can also select the option of a country list to show which countries are supported. 

Using bar graphs, a visual representation of this information is given to the user. This created graph can be saved for further use or for comparison.  

<h2> REQUIREMENTS AND INSTRUCTIONS </h2>
This program requires Python 3 and mySQL. 
It uses the following modules which can be obtained through pip <i>(pip install [module])</i>

- mysql.connector
- tkinter
- matplotlib

First extract the zip file to a folder and change the following values before running the program.

The default username and password for the mySQL database is given as root. If this is not your username or password input the new user and pass on lines <b> 497,502,523 and 551</b>.

The path for the background is currently <b>C:/CET/BackGround.png</b>, this can be changed on line <b> 445 </b>.

<h2> Images </h2>

<h2>SOURCES</h2>
The CSV file used for providing the carbon emission values was obtained from Our World in Data(https://www.ourworldindata.org/)

