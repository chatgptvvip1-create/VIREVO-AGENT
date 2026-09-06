import time
import random
from binance.spot import Spot as Client

saluts_fr = ["BONJOUR", "SALUT", "COUCOU"]
saluts_en = ["HELLO", "HI", "HEY"]
mots_merci_quitter = ["MERCI", "THANKS", "EXIT", "QUIT", "SORTIE"]
mots_anglais = ["CHECK", "ANALYZE", "LOOK", "PRICE", "PLEASE", "HI", "HELLO", "THANKS", "QUIT", "EXIT"]

citations_fr = [
    "Jesse Livermore : 'L'argent se fait en attendant, pas en tradant.'",
    "Warren Buffett : 'La regle n°1 est de ne jamais perdre d'argent.'",
    "George Soros : 'Il faut savoir combien on gagne quand on a raison.'",
    "Benjamin Graham : 'Le pire ennemi du trader est probablement lui-meme.'"
]
citations_en = [
    "Jesse Livermore: 'Money is made by sitting, not by trading.'",
    "Warren Buffett: 'Rule No. 1 is never lose money.'",
    "George Soros: 'It's how much money you make when you're right.'",
    "Benjamin Graham: 'The investor's chief problem is even his worst enemy.'"
]
citations_zh = [
    "杰西·利弗莫尔 : '钱是坐着赚来的。'",
    "沃伦·巴菲特 : '第一条规则是永远不要亏钱。'",
    "乔治·索罗斯 : '重要的是当你正确时你赢了多少钱。'",
    "本杰明·格雷厄姆 : '交易者最大的敌人往往是他自己。'"
]

def recuperer_toutes_les_cryptos():
    try:
        client = Client()
        infos = client.exchange_info()
        cryptos = set()
        for s in infos['symbols']:
            if s['status'] == 'TRADING' and s['quoteAsset'] == 'USDT':
                cryptos.add(s['baseAsset'].upper())
        return list(cryptos)
    except Exception as e:
        print(f"[PRE-LOAD] Erreur liste Binance : {e}")
        return ["BNB", "BTC", "ETH", "SOL", "XRP", "PEPE", "DOGE"]
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
        tot_a = sum(float(a[0]) for a in depth['asks'])
        tot_v = sum(float(b[0]) for b in depth['bids'])
        pression = (tot_a / (tot_a + tot_v)) * 100
        return prix_reel, pression
    except Exception as e:
        print(f"\n[ERREUR] Binance : {e}")
        return None, None

def executer_analyse(crypto, langue):
    p_bin = f"{crypto}USDT"
    p_aff = f"{crypto}/USDT"
    if langue == "ZH": print(f"\n[VIREVO] 获取 {p_aff} 实时 data...")
    elif langue == "EN": print(f"\n[VIREVO] Connecting for {p_aff}...")
    else: print(f"\n[VIREVO] Connexion pour {p_aff}...")
    time.sleep(0.5)
    prix, prs = obtenir_donnees_reelles(p_bin)
    if prix is not None:
        if prs > 55: dec, tend = "STRONG BUY 🚀", "BULLISH"
        elif prs < 45: dec, tend = "STRONG SELL 📉", "BEARISH"
        else: dec, tend = "HOLD / NEUTRAL ⚖️", "SIDEWAYS"
        print("\n=========================================")
        if langue == "ZH":
            print(f"资产名称     : {p_aff}\n当前价格     : ${prix:,.2f}\nAI 决策      : {dec}")
        elif langue == "EN":
            print(f"Asset        : {p_aff}\nReal Price   : ${prix:,.2f}\nAI Decision  : {dec}")
        else:
            print(f"Actif        : {p_aff}\nPrix Reel    : ${prix:,.2f}\nDecision IA  : {dec}")
        print("=========================================")
    else:
        print("[VIREVO] Erreur reseau Binance. Reessayez.")
