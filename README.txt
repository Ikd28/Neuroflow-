If this assesment were to be a production application,there will 
be more users so I will create a reliable database to store the data.
POST calls will write data to the database and GET calls will read data
from the database.
Also there will be two collections in the database(Users and moods).
If there are more users there's a high probability in the recurrence 
of the names so for the User collection I will have two entries,Username and ID.
For each entry there will be two fields and each user ID will be unique for each person.

Also, for the mood collection you will have separate user id's for each name
and for each entry of the mood will have date and time, the text for the mood, and the streak.

In this project, I presented two main separate codes, one named as API PART 1 and the other as PART2.
the Part1 which is the first part of the REST API contains GET, POST, and '/mood' endpoints respectively.
The GET and the POST methods for this particular code can be tested using (http://localhost:3000/getmood or http://localhost:3000/postmood).
For the Part2 of my code, I linked the GET and POST methods to a simple database to serve the purpose of the user logins. 
I have added the various requirements needed for this code to run too.

 






