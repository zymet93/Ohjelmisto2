#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö
# annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.


from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<int:n>')
def prime_number(n):
    """Returns True if n is a prime number, else False."""
    if n == 1:
        return ({'Number': n, 'isPrime': False})
    if n == 2:
        return ({'Number': n, 'isPrime': False})

    for i in range(2, int(n)):
        if n % i == 0:
            return ({'Number': n, 'isPrime': False})
    return ({'Number': n, 'isPrime': True})


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)