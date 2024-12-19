from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Calcul des ondes
@app.route('/calculate', methods=['POST'])
def calculate():
    # Récupération des données
    cuivre = float(request.form.get('cuivre', 0))
    aluminium = float(request.form.get('aluminium', 0))
    fer = float(request.form.get('fer', 0))
    quartz = float(request.form.get('quartz', 0))
    amethyste = float(request.form.get('amethyste', 0))
    fluorite = float(request.form.get('fluorite', 0))
    obsidienne = float(request.form.get('obsidienne', 0))
    tourmaline = float(request.form.get('tourmaline', 0))
    shungite = float(request.form.get('shungite', 0))
    resine = float(request.form.get('resine', 0))

    # Calcul des ondes (pondérations arbitraires pour l'exemple)
    ondes_scalaires = (
        cuivre * 1.5 + aluminium * 1.2 + fer * 1.1 +
        quartz * 2.0 + amethyste * 2.5 + fluorite * 2.2 +
        obsidienne * 1.8 + tourmaline * 2.1 + shungite * 2.4 +
        resine * 1.0
    )
    ondes_electromagnetiques = (
        cuivre * 1.8 + aluminium * 1.5 + fer * 1.3 +
        quartz * 1.7 + amethyste * 1.8 + fluorite * 1.5 +
        obsidienne * 1.3 + tourmaline * 1.9 + shungite * 2.0 +
        resine * 0.8
    )

    # Transmission des résultats à la page
    return render_template(
        'results.html',
        scalaires=ondes_scalaires,
        electromagnetiques=ondes_electromagnetiques
    )

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
