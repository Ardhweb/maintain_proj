
#Setup This project with your Local Machine

Step1 - Create an new virtual envirnemnet for it (venv)
Step2- Activate this venv using shell [For win command : venv/scripts/activate]
Step3- github clone for download this project to same parent dir where is your venv is exists.
Step4- If you are running this on windows machine then
after this in shell change directory to project (maintain_proj)
with command [cd maintain_proj]
Step5 -Now in shell run this command [pip install r- requirments.txt]
Step6- Setup is Compeletd Now you can run this with [python manage.py runserve]


API ENDPOINTS & How to Use
POST Request
1.Creating a new timesheet entry with the ability to select multiple projects.

#For Post Request Creating New TimeSheet Entry.
http://127.0.0.1:8000/api/timesheets/create

Json Format for creating new timesheet Enteries

raw/data
{
   "projects":[
      
         1    -this is project pk or id you can assign multiple like 1,2,3
      
   ],
   "user":2,
   "week_start_date":"2023-12-12",
   "hours_worked":"55.33"
}

e.g -

{
   "projects":[
      1,
      2
   ],
   "user":2,
   "week_start_date":"2023-12-12",
   "hours_worked":"55.33"
}


2.Updating existing timesheet entries.

http://127.0.0.1:8000/api/timesheets/12/update/

3.Retrieving a list of timesheet entries for a specific user
User can only check his related timesheets
#
http://127.0.0.1:8000/api/timesheets/lists/



