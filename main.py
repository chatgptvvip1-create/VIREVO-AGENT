import time
from binance.spot import Spot as Client

def calculer_ressemblance(m1, m2):
    m1, m2 = m1.upper(), m2.upper()
    communs = sum(1 for c in m1 if c in m2)
    mx = max(len(m1), len(m2))
    return (communs / mx) * 100 if mx > 0 else 0

def obtenir_donnees_reelles(paire):
    try:
        client = Client()
        ticker = client.ticker_price(paire)
        prix_reel = float(ticker['price'])
        depth = client.depth(paire, limit=10)
        tot_a = sum(float(a) for a in depth['asks'])
        tot_v = sum(float(b) for b in depth['bids'])
        pression = (tot_a / (tot_a + tot_v)) * 100
        return prix_reel, pression
    except Exception as e:
        print(f"\n[ERREUR] Binance : {e}")
        return None, None

def executer_analyse(crypto):
    p_bin = f"{crypto}USDT"
    p_aff = f"{crypto}/USDT"
    print(f"\n[VIREVO] Connexion Binance pour {p_aff}...")
    time.sleep(1)
    prix, prs = obtenir_donnees_reelles(p_bin)
    if prix is not None:
        if prs > 55: dec, tend = "STRONG BUY 🚀", "BULLISH"
        elif prs < 45: dec, tend = "STRONG SELL 📉", "BEARISH"
        else: dec, tend = "HOLD / NEUTRAL ⚖️", "SIDEWAYS"
        print("\n=========================================")
        print(f"Asset        : {p_aff}")
        print(f"Real Price   : ${prix:,.2f}")
        print(f"Order Book   : {prs:.1f}% Pression Achat")
        print(f"Market Trend : {tend}")
        print(f"AI Decision  : {dec}")
        print("=========================================")
        print(f"\nPlanifier un achat DCA sur {p_aff} ?")
        chx = input("Validation humaine (oui/non) : ").strip().lower()
        if chx in ['oui', 'o']:
            print("[EXECUTION] Ordre préparé pour l'agent.")
        else:
            print("[ANNULATION] Proposition rejetée.")
def main():
    print("=========================================")
    print("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    print("=========================================")
    
    cryptos_valides = ["BNB", "BTC", "ETH", "SOL", "XRP", "ADA", "DOGE", "DOT", "MATIC", "LINK", "AVAX", "SHIB", "PEPE"]

    while True:
        cmd = input("\nUser: ").strip()
        if cmd.lower() == 'exit':
            print("Shutting down... Goodbye!")
            break
        if not cmd: continue
        
        txt = cmd.upper().replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
        mots = [m for m in txt.split(" ") if m]
        
        v_ok = any(calculer_ressemblance(m, "VIREVO") >= 55 for m in mots)
        a_ok = any(calculer_ressemblance(m, "ANALYSE") >= 55 or calculer_ressemblance(m, "ANALYZE") >= 55 for m in mots)
        
        cry = None
        for m in mots:
            if m in cryptos_valides:
                cry = m
                break

        if cry:
            if (not v_ok or not a_ok):
                print(f'[VIREVO] Actif {cry} détecté. Lancer l\'analyse sur Binance ?')
                rep = input("Confirmer (oui/non) : ").strip().lower()
                if rep in ['oui', 'o']:
                    executer_analyse(cry)
                continue
            executer_analyse(cry)
        else:
            mot_inconnu = mots[-1] if len(mots) > 0 else "votre saisie"
            if mot_inconnu in ["VIREVO", "ANALYSE", "ANALYZE"]:
                print("[VIREVO] Veuillez spécifier une crypto-monnaie valide (ex: bnb, btc, sol).")
            else:
                print(f'[VIREVO] Désolé, "{mot_inconnu}" n\'est pas une crypto-monnaie reconnue par mon système.')

main()