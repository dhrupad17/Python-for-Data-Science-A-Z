from flask import Flask,render_template,request

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to Get and Post Request Working</h1></html>"

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name} Welcome to the course!"
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name} Welcome to the course!"
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)

