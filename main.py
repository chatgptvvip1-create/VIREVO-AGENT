import time
from binance.spot import Spot as Client

def obtenir_donnees_reelles(paire):
    try:
        # Connexion à l'API publique de Binance (pas besoin de clés privées pour lire le marché)
        client = Client()
        
        # 1. Récupération du vrai prix en direct
        ticker = client.ticker_price(paire)
        prix_reel = float(ticker['price'])
        
        # 2. Récupération du carnet d'ordres (Order Book) pour calculer la pression
        depth = client.depth(paire, limit=10)
        total_achats = sum(float(ask) for ask in depth['asks'])
        total_ventes = sum(float(bid) for bid in depth['bids'])
        
        # Calcul de la pression des acheteurs (en %)
        pression_achat = (total_achats / (total_achats + total_ventes)) * 100
        
        return prix_reel, pression_achat
    except Exception as e:
        print(f"\n[ERREUR BINANCE] Impossible de lire les données : {e}")
        return None, None

def main():
    print("=========================================")
    print("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    print("=========================================")
    
    while True:
        commande = input("\nUser: ").strip()
        
        if commande.lower() == 'exit':
            print("Shutting down VIREVO AGENT... Goodbye!")
            break
            
        # Vérifie si la commande commence par l'ordre d'analyse
        if commande.upper().startswith("VIREVO, ANALYZE"):
            try:
                # Découpe la commande pour récupérer la paire (ex: BNB/USDT)
                paire_brute = commande.split(" ")[-1]
                paire_binance = paire_brute.replace("/", "").upper()
            except IndexError:
                print("[VIREVO] Format incorrect. Exemple: VIREVO, analyze BNB/USDT")
                continue
                
            print(f"\n[VIREVO] Connecting to Binance Agent OS for {paire_brute}...")
            time.sleep(1)
            
            # Récupération des vraies données du marché
            prix, pression = obtenir_donnees_reelles(paire_binance)
            
            if prix is not None:
                # Logique de décision IA basée sur la vraie pression du carnet d'ordres
                if pression > 55:
                    decision = "STRONG BUY 🚀 (Forte pression acheteuse)"
                    tendance = "BULLISH"
                elif pression < 45:
                    decision = "STRONG SELL 📉 (Forte pression vendeuse)"
                    tendance = "BEARISH"
                else:
                    decision = "HOLD / NEUTRAL ⚖️ (Marché indécis)"
                    tendance = "SIDEWAYS"
                
                print("\n=========================================")
                print("    VIREVO Step 4: ACTIONABLE REPORT     ")
                print("=========================================")
                print(f"Asset        : {paire_brute}")
                print(f"Real Price   : ${prix:,.2f}")
                print(f"Order Book   : {pression:.1f}% Pression d'Achat")
                print(f"Market Trend : {tendance}")
                print("-----------------------------------------")
                print(f"AI Decision  : {decision}")
                print("=========================================")
                
                # Flux de sécurité (Workflow de proposition)
                print(f"\n[PROPOSITION] Souhaitez-vous planifier un achat DCA sur {paire_brute} ?")
                choix = input("Validation humaine (oui/non) : ").strip().lower()
                if choix == 'oui':
                    print(f"[EXECUTION] Ordre préparé pour le sous-compte Agentic. En attente des clés API.")
                else:
                    print("[ANNULATION] Proposition rejetée par l'opérateur.")
            else:
                print("[VIREVO] Erreur lors de l'analyse. Vérifiez le nom de la crypto.")
        else:
            print("[VIREVO] Request not recognized. Commandes disponibles: VIREVO, analyze X/USDT, exit")

if name == "main":
    main()