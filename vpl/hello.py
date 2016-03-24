from flask import Flask
from flask import jsonify 
from flask import session,render_template,url_for,send_from_directory,request,redirect,make_response
from sqlalchemy import create_engine
from flask_socketio import SocketIO,emit
engine = create_engine('mysql://root@localhost/csv_db')
connection = engine.connect()
app = Flask(__name__)
app.secret_key = 'ajaadike'
print("run")
socketio = SocketIO(app,message_queue='redis://')
l=[]
price=10000
x= True
email="";name="asd";pop="asd";class2="asd";no="asd";photo="asd";pool="asd"
@app.route('/admin')
def admin():
	return render_template("dir.html")

@app.route('/emails',methods=['POST','GET'])
def emails():
	global price
	global email
	global name;global pop;global class2;global no;global photo;global pool;

	if request.method=='POST':
		return jsonify(name=name,pop=pop,pool=pool,class1=class2,no=no,photo="",price=str(price))
	return "SECRET HAI BAAP"

@app.route('/myteam')
def myteam():
	result = engine.execute("select * from `table 3` where `Team`='"+session['name']+"'")
	name=""
	res=[]
	for row in result:
		temp={}
		temp['LINK']="./cont/img/"+str(row['Photo'])+"/1.jpg"
		temp['PRICE']=str(row['Price'])
		temp['NAME']=row['First name']
		res.append(temp)
	result.close();
	j={}
	j['result']=res
	print (j)
	result = engine.execute("select * from users where id='"+session['name']+"'")
	name=""
	for row in result:
		name=row['balance']
	result.close();

	if 'name' in session:
		return render_template("myteam.html",dict=j,balance=name)
	else :
		return render_template('login.html')







@app.route('/home')
def k():
	if 'name' in session:
			result = engine.execute("select * from users where id='"+session['name']+"'")
			name=""
			for row in result:
				name=row['balance']
			result.close();
			resp = make_response(render_template('index.html',name='cont/assets/img/avatars/avatar_11_tn.png',balance=name))
			resp.set_cookie('name', session['name'])
			return resp
	else:
			return render_template('login.html') 




@app.route('/login',methods=['POST','GET'])
def login():
	print("Logged in")
	error=None
	session['name']=""
	if request.method=='POST':
		result = engine.execute("select * from users where id='"+str(request.form['login_username'])+"' AND password ='"+str(request.form['login_password'])+"'")
		for row in result:
			session['name']=request.form['login_username']
		result.close()		
	return  redirect(url_for('k'))



@app.route('/cont/<path:path>')
def send(path):
    return send_from_directory('cont', path)



@socketio.on('my event')
def handle_my_custom_event(json):
    print ("Myevent")
    if x==True:
    	global l
    	global price
    	
    	a=""
    	if len(l)!=0:
    		a=l.pop()
    		l.append(a)
    	if str(a)!=str(session['name']):
    		if 6000000>int(price) and int(price) >=4000000:
    			price=int(price)+200000
    			
    		if 10000000>int(price) and int(price) >=6000000:
    			
    			price=int(price)+500000
    		if int(price) >=10000000:
    			
    			price=int(price)+1000000		
    		emit('my response',{'data':str(price),'name':session['name']},broadcast=True)
    		l.append(session['name'])
    		
    return	

@app.route('/hello.py')
def hello():
	session['name']="amey"
	return render_template("sock.html")

@socketio.on('my')
def handlg(json):
	print ("works")
	return render_template('login.html')

@socketio.on('selling')
def handlsomething(json):
	print ("Selling")

	global price
	global l
	a=l.pop()
	
	emit('sold',{'user':str(a),'data':str(price)},broadcast=True)
	return
@socketio.on('start')
def start(json):
	print ("Start")
	global x
	
	if x!=True :
		x=True
		
	else :
		x=False

	return
@socketio.on('sell')
def star(json):
	print ("Sell")
	global email
	
	global price
	global l
	a=l.pop()
	
	
	
	result = engine.execute("update `table 3` set `Team`='"+str(a)+"',`Price`= '"+str(price)+"' where `Email`='"+email+ "'")
	result.close();

	result = engine.execute("update users set balance=balance-"+str(price)+" where id='"+str(a)+ "'")
	result.close();
	del l[:]
	emit('sold',{'user':str(a),'data':str(price)},broadcast=True)
	return
@socketio.on('kk')
def stark(json):
	print ("Testing")
	emit('change',{'data':'amey'},broadcast=True)	
	return
@app.route('/data',methods=['POST','GET'])
def data():
	global srno
	global pool
	k={}
	global price
	global email
	global name;global pop;global class2;global no;global photo;global pool;

	if request.method=='POST':
		
		if pool!=str(request.form['pool']):
			pool=str(request.form['pool'])
			srno=1
		else :
			srno=srno+1
		
		result = engine.execute("select * from pool"+pool+" where srno='"+str(srno)+"'")
		for row in result:
				k['name']=name=row['First name']
				k['pool']=row['Pool']
				k['class1']=class2=row['Class']
				k['no']=no=row['Mobile Number']
				k['photo']=photo="./cont/img/"+str(row['Photo'])+"/1.jpg"
				k['price']=price=row['Price']
				k['Email']=email=row['Email']
				k['pop']=pop=row['Position Of Play']
		result.close()		
	return  str(k)
@app.route('/data1',methods=['POST','GET'])
def data1():
	global srno
	global pool
	k={}
	global price
	global email
	global name;global pop;global class2;global no;global photo;global pool;

	if request.method=='POST':
		
		if pool!=str(request.form['pool']):
			pool=str(request.form['pool'])
			srno=1
		else :
			srno=srno-1
		
		result = engine.execute("select * from pool"+pool+" where srno='"+str(srno)+"'")
		for row in result:
				k['name']=name=row['First name']
				k['pool']=row['Pool']
				k['class1']=class2=row['Class']
				k['no']=no=row['Mobile Number']
				k['photo']=photo="./cont/img/"+str(row['Photo'])+"/1.jpg"
				k['price']=price=row['Price']
				k['Email']=email=row['Email']
				k['pop']=pop=row['Position Of Play']
		result.close()		
	return  str(k)
@app.route('/data2',methods=['POST','GET'])
def data2():
	global srno
	global pool
	k={}
	if request.method=='POST':
		result = engine.execute("select * from pool"+pool+" where srno='"+str(srno)+"'")
		for row in result:
				k['name']=row['First name']
				k['pool']=row['Pool']
				k['class1']=row['Class']
				k['no']=row['Mobile Number']
				k['photo']=photo="./cont/img/"+str(row['Photo'])+"/1.jpg"
				k['price']=row['Price']
				k['pop']=pop=row['Position Of Play']
		result.close()		
	return  str(k)
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=81)
    app.run(host='0.0.0.0',debug=False,port=81)

#url_for('static', filename='game1.unity3d')