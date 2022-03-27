from token import NEWLINE
from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')#the render_template method takes the items in the templates folder

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



def write_to_file(data):
    email=data['email']
    subject= data['subject']
    message=data['message']
    with open('./web server/database.txt','a') as database:
        file_writer = database.write(f"\n{email}=>{subject}=>{message}")


def write_to_csv(data):
    email=data['email']
    subject= data['subject']
    message=data['message']
    with open('./web server/database.csv','a', newline='') as database_2:
        csv_writer = csv.writer(database_2,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict() #turn the data into a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'There was an error!'
    else: 
        return 'Something went wrong?'
