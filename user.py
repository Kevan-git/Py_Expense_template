from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New Expense - Name: ",
    }
]

def add_user():
    infos = prompt(user_questions)
    with open('users.csv','a') as users_file:
        csv_writer = csv.writer(users_file)
        csv_writer.writerow([infos['name']])
    print("User Added !")
    return