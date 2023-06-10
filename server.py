from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "quirkless"

@app.route('/')
def main_page():
    return render_template("index.html")

# # ('/process)route function that submits data that use inputs when button is pressed 
# @app.route('/process', methods = ['POST'])
# def submit_data():
#     session['user'] = request.form['user']
#     return redirect('/index.html')

#!or?

@app.route('/process', methods = ['POST'])
def submit_data():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']


    print(request.form)
    return redirect('/result')



# save the form data into session ???



#localhost:5001/result ('/result') - app route that redirects to "indexR.html" (results page) that shows user submitted info by post
@app.route('/result')
def show_results():
    return render_template('indexR.html')


if __name__=="__main__":
    app.run(debug=True, port=5001)
