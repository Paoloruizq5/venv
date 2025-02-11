from flask import Flask


app = Flask (__name__)


@app.route('/alumnos')
def getAlumnos():
    return 'Aqui van alumnos'


if __name__ =='__main__':
    app.run(debug=True)