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
        print(f"\n[ERROR/ERREUR/错误] Binance : {e}")
        return None, None
def executer_analyse(crypto, langue):
    p_bin = f"{crypto}USDT"
    p_aff = f"{crypto}/USDT"
    if langue == "ZH": print(f"\n[VIREVO] 正在连接Binance获取 {p_aff} 的实时数据...")
    elif langue == "EN": print(f"\n[VIREVO] Connecting to Binance for {p_aff}...")
    else: print(f"\n[VIREVO] Connexion Binance pour {p_aff}...")
    time.sleep(1)
    prix, prs = obtenir_donnees_reelles(p_bin)
    if prix is not None:
        if prs > 55:
            dec = "STRONG BUY 🚀 (强烈建议买入)" if langue == "ZH" else ("STRONG BUY 🚀" if langue == "EN" else "STRONG BUY 🚀 (Forte pression acheteuse)")
            tend = "BULLISH"
        elif prs < 45:
            dec = "STRONG SELL 📉 (强烈建议卖出)" if langue == "ZH" else ("STRONG SELL 📉" if langue == "EN" else "STRONG SELL 📉 (Forte pression vendeuse)")
            tend = "BEARISH"
        else:
            dec = "HOLD / NEUTRAL ⚖️ (市场观望)" if langue == "ZH" else "HOLD / NEUTRAL ⚖️"
            tend = "SIDEWAYS"
        print("\n=========================================")
        if langue == "ZH":
            print("    VIREVO 步骤 4 : 可执行交易报告       ")
            print("=========================================")
            print(f"资产名称     : {p_aff}")
            print(f"当前实时价格 : ${prix:,.2f}")
            print(f"订单薄分析   : {prs:.1f}% 买盘压力")
            print(f"市场趋势     : {tend}")
            print(f"AI 交易决策  : {dec}")
            print("=========================================")
            print(f"\n是否为 {p_aff} 安排定投(DCA)买入订单？")
            chx = input("人工授权验证 (yes/no/是/否) : ").strip().lower()
            if chx in ['yes', 'y', 'oui', 'o', '是', 'sh', 'shi']: print("[执行] 订单已为自动交易子账户准备就绪。")
            else: print("[取消] 操作员已拒绝此交易提案。")
        elif langue == "EN":
            print("    VIREVO Step 4: ACTIONABLE REPORT     ")
            print("=========================================")
            print(f"Asset        : {p_aff}")
            print(f"Real Price   : ${prix:,.2f}")
            print(f"Order Book   : {prs:.1f}% Buy Pressure")
            print(f"Market Trend : {tend}")
            print(f"AI Decision  : {dec}")
            print("=========================================")
            print(f"\nSchedule a DCA buy order for {p_aff}?")
            chx = input("Human validation (yes/no) : ").strip().lower()
            if chx in ['yes', 'y', 'oui', 'o']: print("[EXECUTION] Order prepared for Agentic sub-account.")
            else: print("[CANCELLATION] Proposal rejected by operator.")
        else:
            print("    VIREVO Étape 4 : RAPPORT D'ACTION    ")
            print("=========================================")
            print(f"Actif        : {p_aff}")
            print(f"Prix Réel    : ${prix:,.2f}")
            print(f"Order Book   : {prs:.1f}% Pression Achat")
            print(f"Tendance     : {tend}")
            print(f"Décision IA  : {dec}")
            print("=========================================")
            print(f"\nPlanifier un achat DCA sur {p_aff} ?")
            chx = input("Validation humaine (oui/non) : ").strip().lower()
            if chx in ['oui', 'o', 'yes', 'y']: print("[EXECUTION] Ordre préparé pour le sous-compte Agentic.")
            else: print("[ANNULATION] Proposition rejected par l'opérateur.")
    else:
        if langue == "ZH": print("[VIREVO] 币安网络错误。请重试。")
        elif langue == "EN": print("[VIREVO] Binance network error. Please try again.")
        else: print("[VIREVO] Erreur réseau Binance. Réessayez.")
