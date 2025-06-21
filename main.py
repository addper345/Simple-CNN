
from flask import Flask, request, make_response, render_template
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'

# decorator to route URL 
@app.route('/hello') 

# binding to the function of route 
def hello_world():     
    return 'hello world'

@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie(): 
    if request.method == 'POST': 
        user = request.form['nm'] 
        resp = make_response(render_template('cookie.html')) 
        resp.set_cookie('userID', user) 
        return resp 

@app.route('/getcookie') 
def getcookie(): 
    name = request.cookies.get('userID') 
    return '<h1>welcome '+name+'</h1>'
  
if __name__=='__main__': 
   app.run() 