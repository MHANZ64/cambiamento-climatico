from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)
ideas_file = 'idee_cambiamento_climatico.txt'

# Pagina principale per l'invio delle idee
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        idea = request.form.get('idea')
        if idea:
            with open(ideas_file, 'a') as file:
                file.write(idea + '\n')
            return redirect(url_for('thanks'))
    return render_template('index.html')

# Pagina di ringraziamento
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

# Pagina per visualizzare le idee
@app.route('/ideas')
def show_ideas():
    with open(ideas_file, 'r') as file:
        ideas = file.readlines()
    return render_template('ideas.html', ideas=ideas)

if _name_ == '_main_':
    app.run(debug=True)