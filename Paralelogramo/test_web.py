from Paralelogramo import perimetro_paralelogramo
from flask import Flask, render_template, redirect, request

app = Flask (__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry/')
def go_entry() -> 'html':
    return render_template('entry.html', the_title='Hola,Quieres saber cual es el perimetro del paralelogramo,ingresa los datos y calcula')

@app.route("/calculate/", methods=['POST'])
def calculate()->'html':
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = perimetro_paralelogramo(a,b)
    title = "Perimetro from Paralelogramo result"
    return render_template('result.html',
                           the_a=a,
                           the_b=b,
                           the_result=result,
                           the_title=title)
app.run(debug=True)
