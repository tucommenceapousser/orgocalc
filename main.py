from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # Récupérer les données du formulaire
    side = request.form.get("side")
    height = request.form.get("height")
    cuivre = request.form.get("cuivre")
    aluminium = request.form.get("aluminium")
    fer = request.form.get("fer")
    quartz = request.form.get("quartz")
    amethyste = request.form.get("amethyste")
    fluorite = request.form.get("fluorite")
    obsidienne = request.form.get("obsidienne")
    tourmaline = request.form.get("tourmaline")
    shungite = request.form.get("shungite")
    resine = request.form.get("resine")

    # Calcul du volume de la pyramide
    if side and height:
        volume = (1/3) * (float(side) ** 2) * float(height)
        result = f"Le volume de la pyramide est de {volume:.2f} unités cubiques."
    else:
        # Calcul des ondes gérées
        total_material = sum(float(val) for val in [cuivre, aluminium, fer, quartz, amethyste, fluorite, obsidienne, tourmaline, shungite, resine] if val)
        result = f"Les matériaux gèrent un total de {total_material:.2f} ondes."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
