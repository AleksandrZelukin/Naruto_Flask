from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# db = sqlite3.connect('noma.db')
# sql = db.cursor()
# sql.execute("""CREATE TABLE IF NOT EXISTS nomnieks(
#     id_nomnieks TEXT PRIMARY KEY,
#     "vards" TEXT, 
#     "uzvards" TEXT, 
#     "talrunis" TEXT
# )""")

# db.commit()


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/gaara')
def gaara():
  return render_template('gaara.html')

@app.route('/hinata')
def hinata():
  return render_template('hinata.html')

@app.route('/ielogoties1')
def ielogoties1():
  return render_template('ielogoties1.html')

@app.route('/ino')
def ino():
  return render_template('ino.html')
  
@app.route('/jiraja')
def jiraja():
  return render_template('jiraja.html')

@app.route('/kakashi')
def kakashi():
  return render_template('kakashi.html')

@app.route('/karte')
def karte():
  return render_template('karte.html')

@app.route('/naruto')
def naruto():
  return render_template('naruto.html')

@app.route('/orochimaru')
def orochimaru():
  return render_template('orochimaru.html')

@app.route('/palidziba')
def palidziba():
  return render_template('palidziba.html')
  
@app.route('/par_mums')
def par_mums():
  return render_template('Par_mums.html')

@app.route('/roclee')
def roclee():
  return render_template('roclee.html')

@app.route('/Sakura')
def sakura():
  return render_template('Sakura.html')

@app.route('/Saske')
def saske():
  return render_template('Saske.html')

@app.route('/shikamaru')
def shikamaru():
  return render_template('shikamaru.html')

@app.route('/tsunada')
def tsunada():
  return render_template('tsunada.html')

@app.route('/varoni')
def varoni():
  return render_template('varoni.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)