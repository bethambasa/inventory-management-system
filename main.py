# importing
# import <filename>
# from filename import <.....>

from flask import Flask, render_template, request, redirect, url_for

import pygal

import psycopg2

from flask_sqlalchemy import SQLAlchemy

from config.config import Development,Production

 
#FLASK-SQLALCHEMY 
    #Library that helps us write classes object to communicate to our database without
    #writing sql statements

   # EXAMPLE 
    #INSERT INTO sales VALUES (inv_id=1, quantity=10, created=now())

    #create a class and it SalesModel
    #then create function that inserts records
    #then insert

    #class SalesModel():
        #def insert_sales(self):
           # db.session.add()
        
    #query

       # def query_sales(self):
            #self.query.all()
 

# calling/ instanciating

#PSYCOPG2
    #Its a python library that helps write queries in flask
    #HOW TO USE IT
    #1. install it
    #2. set up a connection to your database 
        #- username
        #- password
        #- port
        #- root
        #- dbname
    #3. connect to using cursor
    #4. execute an SQL Statement
    #5. Fetch your records



app = Flask(__name__)
# load configuration

# calling/ instanciating
db= SQLAlchemy(app)

app.config.from_object(Productionconfig)

# Creating of endpoints/ routes
# 1. declaration of a route
# 2. a function embedded to the route

conn = psycopg2.connect(
        dbname='d5agpncjn4ork6'
        user='zqgtjktttrhkai'
        host='ec2-52-201-55-4.compute-1.amazonaws.com'
        port='5432'
        password='084fd839350946db1d97269c132c0f717a5dc954b6380c3172d407387de6cc0e')
        cur = conn.cursor()



#creating tables
from models.inventory import InventoryModel
from models.sales  import SalesModel
from models.stock  import StockModel


@app.before_first_request
def create_table():
    db.create_all()

def drop_table():
    db.drop_all()
  
 

@app.route('/')
def hello_world():
    return '<h1>Welcome to web development</h1>'
@app.route('/home')
def home():
    return '<h1>Welcome to Home Page</h1>'
# @app.route('/name/<name>')
# def my_name(name):
#     # return f'My name is {name}'
#     # return 'My name is {}'.format(name)
#     return 'My name is ' +name
# add two numbers dynamically
@app.route('/add/<a>/<b>')
def adding(a, b):
    sum = int(a)+int(b)
    return str(sum) 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact_us')
def contact():
    return render_template('contact.html')

@app.route('/service') 
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/inventories', methods=['GET', 'POST'])
def inventories():
    # recieve from a form
    
    if request.method == 'POST':
        name = request.form['name']
        inv_type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)
        
        new_inv=InventoryModel(name=name,inv_type=inv_type,buying_price=buying_price,selling_price=selling_price)
        db.session.add(new_inv)
        db.session.commit()
        
        return redirect(url_for('inventories'))
 
    return render_template('inventory.html')
# A ROUTE TO RECIEVE STOCK DATA FROM ADD STOCK MODAL
@app.route('/add_stock', methods=['POST'])
def add_stock():
    # check if the method is post
    if request.method == 'POST':
        stock = request.form['stock']
        print(stock)
        return redirect(url_for('inventories'))
        
@app.route('/make_sale', methods=['POST'])
def make_sale():
    if request.method == 'POST':
        quantity = request.form['quantity']
        print(quantity)
        return redirect(url_for('inventories'))
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # recieve from a form
    
    if request.method == 'POST':
        name = request.form['name']
        inv_type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)
        return redirect(url_for('inventories'))
 

@app.route('/data_visualisation')
def data_visualization():


    pie_chart = pygal.Pie()
    pie_chart.title = 'Distribution of corona virus in Kenya'
    pie_chart.add('Nairobi', 53)
    pie_chart.add('Mombasa', 20)
    pie_chart.add('kilifi', 12)
    pie_chart.add('Kiambu', 9)

    return pie_chart.render()

    return 'my charts here'

    pie_chart=pie_chart.render_data_uri()

    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

    return line_chart.render() 
     
    return render_template('charts.html',pie=pie_data, line=line_data)
    line_graoh=line_graph.render_data_uri()

    @app.route('/view_sales/<inv_id>')
    def view_sales(inv_id):
        sales=salesModel.get_sales_by_id(inv_id)

        return render_template('view_sales.html')


    if __name__ == "__main__":

       app.run()