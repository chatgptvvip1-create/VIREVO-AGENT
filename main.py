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
            else: print("[ANNULATION] Proposition rejetée par l'opérateur.")
    else:
        if langue == "ZH": print("[VIREVO] 币安网络错误。请重试。")
        elif langue == "EN": print("[VIREVO] Binance network error. Please try again.")
        else: print("[VIREVO] Erreur réseau Binance. Réessayez.")
for m in mots:
            if m in cryptos_valides: cry = m; break
        if not cry:
            if "BTC" in cmd_upper: cry = "BTC"
            elif "ETH" in cmd_upper: cry = "ETH"
            elif "BNB" in cmd_upper: cry = "BNB"
            elif "SOL" in cmd_upper: cry = "SOL"
            elif "XRP" in cmd_upper: cry = "XRP"
            
        if (est_salut_fr or est_salut_en or langue == "ZH" and not cry) and not cry:
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
            if langue == "ZH": print(f'[VIREVO] 对不起，未能识别您输入的加密货币资产。请输入正确的缩写（例如: btc, bnb, sol）。')
            elif langue == "EN": print(f'[VIREVO] Sorry, "{mot_inconnu}" is not a recognized cryptocurrency.')
            else: print(f'[VIREVO] Désolé, "{mot_inconnu}" n\'est pas une crypto-monnaie reconnue par mon système.')

main()