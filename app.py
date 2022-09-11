from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""Привет"""


@app.route('/petya/')
def petya():  # put application's code here
    return ''' <h2> Александр Твардовский

Василий Теркин. Сборник

Лирика

РОДНОЕ

<br>Дорог израненные спины, </br>
<br>Тягучий запах конопли…  </br>
<br>Передо мной знакомые картины  </br>
<br>И тихий вид родной земли… </br>
<br>Я вижу – в сумерках осенних </br>
<br>Приютом манят огоньки. </br>
<br>Иду в затихнувшие сени, </br>
<br>Где пахнет залежью пеньки. </br>
<br>На стенке с радостью заметить </br>
<br>Люблю приклеенный портрет. </br>
<br>И кажется, что тихо светит </br>
<br>В избе какой-то новый свет. </br>
<br>Еще с надворья тянет летом, </br>
<br>Еще не стихнул страдный шум… </br>
<br>Пришла «Крестьянская газета», </br>
<br>Как ворох мужиковских дум.  </br>
<br>А проскрипит последним возом </br>
<br>Уборка хлеба на полях — </br>
<br>И осень закует морозом </br>
<br>В деревне трудовой размах. </br>
<br>Придет зима. Под шум метелей </br>
<br>В читальне, в радостном тепле, </br>
<br>Доклад продуманный застелет </br>
<br>Старинку темную в селе… </br>
<br>А за столом под шум газетный </br>
<br>Улыбки вспыхнут в бородах, </br>
<br>Прочтя о разностях на свете, </br>
<br>О дальних шумных городах. </br>
    </h2> '''


@app.route('/user/<username>')
def user_profile(username):  # put application's code here
    return render_template('index.html',title=str(random.randint(1,4)))


@app.route('/user/<int:post_id>')
def show_post(post_id):  # put application's code here
    return f"<h1>Горячая и свежая новость № {post_id}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
