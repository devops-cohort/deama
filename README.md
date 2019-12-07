# Online Snake Game

Jenkins: **34.89.51.152:8080**  
Flask: **34.76.185.11:5001**  
Pytest-coverage: **34.76.185.11:5001/coverage**
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


# What I got
the Use case and the functionality of the original project idea is essentially completely intact, however I have decided to change the database as I thought one of the tables was redundant.

## New ERD diagram
![ERD new diagram](/images/ERDnew.png)

