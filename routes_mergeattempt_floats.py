from flask import *
from functools import wraps
import sqlite3
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm, CsrfProtect
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pygal


app = Flask(__name__)
app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Users\Mike\Desktop\PythonSuccess\Beatscrape.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(__name__)
csrf = CsrfProtect(app)

   
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def connect_db2():
	return sqlite3.connect(app.config['SurfSend'])

@app.route('/')  
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


#-------------------------- RHODE ISLAND BEACHES--------------------------------
@app.route('/TwoBeach')
@csrf.exempt
def TwoBeach():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='2nd Beach'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = '2nd Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='2nd Beach' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('TwoBeach.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Narragansett')
@csrf.exempt
def Narragansett():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Narragansett'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Narragansett 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Narragansett' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Narragansett.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)



@app.route('/Ruggles')
@csrf.exempt
def Ruggles():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Ruggles'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Ruggles 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Ruggles' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Ruggles.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)



#--------------------------MA BEACHES--------------------------------




@app.route('/Nahant')
@csrf.exempt
def Nahant():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Nahant'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Nahant 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nahant' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Nahant.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Nantasket')
@csrf.exempt
def Nantasket():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Nantasket'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Nantasket 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Nantasket' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Nantasket.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Scituate')
@csrf.exempt
def Scituate():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Scituate'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Scituate 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Scituate' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Scituate.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/CapeCod')
@csrf.exempt
def CapeCod():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Cape Cod'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Cape Cod 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Cape Cod' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('CapeCod.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/GreenHarbor')
@csrf.exempt
def GreenHarbor():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Green Harbor'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Green Harbor 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Green Harbor' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('GreenHarbor.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)

@app.route('/CapeAnn')
@csrf.exempt
def CapeAnn():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Cape Ann'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Cape Ann 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name = 'Cape Ann' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('CapeAnn.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Devereux')
@csrf.exempt
def Devereux():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Devereux Beach'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Devereux Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Devereux Beach' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Devereux.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Salisbury')
@csrf.exempt
def Salisbury():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Salisbury'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Salisbury Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Salisbury' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Salisbury.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)

@app.route('/Plymouth')
@csrf.exempt
def Plymouth():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Plymouth'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Plymouth Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Plymouth' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Plymouth.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


#--------------------------NH BEACHES--------------------------------

@app.route('/Rye')
@csrf.exempt
def Rye():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Rye'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Rye Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Rye' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Rye.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)

@app.route('/Hampton')
@csrf.exempt
def Hampton():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Hampton'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Hampton Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Hampton' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Hampton.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)


@app.route('/Seabrook')
@csrf.exempt
def Seabrook():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='Seabrook'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'Seabrook Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='Seabrook' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('Seabrook.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)

@app.route('/NHSeacoast')
@csrf.exempt
def NHSeacoast():
	#responsible for getting X,Y values, both lists stored as variables mylist & newl
	conn = sqlite3.connect('SurfSend.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	# valuesx = c.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'").fetchall()
	values = c.execute("select distinct avg_day from surfmaster2 where beach_name ='NH Seacoast'").fetchall()

	mmm = [float(i) for i in values]

	labels = c.execute("select distinct date_ from surfmaster2").fetchall()
	mylist = []
	for l in labels:
		dates = l[5:]
		mylist.append(str(dates))
	print(mylist)
	print(mmm)

	#code responsible for graphing the pygal chart ... using data from the DB, from list objects mylist & newl
	graph = pygal.Line()
	graph.title = 'NHSeacoast Beach 7 Day Surf Forecast'
	graph.x_labels = mylist
	graph.add('Avg Wave Height',  mmm)
	graph_data = graph.render_data_uri()
	#original code, used for creating table in Nahant.html

	# getdate() table
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info1 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now')")
	info2 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+1 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+1 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info3 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+1
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+1 day')")
	info4 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+2 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+2 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info5 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+2
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+2 day')")
	info6 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()

	# getdate()+3 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+3 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info7 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+3
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+3 day')")
	info8 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+4 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+4 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info9 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+4
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+4 day')")
	info10 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+5 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+5 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info11 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+5 day')")
	info12 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()


	# getdate()+6 table
	cursor = conn.cursor()
	cursor.execute("select SwellSizeFt, SwellIntervalSec, WindMPH, WindDescription, AirTemp, beach_name, date_, time_, state from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+6 day') order by SurfMaster2.beach_name ASC, SurfMaster2.date_ ASC")
	info13 = [dict(SwellSize=row[0], SwellInterval=row[1], WindSpeed=row[2], WindDescription=row[3], AirTemperature=row[4], Beach=row[5], Day=row[6], Tiempo=row[7], St8=row[8]) for row in cursor.fetchall()]
	cursor.close()

	# distinct day for getdate()+5
	cursor = conn.cursor()
	cursor.execute("select distinct date_ from SurfMaster2 where beach_name ='NH Seacoast' and date_ = date('now','+6 day')")
	info14 = [dict(DayDistinct=row[0]) for row in cursor.fetchall()]
	cursor.close()



	return render_template('NHSeacoast.html', selected='submit',info1=info1, info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7, info8=info8,  info9=info9,  info10=info10,  info11=info11,  info12=info12,  info13=info13,  info14=info14,  graph_data=graph_data)



@app.route('/hello')
@login_required
def hello():
	g.db = connect_db()
	cur = g.db.execute('select Artist, Song, Label, Price from BeatPortTechHouse')
	info = [dict(Artist=row[0], Song=row[1], Label=row[2], Price=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('hello.html', info=info)




if __name__ == '__main__':
	app.run(debug=True)