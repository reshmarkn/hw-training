from datetime import datetime as dt
import json
class WorkingHours():
    def __init__(self,employee_name,employee_id):
        self.employee_name=employee_name
        self.employee_id=employee_id
    def login(self):
        return dt.now().strftime("%Y-%m-%d %H:%M")
    def logout(self):
        return dt.now().strftime("%Y-%m-%d %H:%M")
    def add_task(self):
        task=[
            {
            'task1':'Accounting',
            'description':'Establishes financial status by developing and implementing systems',
            'start_time':dt.now().strftime("%Y-%m-%d %H:%M"),
            'task_status':'success',
            'end_time':dt.now().strftime("%Y-%m-%d %H:%M")
            },
            {
            'task2':'Sales Cordination',
            'description':'Cordinating training and scheduling for sales staff.',
            'start_time':dt.now().strftime("%Y-%m-%d %H:%M"),
            'task_status':'failure',
            'end_time':dt.now().strftime("%Y-%m-%d %H:%M")
            },
            {
            'task3':'recruitment',
            'description':'recruiting students',
            'start_time':dt.now().strftime("%Y-%m-%d %H:%M"),
            'task_status':'success',
            'end_time':dt.now().strftime("%Y-%m-%d %H:%M")
            }
        ]
        return task
        
emp=WorkingHours("reshu",1)
employee_information={
    'emp_name':emp.employee_name,
    'emp_id':emp.employee_id,
    'login_time':emp.login(),
    'logout_time':emp.logout(),
    'tasks':emp.add_task()
}
json_object=json.dumps(employee_information,indent=4)
with open("2020-08-18.json","w") as outfile:
    outfile.write(json_object)
print(json_object)



