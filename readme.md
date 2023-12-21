# Expenses Manager

### Architecture

- Backend Language: Python.
- Backend Framework: Django.
- Comunication: Rest APIs.
- Services: Lambda, Speech, Transcribe, S3.
- Frontend Language: JavaScript.
- Frontend Framework: Vue.js

### About 

This application should allow users to store their expenses using a easy going method, user can record the expense information in a provided format or he can write expenses information.
As the cherry on top of cake we provide a dashboard that has many filters to user track his expenses, week by week, month by month and etc...

We're using some AWS services like S3 to store the recorded audios, Speech to record audios and transcribe to transcribe the audios and store it as useful information.

### Features

- Expenses manually insertion - to user write each expense data.
    - Create, Delete, Read and Update.
- Voice record - to allow users to talk their expenses. 
- Dashboard - to user track his expenses.
- Expenses import - allow importing from csv a bulk of expenses.
- Expenses export - export of all expenses and dashboard results to many formats.


