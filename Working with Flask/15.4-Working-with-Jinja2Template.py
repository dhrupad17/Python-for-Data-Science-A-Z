### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Jinja2 Template Tutorial</H1></html>"

## Variable Rule

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html',results=res)

## Variable Rule (Key , value)

@app.route("/result/<int:score>")
def result(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'Score':score,"Result":res}
    return render_template('result1.html',results=exp)


## if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)


## Dynamic URLs
@app.route('/submit',methods=['POST,GET'])
def submit():
    total_score=0
    if request.method=='POST':
        java=float(request.form['java'])
        python=float(request.form('python'))
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(java+python+c+data_science)/4

    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



if __name__=="__main__":
    app.run(debug=True)