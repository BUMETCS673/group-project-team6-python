
<br>

## Additional Analog Data:
####  Survey
####  Student Answers


CS673 Fall2022 Team 6 - iGroup
=======================================

#### Project Name : iGroup
#### Team name : Panda

|Team members :|
|---|
|Shawn(baymax@bu.edu) - Team leader 
Dawei(davidyin@bu.edu)- Design and Implementation leader
Lijian(yao049@bu.edu) - Configuration leader
Alex(alexrw@bu.edu)- Security leader
Siming(s1a1d1f1@bu.edu)- Requirement Leader
Haiyang(whaiyang@bu.edu) - QA leader |

<br />

## Project Description:

Our project is making a team assign tool that can automatically assign students to a team, which involves the concepts of front-end, back-end, database and so on. We named it "iGroup". The main idea of the Team assignment tool is to help create teams based on students preferences and background. For this application, we choose Python as our development programming language, and use Django as framework. Algorithmically, we weight different preferences to create the most appropriate team.


Iteration Process
|---|
Iteration 0 : 09/07/2022 - 09/21/2022
Iteration 1 : 09/22/2022 - 10/20/2022
Iteration 2 : 10/21/2022 - 11/11/2022
Iteration 3 : 11/12/2022 - 12/10/2022

## List of Completed Features

User - Login,logout, save account data in backend database
Application - Create and Delete (Instance,Survey,Questions,Options)
              Import and uplode Data
              Lock the Survey and Create Survey link to students
              Run the Algorithm base on the collected data 
              Save the all results of team assignment



<br />

## How To Run:
##### Step 1 - Clone the code from GitHub to local device
##### Step 2 - Switch to "dev" branch and pull it again
##### Step 3 - Open the Pycharm Terminal and type: 
               $cd source_code
               $cd web
               $pip install -r requirements.txt
               $python manage.py makemigrations (First time run, Don't need)
               $python manage.py migrate
               $python manage.py runserver 8000
##### Step 4 - Open browser and visit URL: http://127.0.0.1:8000/


<br /><br />

## Tech Stack and Frameworks:

#### Front End: 
HTML: Front End building block 

CSS: Front End building block 

Javascript: used for more dynamic elements in front end

Django : Default

#### Back End:
Django : Framework

Pure Python : Algorithm part 

#### Management:
Git/Github: Version control tool 

Pivotal Tracker: Project Management

#### Database:
Django : SQLite

.CSV file : Analog Data


<br /><br />

## Design Description

#### a.Software Architecture
In our iGroup application, Since we have adopted the agile methodology as the development process, we mainly focus on developing the local application at this iteration, with using local file systems as our persistent data storage.
Within the iGroup system, the user needs to use the account system to gain access to create surveys and send the survey to students, which the student responds to and creates the student account in the system. Then the instructor can gather the response from the students and call the allocation system to do the team allocation corresponding to the parameter that instructor assigned before the allocation.


#### b.Business Logic and/or Key Algorithms
For the process of the algorithm, the first step is to randomly assign all the students into different groups, and then calculate the score of each team (the part of calculating the score here uses the team-maker algorithm). After the score of each group is obtained, the group with the second highest score and the group with the lowest score will swap the team members and calculate the score again, until the new score of both groups has improved, and then confirm to switch the team members. After 20 rounds of this, all the groups were formed. (The Gale-Shapley Algorithm used here)


<br /><br />

## Risk Management
https://docs.google.com/spreadsheets/d/1oXajwHWtP0rqrXSfCWsf2NTtd7TqJNTJ5b6tWfP5csk/edit

<br /><br />

## Configuration Management
#### Tools
Version Control: Git,Github

Front end: VS Code(HTML,CSS), Pycharm (Django Defaults) 

Back end: PyCharm (Python)

Framework: Django

Database: Django(SQLite)

CI/CD:TeamCity(optional)

#### Code Commit Guideline and Git Branching Strategy
During development, we each have our own branch of development. 
Also, we created some special branches for important features.



<br /><br />


## Quality Assurance Management

### Coding Standard
Please refer to this link: 
https://www.geeksforgeeks.org/coding-standards-and-guidelines/
Our standards will be based on the contents in this link.

### Code Review Process
Team members review each other’s code. We will make sure we all review code that is not from ourselves. We will use pull requests for the code review, to make sure there is no conflict. Recently we don’t have a checklist that everyone must do, but we do require the reviewer to give feedback about cleanliness, clarity and bugs.

### 
Testing Plan
|---|
Unit Test 
Integrate Test
System Test
Acceptance Test
Regression Test




<br /><br />

## Related Work:
#### Try to comprehensive the previous student project 
https://github.com/BUMETCS673/BUMETCS673A1F21P3
#### Survey
https://docs.google.com/forms/d/e/1FAIpQLSfkskHnSJLweJSulYyeBenhNPSyzHkQTRW6wzakM_Ffb3gJFA/viewform
#### Team Sign
https://docs.google.com/document/d/1PzFrv9GLrKaXZP46fl1S_kaAev4Gb6BcfAxBUfSvNSs/edit
#### Reference
 https://drive.google.com/drive/u/1/folders/1BBafMsvOnvsn76p2TktR9ZJ1NIbP4Eg5
