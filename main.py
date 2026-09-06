import time
import random
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
def executer_analyse(crypto, langue):
    p_bin = f"{crypto}USDT"
    p_aff = f"{crypto}/USDT"
    if langue == "ZH":
        print(f"\n[VIREVO] 获取 {p_aff} 实时数据...")
    elif langue == "EN":
        print(f"\n[VIREVO] Connecting for {p_aff}...")
    else:
        print(f"\n[VIREVO] Connexion pour {p_aff}...")
    time.sleep(1)
    prix, prs = obtenir_donnees_reelles(p_bin)
    if prix is not None:
        if prs > 55:
            dec = "STRONG BUY 🚀"
            tend = "BULLISH"
        elif prs < 45:
            dec = "STRONG SELL 📉"
            tend = "BEARISH"
        else:
            dec = "HOLD / NEUTRAL ⚖️"
            tend = "SIDEWAYS"
        print("\n=========================================")
        if langue == "ZH":
            print("    VIREVO 步骤 4 : 交易报告       ")
            print("=========================================")
            print(f"资产名称     : {p_aff}")
            print(f"当前价格     : ${prix:,.2f}")
            print(f"订单薄分析   : {prs:.1f}% 买盘")
            print(f"AI 决策      : {dec}")
            print("=========================================")
            chx = input("人工验证 (yes/no/是/否) : ").strip().lower()
            if chx in ['yes', 'y', 'oui', 'o', '是']:
                print("[执行] 订单已就绪。")
            else:
                print("[取消] 操作员已拒绝。")
        elif langue == "EN":
            print("    VIREVO Step 4: REPORT     ")
            print("=========================================")
            print(f"Asset        : {p_aff}")
            print(f"Real Price   : ${prix:,.2f}")
            print(f"AI Decision  : {dec}")
            print("=========================================")
            chx = input("Human validation (yes/no) : ").strip().lower()
            if chx in ['yes', 'y', 'oui', 'o']:
                print("[EXECUTION] Order prepared.")
            else:
                print("[CANCELLATION] Rejected by operator.")
        else:
            print("    VIREVO Étape 4 : RAPPORT    ")
            print("=========================================")
            print(f"Actif        : {p_aff}")
            print(f"Prix Réel    : ${prix:,.2f}")
            print(f"Décision IA  : {dec}")
            print("=========================================")
            chx = input("Validation humaine (oui/non) : ").strip().lower()
            if chx in ['oui', 'o', 'yes', 'y']:
                print("[EXECUTION] Ordre préparé.")
            else:
                print("[ANNULATION] Rejetée par l'opérateur.")
    else:
        print("[VIREVO] Erreur réseau Binance. Réessayez.")
def main():
    print("=========================================")
    print("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    print("=========================================")
    cryptos_valides = ["BNB", "BTC", "ETH", "SOL", "XRP", "PEPE"]
    saluts_fr = ["BONJOUR", "SALUT", "COUCOU"]
    saluts_en = ["HELLO", "HI", "HEY"]
    mots_merci_quitter = ["MERCI", "THANKS", "EXIT", "QUIT", "SORTIE"]
    mots_anglais = ["CHECK", "ANALYZE", "LOOK", "PRICE", "PLEASE", "HI", "HELLO", "THANKS", "QUIT", "EXIT"]

    citations_fr = [
        "Jesse Livermore : 'L'argent se fait en attendant.'",
        "Warren Buffett : 'La règle n°1 est de ne jamais perdre d'argent.'",
        "George Soros : 'Ce qui importe est de savoir combien on gagne.'"
    ]
    citations_en = [
        "Jesse Livermore: 'Money is made by sitting.'",
        "Warren Buffett: 'Rule No. 1 is never lose money.'",
        "George Soros: 'It's how much money you make when you're right.'"
    ]
    citations_zh = [
        "杰西·利弗莫尔 : '钱是坐着赚来的。'",
        "沃伦·巴菲特 : '第一条规则是永远不要亏钱。'",
        "乔治·索罗斯 : '重要的是当你正确时你赢了多少钱。'"
    ]
while True:
        cmd = input("\nUser: ").strip()
        if not cmd: continue
        cmd_upper = cmd.upper()
        
        langue = "FR"
        est_chinois = any(ord(c) > 127 for c in cmd) or "ZH" in cmd_upper or "CHINESE" in cmd_upper
        if est_chinois:
            langue = "ZH"
        else:
            txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
            mots = [m for m in txt.split(" ") if m]
            if sum(1 for m in mots if m in mots_anglais) > 0:
                langue = "EN"
        
        txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
        mots = [m for m in txt.split(" ") if m]
        
        est_fin = any(any(calculer_ressemblance(m, f) >= 70 for f in mots_merci_quitter) for m in mots)
        if est_fin:
            if langue == "ZH":
                print(f"\n[VIREVO] 感谢使用！🍀\n金句: {random.choice(citations_zh)}\n再见！")
            elif langue == "EN":
                print(f"\n[VIREVO] Thank you! 🍀\nQuote: {random.choice(citations_en)}\nGoodbye!")
            else:
                print(f"\n[VIREVO] Merci ! 🍀\nCitation: {random.choice(citations_fr)}\nAu revoir !")
            break

        est_salut_fr = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_fr) for m in mots)
        est_salut_en = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_en) for m in mots)
        v_ok = any(calculer_ressemblance(m, "VIREVO") >= 55 for m in mots) or "VIREVO" in cmd_upper or langue == "ZH"
        a_ok = any(calculer_ressemblance(m, "ANALYSE") >= 55 or calculer_ressemblance(m, "ANALYZE") >= 55 for m in mots) or langue == "ZH"
        
        cry = None
        for m in mots:
            if m in cryptos_valides: cry = m; break
        if not cry:
            if "BTC" in cmd_upper: cry = "BTC"
            elif "ETH" in cmd_upper: cry = "ETH"
            elif "BNB" in cmd_upper: cry = "BNB"
            elif "SOL" in cmd_upper: cry = "SOL"
            elif "XRP" in cmd_upper: cry = "XRP"
            
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
                    print(f"[VIREVO] Crypto {cry} détectée. Lancer l'analyse ?")
                    rep = input("Confirmer (oui/non) : ").strip().lower()
                    if rep in ['oui', 'o']: executer_analyse(cry, langue)
                continue
            executer_analyse(cry, langue)
        else:
            mot_inconnu = mots[-1] if len(mots) > 0 else "saisie"
            if langue == "ZH": print(f'[VIREVO] 对不起，未能识别您输入的资产。')
            elif langue == "EN": print(f'[VIREVO] Sorry, "{mot_inconnu}" is not recognized.')
            else: print(f'[VIREVO] Désolé, "{mot_inconnu}" n\'est pas reconnu par mon système.')

main()