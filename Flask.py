from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def g():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def h():
    otvet = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(otvet)


@app.route('/image_mars')
def show_image():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <h2><img src="/static/mars.jpg" alt="здесь должна была быть картинка, но не нашлась"></h2>
                        <meta charset="utf-8">
                        <h3>Вот она какая, красная планета!</h3>
                      </body>
                    </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
