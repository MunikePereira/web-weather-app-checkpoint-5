from flask import Flask, render_template, request
import requests

API_KEY = "34bec0cadd4c1616c443e299970fd2d0"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    erro = None
    
    if request.method == "POST":
        cidade = request.form.get("cidade")
        if cidade:
            # URL corrigida para o endpoint oficial da OpenWeatherMap v2.5
            url = f"https://openweathermap.org{cidade}&appid={API_KEY}&units=metric&lang=pt_br"
            try:
                res = requests.get(url)
                if res.status_code == 200:
                    clima = res.json()
                else:
                    erro = "Cidade não encontrada."
            except requests.exceptions.RequestException:
                erro = "Erro ao conectar ao serviço de clima."
        
    # O return deve ficar fora do bloco 'if' para responder tanto ao GET quanto ao POST
    return render_template("index.html", clima=clima, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)