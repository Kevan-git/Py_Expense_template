from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    }

]





def new_expense(*args):
    infos = prompt(expense_questions)
    with open('users.csv', newline='') as users_file:
        csv_reader = csv.reader(users_file)
        users = [row[0] for row in csv_reader]

    spender_questions = [
        {
            "type":"list",
            "name":"spender",
            "message":"New Spender - Spender: ",
            "choices": users
        }
    ]
    spender = prompt(spender_questions)['spender']
    users.remove(spender)

    users = [{'name': row} for row in users]

    involved_questions = [
        {
            "type":"checkbox",
            "name":"involved",
            "message":"Involved users: ",
            "choices": users
        }
    ]
    involved = prompt(involved_questions)['involved']
    involved.append(spender)
    payback = float(infos['amount'])/len(involved)

    with open('expenses.csv','a') as expenses_file:
        csv_writer = csv.writer(expenses_file)
        csv_writer.writerow([infos['amount'],infos['label'],spender,involved, payback])
    
    
    print("Expense Added !")
    return True


