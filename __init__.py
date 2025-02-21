from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

@app.route('/api/search', methods=['GET'])
def search_client():
    query = request.args.get('nom')

    if not query:
        return jsonify({"error": "Veuillez fournir un paramètre 'nom' pour la recherche."}), 400

    # Utiliser une requête SQL LIKE pour rechercher le nom dans la base de données
    cursor.execute("SELECT * FROM clients WHERE nom LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_value = list_element.get('temp', {}).get('day') - 273.15  # Correction here
        results.append({'Jour': dt_value, 'temp': temp_value})
    return jsonify(results=results)


  
@app.route("/fr/")
def monfr():
    return "<h2>Bonjour tout le monde  !</h2>"
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
