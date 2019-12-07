# Online Snake Game

References:  
Jenkins: **34.89.51.152:8080**  
Flask: **34.76.185.11:5001**  
Pytest-coverage: **34.76.185.11:5001/coverage**  
Trello-board: **https://trello.com/b/Ek1HhDcU/individual-project-plan**  
<br><br><br><br><br><br><br><br>


# Original Project Idea
Allow a user to register then login, play a snake game which would record their score and save onto a database, and allow the user to view his scores as well as the user with the highest score.

The snake game would involve user manipulating an entity on a arena, the user would be able to collect fruits which would increase the length of the snake entity, and increase the user's score. If the snake entity hit the edge of the arena, the game would be over.

## Original ERD diagram
![ERD diagram](/images/ERD.png)
Player would have a one to many relationship with Scores.  
Account details would have a one-to-one relationship with Player.

<br>

## Original Use Case Diagram
![use case diagram](/images/UseCase.png)

## Trello Board
![trello board](/images/trello.png)


# What I got
The Use case and the functionality of the original project idea is essentially completely intact to that of what I had envisioned, however I have decided to change the database as I thought one of the tables was redundant.

## New ERD diagram
![ERD new diagram](/images/ERDnew.png)
Now there are simply two tables with Account details filling the void of what Player table was doing previously.  
Account details has a one-to-many relationship with Scores table.

# Testing
Testing was done using pytest and a coverage has also been supplied. Look at *References* for the link to the coverage.  
<br>
74% coverage was achieved.  
11 tests total have been created and executed; 3 of which were used to test the snake game, and the rest were used to test the website and database functionality.  
Coverage may further be increased if integration testing could be performed, such as using Selenium to test the more user-dependant functionalities such as being able to login, test the forms, test the jinja2 code, etc...  

The snake game is an interesting creation. It is a simple application, however it is multi-threaded, meaning that conventional testing schemes such as Unit testing or Integration testing may not fully apply due to the nature of parallel systems. Ideally you would use a test package suited for multi-threaded testing, such as some sort of spec=flow analysis which would calculate all possible states each of the threads could be in to see whether a deadlock or a livelock has occured.  

# Deployment Overview
![techs used](/images/tech.png)
Technologies used:  
Python/Mysql  
Git/Github  
Trello  
Jenkins  
Pytest  
GCP  


