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

<b>Change the following values before running the program:</b>

The default username and password for the mySQL database is given as root. If this is not your username or password input the new user and pass on lines <b> 497,502,523 and 551</b>.

The path for the background is currently <b>C:/CET/BackGround.png</b>, this can be changed on line <b> 445 </b>.

<h2> IMAGES </h2>
<h4> Starting Window </h4>

![1](https://user-images.githubusercontent.com/74500069/180897293-7aadc5ca-d9eb-4082-aeb6-edd0399eb233.png)

<br>
<h4> Selecting an Option </h4>

![6](https://user-images.githubusercontent.com/74500069/180897547-bdad455c-636b-43f4-93c6-5ab857aa5aa7.png)

<h4> Graph </h4>


![7](https://user-images.githubusercontent.com/74500069/180897576-b8c3e7ba-02d8-416b-bce1-cea04bb3e81e.png)


<h4> Country List </h4>

![8](https://user-images.githubusercontent.com/74500069/180897605-bd56ff5e-d237-47c6-b971-fb6963067fb1.png)



<h2>SOURCES</h2>
The CSV file used for providing the carbon emission values was obtained from Our World in Data(https://www.ourworldindata.org/)