def main():
    print("=========================================")
    print("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    print("=========================================")
    cryptos_valides = ["BNB", "BTC", "ETH", "SOL", "XRP", "ADA", "DOGE", "DOT", "MATIC", "LINK", "AVAX", "SHIB", "PEPE"]
    saluts_fr = ["BONJOUR", "SALUT", "COUCOU"]
    saluts_en = ["HELLO", "HI", "HEY", "GOOD MORNING"]
    mots_merci_quitter = ["MERCI", "THANKS", "THANK", "THANKYOU", "EXIT", "QUIT", "QUITTER", "QUITER", "SORTIE", "SORTIR", "FERMER", "CLOSE"]
    mots_anglais = ["CHECK", "ANALYZE", "LOOK", "PRICE", "PLEASE", "YES", "NO", "HI", "HELLO", "THANKS", "QUIT", "EXIT"]

    citations_fr = [
        "Jesse Livermore : 'L'argent se fait en attendant, pas en tradant.'",
        "Warren Buffett : 'La règle n°1 est de ne jamais perdre d'argent. La règle n°2 est de ne jamais oublier la règle n°1.'",
        "George Soros : 'Ce qui importe n'est pas d'avoir raison ou tort, mais de savoir combien d'argent on gagne quand on a raison.'"
    ]
    citations_en = [
        "Jesse Livermore: 'Money is made by sitting, not by trading.'",
        "Warren Buffett: 'Rule No. 1 is never lose money. Rule No. 2 is never forget Rule No. 1.'",
        "George Soros: 'It's not whether you're right or wrong, but how much money you make when you're right.'"
    ]
    citations_zh = [
        "杰西·利弗莫尔 : '钱是坐着赚来的，而不是靠频繁交易赚来的。'",
        "沃伦·巴菲特 : '第一条规则 is 永远不要亏钱。第二条规则 is 永远不要忘记第一条。'",
        "乔治·索罗斯 : '对与错并不重要，重要的是当你正确时你赢了多少钱。'"
    ]
while True:
        cmd = input("\nUser: ").strip()
        if not cmd: continue
        cmd_upper = cmd.upper()
        langue = "FR"
        est_chinois = any(ord(c) > 127 for c in cmd) or "ZH" in cmd_upper or "CHINESE" in cmd_upper or "NIHAO" in cmd_upper
        if est_chinois: langue = "ZH"
        else:
            txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
            mots = [m for m in txt.split(" ") if m]
            if sum(1 for m in mots if m in mots_anglais) > 0: langue = "EN"
        txt = cmd_upper.replace(",", " ").replace(";", " ").replace("/", " ").replace(".", " ")
        mots = [m for m in txt.split(" ") if m]
        est_fin = any(any(calculer_ressemblance(m, f) >= 70 for f in mots_merci_quitter) for m in mots) or (langue == "ZH" and any(x in cmd_upper for x in ["XIXI", "EXIT", "QUIT", "BYE"]))
        if est_fin:
            if langue == "ZH": print(f"\n[VIREVO] 感谢您的使用！🍀\n[智能交易金句] {random.choice(citations_zh)}\n正在关闭... 再见！")
            elif langue == "EN": print(f"\n[VIREVO] Thank you! 🍀\n[AI Trading Quote] {random.choice(citations_en)}\nShutting down... Goodbye!")
            else: print(f"\n[VIREVO] Merci ! 🍀\n[Citation Trader] {random.choice(citations_fr)}\nArrêt en cours... Au revoir !")
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
            if langue == "ZH": print("[VIREVO] 你好！我是您的智能AI助手。今天您想分析哪种加密货币？")
            elif langue == "EN": print("[VIREVO] Hello! I am your AI assistant. Which crypto would you like to analyze today?")
            else: print("[VIREVO] Bonjour ! Je suis votre assistant. Quelle crypto souhaitez-vous analyser aujourd'hui ?")
            continue
        if cry:
            if (not v_ok or not a_ok) and langue != "ZH":
                if langue == "EN":
                    print(f"[VIREVO] Asset {cry} detected. Launch analysis on Binance?")
                    rep = input("Confirm (yes/no) : ").strip().lower()
                    if rep in ['yes', 'y']: executer_analyse(cry, langue)
                else:
                    print(f"[VIREVO] Actif {cry} détecté. Lancer l'analyse sur Binance ?")
                    rep = input("Confirmer (oui/non) : ").strip().lower()
                    if rep in ['oui', 'o']: executer_analyse(cry, langue)
                continue
            executer_analyse(cry, langue)
        else:
            mot_inconnu = mots[-1] if len(mots) > 0 else "saisie"
            if langue == "ZH": print(f'[VIREVO] 对不起，未能识别您输入的加密货币资产。')
            elif langue == "EN": print(f'[VIREVO] Sorry, "{mot_inconnu}" is not a recognized cryptocurrency.')
            else: print(f'[VIREVO] Désolé, "{mot_inconnu}" n\'est pas une crypto-monnaie reconnue par mon système.')

main()