from flask import Flask, jsonify
import os

# CORRIGÉ : Utilisation des doubles underscores obligatoires
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
            body { background-color: #0b0e11; color: #eaecef; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 40px; text-align: center; }
            .container { max-width: 800px; margin: auto; background: #181a20; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); border: 1px solid #f3ba2f; }
            h1 { color: #f3ba2f; font-size: 2.5em; margin-bottom: 10px; }
            h2 { color: #848e9c; font-size: 1.2em; font-weight: normal; letter-spacing: 2px; margin-bottom: 30px; }
            .status-box { background: #2b3139; padding: 20px; border-radius: 8px; margin-top: 20px; border-left: 5px solid #02c076; text-align: left; }
            .badge { background-color: #02c076; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold; }
            .console-box { background: #000000; color: #00ff00; font-family: 'Courier New', Courier, monospace; padding: 15px; border-radius: 6px; text-align: left; height: 150px; overflow-y: auto; margin-top: 20px; border: 1px solid #333; }
        </style>
        <script>
            setInterval(function() {
                fetch('/logs')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('console').innerHTML = data.logs.replace(/\\n/g, '<br>');
                    });
            }, 2000);
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🤖 VIREVO AGENT</h1>
            <h2>I SPEAK → IT UNDERSTANDS → IT ANALYZES → IT ACTS</h2>
            
            <div class="status-box">
                <h3>Statut du Système : <span class="badge">ACTIF</span></h3>
                <p><strong>Réseau :</strong> Connecté avec succès à Binance Agent OS.</p>
                <div class="console-box" id="console">Démarrage du flux d'activité de l'agent...</div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/logs")
def obtenir_logs():
    if os.path.exists("agent_activity.log"):
        with open("agent_activity.log", "r") as f:
            lignes = f.readlines()
        return jsonify(logs="".join(lignes[-6:]))
    return jsonify(logs="L'agent se prépare à transmettre ses données...")

# CORRIGÉ : Lancement direct sans bloc conditionnel complexe pour éviter les erreurs
app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)