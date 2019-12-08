# Online Snake Game

References:  
Jenkins: **34.89.51.152:8080**  
Flask: **34.76.185.11:5001**  
Pytest-coverage: **34.76.185.11:5001/coverage**  
Trello-board: **https://trello.com/b/Ek1HhDcU/individual-project-plan**  
Presentation: **https://docs.google.com/presentation/d/1FVA6l7NiQrynJE3OerSMeHe9xMafuAoekVf3a9gu3Sg/edit?usp=sharing**
<br><br><br><br><br><br><br>


# Original Project Idea
Allow a user to register then login, play a snake game which would record their score and save onto a database, and allow the user to view his scores as well as the user with the highest score.

The snake game would involve user manipulating an entity on a arena, the user would be able to collect fruits which would increase the length of the snake entity, and increase the user's score. If the snake entity hit the edge of the arena, the game would be over.

### Original ERD diagram
![ERD diagram](/images/ERD.png)
Player would have a one to many relationship with Scores.  
Account details would have a one-to-one relationship with Player.

<br>

### Original Use Case Diagram
![use case diagram](/images/UseCase2.png)

# What I got
The Use case and the functionality of the original project idea is essentially completely intact to that of what I had envisioned, however I have decided to change the database as I thought one of the tables was redundant.

### New ERD diagram
![ERD new diagram](/images/ERDnew.png)
Now there are simply two tables with Account details filling the void of what Player table was doing previously.  
Account details has a one-to-many relationship with Scores table.  

### Had to switch to websocket for game connection
During development, I used Ajax requests from the client to poll the python flask server for information on the state of the snake game. This, I later realised, proved to be flawed because if the server location happened to be too far away (e.g from Manchester to Finland), the Ajax requests would not be processed as the connections kept dropping at almost 100% of the time.  
After thinking about the issue, I realised websockets would fix my problem and should also make the interaction between client and server smoother, so I went ahead and re-did the implementation of how the client would poll the server for information. It instead now uses a communicational system wherein after establishing a session, the client asks for information and waits for the server to respond, once the server responds, the client processes the information and sends another request for newer information.  

# Testing
Testing was done using pytest and a coverage has also been supplied. Look at *References* for the link to the coverage.  
<br>
74% coverage was achieved.  
11 tests total have been created and executed; 3 of which were used to test the snake game, and the rest were used to test the website and database functionality.  
Coverage may further be increased if integration testing could be performed, such as using Selenium to test the more user-dependant functionalities such as being able to login, test the forms, test the jinja2 code, etc...  

The snake game is an interesting creation. It is a simple application, however it is multi-threaded, meaning that conventional testing schemes such as Unit testing or Integration testing may not fully apply due to the nature of parallel systems. Ideally you would use a test package suited for multi-threaded testing, such as some sort of spec=flow analysis which would calculate all possible states each of the threads could be in to see whether a deadlock or a livelock has occured.  
However, I have still included some minor tests for the snake game specifically by creating an instance of it and simply waiting to see what would happen. In theory, after a certain amount of time, the snake would hit the outer edges of the arena, thereby changing the game state variable which I would then be able to test.

# Deployment Overview
![techs used](/images/tech.png)
Made a webserver application using Python, MySQL, and Flask. Used git and github for version control whilst using Trello to organise myself. Github would submit requests to Jenkins to update, test using pytest, and redeploy the application. Finally, the cloud provide, GCP, was used to host the application.  

Technologies used:  
Python/Mysql/Flask  
Git/Github  
Trello  
Jenkins  
Pytest  
GCP  

# The Future
Many things could be improved. For example, I am not really sure how multi-threading is done under the hood in Python, so whether my snake game is thread safe is unknown at this point, so more research would definitely help. In terms of looks, the website looks pretty barebones, perhaps integrating a front-end View framework such as Bootstrap would be a good idea.  
Further expanding the game would be interesting, such as adding multi-player functionality wherein two snakes would be in the same arena, and the one that hits the others' tail loses.  
<br>
For the snake game, the implementation of how it is streamed to the client is a bit cumbersome, currently the client asks for the entire grid information every request. I believe the best solution to this problem would be to implement the actual game on the client-side, and then simply hash the snake game source code and send it to the server every half a minute or so, the server would then verify the hash and if there was a difference, the score would not be submitted when the player finished playing. This would drastically reduce the load on the server, and make the game much smoother to play.
