import random
import requests
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to fetch random project name
def fetch_project_name():
    response = requests.get("https://api.namefake.com/")
    data = response.json()
    return data['name']

# Function to fetch random project description
def fetch_project_description():
    response = requests.get("https://baconipsum.com/api/?type=all-meat&sentences=1&start-with-lorem=1")
    data = response.json()
    return data[0]

# Function to fetch random project note
def fetch_project_note():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data['content']

# Function to fetch random project client
def fetch_project_client():
    return fake.company()

# Function to generate random project budget
def generate_project_budget():
    return '$' + str(random.randint(1000, 10000))

# Function to generate random start and end dates for the project
def generate_project_dates():
    start_date = datetime.now() + timedelta(days=random.randint(-365, 0))
    end_date = start_date + timedelta(days=random.randint(30, 365))
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

# Function to generate random tasks
def generate_tasks():
    tasks = ['Design UI mockups', 'Develop backend logic', 'Test application functionality',
             'Implement user authentication', 'Optimize database queries',
             'Conduct security audit', 'Prepare deployment plan', 'Document codebase',
             'Conduct client meeting', 'Finalize project documentation']
    return random.sample(tasks, 10)

# Function to fetch a random developer name
def fetch_developer_name():
    response = requests.get("https://api.namefake.com/")
    data = response.json()
    return data['name']

# Function to generate random bank account details
def generate_bank_account_details():
    return 'Account Number: ' + fake.credit_card_number(card_type=None)

# Function to generate a random address
def generate_address():
    return fake.address()

# Function to generate a simple password
def generate_password():
    return fake.password()

# Function to generate a random join date for the developer
def generate_join_date():
    return fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')

# Function to generate random bugs for each task
def generate_bugs(tasks):
    bugs = {}
    for task in tasks:
        bugs[task] = fake.sentence()
    return bugs

# Generate project data
project_data = {
    'project': {
        'name': fetch_project_name(),
        'description': fetch_project_description(),
        'note': fetch_project_note(),
        'client': fetch_project_client(),
        'budget': generate_project_budget(),
        'dates': generate_project_dates(),
        'tasks': generate_tasks()
    },
    'developer': {
        'name': fetch_developer_name(),
        'bank_account_details': generate_bank_account_details(),
        'address': generate_address(),
        'password': generate_password(),
        'join_date': generate_join_date()
    }
}

# Generate bugs for each task
project_data['bugs'] = generate_bugs(project_data['project']['tasks'])

# Write data to text file
with open('project_data.txt', 'w') as file:
    file.write('Project Details:\n\n')
    file.write('Name: ' + project_data['project']['name'] + '\n')
    file.write('Description: ' + project_data['project']['description'] + '\n')
    file.write('Note: ' + project_data['project']['note'] + '\n')
    file.write('Client: ' + project_data['project']['client'] + '\n')
    file.write('Budget: ' + project_data['project']['budget'] + '\n')
    file.write('Start Date: ' + project_data['project']['dates'][0] + '\n')
    file.write('End Date: ' + project_data['project']['dates'][1] + '\n\n')
    file.write('Tasks:\n')
    for i, task in enumerate(project_data['project']['tasks']):
        file.write(f'{i+1}. {task}\n')
        file.write(f'   Bug: {project_data["bugs"][task]}\n')
    
    file.write('\n\nDeveloper Details:\n\n')
    file.write('Name: ' + project_data['developer']['name'] + '\n')
    file.write('Bank Account Details: ' + project_data['developer']['bank_account_details'] + '\n')
    file.write('Address: ' + project_data['developer']['address'] + '\n')
    file.write('Password: ' + project_data['developer']['password'] + '\n')
    file.write('Join Date: ' + project_data['developer']['join_date'] + '\n')
