from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VIREVO AGENT - Binance Dashboard</title>
        <style>
            body {
                background-color: #0b0e11;
                color: #eaecef;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 40px;
                text-align: center;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background: #181a20;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                border: 1px solid #f3ba2f;
            }
            h1 {
                color: #f3ba2f; /* Couleur Or officielle de Binance */
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            h2 {
                color: #848e9c;
                font-size: 1.2em;
                font-weight: normal;
                letter-spacing: 2px;
                margin-bottom: 30px;
            }
            .status-box {
                background: #2b3139;
                padding: 20px;
                border-radius: 8px;
                margin-top: 20px;
                border-left: 5px solid #02c076; /* Vert pour indiquer actif */
                text-align: left;
            }
            .badge {
                background-color: #02c076;
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.8em;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 VIREVO AGENT</h1>
            <h2>I SPEAK → IT UNDERSTANDS → IT ANALYZES → IT ACTS</h2>
            
            <div class="status-box">
                <h3>Statut du Système : <span class="badge">ACTIF</span></h3>
                <p><strong>Réseau :</strong> Connecté avec succès à Binance Agent OS.</p>
                <p><strong>Fonction :</strong> Analyse des marchés et exécution d'ordres par IA en cours.</p>
            </div>
        </div>
    </body>
    </html>
    """

if name == "main":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)