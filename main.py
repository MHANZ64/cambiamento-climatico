from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Definisci il file per memorizzare le idee
ideas_file = 'memoria.txt'  
comments = []  # Inizializza anche la lista dei commenti

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Gestione dei commenti
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if name and email and message:
            comments.append({'name': name, 'email': email, 'message': message})
        
        # Gestione delle idee
        idea = request.form.get('idea')
        if idea:
            with open(ideas_file, 'a') as file:
                file.write(idea + '\n')
            return redirect(url_for('thanks'))

    return render_template('index.html', comments=comments)  # Correzione qui

@app.route('/thanks')
def thanks():
    return "Grazie per aver inviato la tua idea!"

if __name__ == '__main__':
    app.run(debug=True)