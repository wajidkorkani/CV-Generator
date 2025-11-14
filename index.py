from flask import Flask, request, render_template as render, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Home():
  return render("index.html", text="Flask")

@app.route('/form')
def Form():
  return render('form.html')

@app.route('/generate-cv', methods=['POST'])
def Generate_CV():
  if(request.method == "POST"):
    name = request.form['name']
    return redirect(url_for('Home'))

app.run(debug=True)