def main():
    print("=========================================")
    print("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    print("=========================================")
    print("[VIREVO] Synchronisation avec Binance...")
    cryptos_valides = recuperer_toutes_les_cryptos()
    print(f"[VIREVO] Succes ! {len(cryptos_valides)} actifs synchronises.")
    print("\n[VIREVO] Initialisation des flux...")
    for coin in ["BTC", "ETH", "BNB"]:
        if coin in cryptos_valides:
            executer_analyse(coin, "FR")
            time.sleep(0.5)

    while True:
        cmd = input("\nUser: ").strip()
        if not cmd: continue
        cmd_upper = cmd.upper()
        langue = "FR"
        est_chinois = any(ord(c) > 127 for c in cmd) or "ZH" in cmd_upper or "CHINESE" in cmd_upper
        if est_chinois: langue = "ZH"
        else:
            txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
            mots = [m for m in txt.split(" ") if m]
            if sum(1 for m in mots if m in mots_anglais) > 0: langue = "EN"
        txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
        mots = [m for m in txt.split(" ") if m]
        
        est_fin = any(any(calculer_ressemblance(m, f) >= 70 for f in mots_merci_quitter) for m in mots)
        if est_fin:
            if langue == "ZH": print(f"\n[VIREVO] 感谢使用！🍀\n[AI 金句] {random.choice(citations_zh)}\n再见！")
            elif langue == "EN": print(f"\n[VIREVO] Thank you! 🍀\n[AI Quote] {random.choice(citations_en)}\nGoodbye!")
            else: print(f"\n[VIREVO] Merci d'avoir utilise mon systeme ! 🍀\n[Citation] {random.choice(citations_fr)}\nAu revoir !")
            break
            
        est_salut_fr = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_fr) for m in mots)
        est_salut_en = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_en) for m in mots)
        v_ok = any(calculer_ressemblance(m, "VIREVO") >= 55 for m in mots) or "VIREVO" in cmd_upper or langue == "ZH"
        a_ok = any(calculer_ressemblance(m, "ANALYSE") >= 55 or calculer_ressemblance(m, "ANALYZE") >= 55 for m in mots) or langue == "ZH"
        
        cry = None
        for m in mots:
            if m in cryptos_valides: cry = m; break
        if not cry:
            for m in mots:
                if f"{m}USDT" in cryptos_valides or m in ["BTC", "ETH", "BNB", "SOL", "XRP", "DOGE"]:
                    cry = m; break

        if (est_salut_fr or est_salut_en or (langue == "ZH" and not cry)) and not cry:
            if langue == "ZH": print("[VIREVO] 你好！我是您的助手。今天您想分析哪种货币？")
            elif langue == "EN": print("[VIREVO] Hello! I am your AI assistant. Which crypto to analyze?")
            else: print("[VIREVO] Bonjour ! Je suis votre assistant. Quelle crypto analyser aujourd'hui ?")
            continue
        if cry:
            if (not v_ok or not a_ok) and langue != "ZH":
                if langue == "EN":
                    print(f"[VIREVO] Crypto {cry} detected. Analyze on Binance?")
                    rep = input("Confirm (yes/no) : ").strip().lower()
                    if rep in ['yes', 'y']: executer_analyse(cry, langue)
                else:
                    print(f"[VIREVO] Crypto {cry} detectee. Lancer l'analyse ?")
                    rep = input("Confirmer (oui/non) : ").strip().lower()
                    if rep in ['oui', 'o']: executer_analyse(cry, langue)
                continue
            executer_analyse(cry, langue)
        else:
            mot_inconnu = mots[-1] if len(mots) > 0 else "saisie"
            if langue == "ZH": print(f'[VIREVO] 对不起，未能识别您输入的资产。')
            elif langue == "EN": print(f'[VIREVO] Sorry, "{mot_inconnu}" is not recognized.')
            else: print(f'[VIREVO] Desole, "{mot_inconnu}" n\'est pas reconnu par mon systeme.')

main()
    