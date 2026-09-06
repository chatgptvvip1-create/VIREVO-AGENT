import time
import random

def obtenir_donnees_reelles(paire):
    try:
        client = Client()
        ticker = client.ticker_price(paire)
        prix_reel = float(ticker['price'])
        depth = client.depth(paire, limit=10)
        tot_a = sum(float(a) for a in depth['asks'])
        tot_v = sum(float(b) for b in depth['bids'])
        pression = (tot_a / (tot_a + tot_v)) * 100 if (tot_a + tot_v) > 0 else 50
        return prix_reel, pression
    except Exception as e:
        log_action(f"\n[ERREUR] Binance : {e}")
        return None, None

def executer_analyse(crypto, langue):
    p_bin = f"{crypto}USDT"
    p_aff = f"{crypto}/USDT"
    if langue == "ZH": log_action(f"\n[VIREVO] 获取 {p_aff} 实时数据...")
    elif langue == "EN": log_action(f"\n[VIREVO] Connecting for {p_aff}...")
    else: log_action(f"\n[VIREVO] Connexion Binance pour {p_aff}...")
    time.sleep(0.5)
    prix, prs = obtenir_donnees_reelles(p_bin)
    if prix is not None:
        if prs > 55: dec, tend = "STRONG BUY 🚀", "BULLISH"
        elif prs < 45: dec, tend = "STRONG SELL 📉", "BEARISH"
        else: dec, tend = "HOLD / NEUTRAL ⚖️", "SIDEWAYS"
        log_action("\n=========================================")
        if langue == "ZH":
            log_action(f"Asset        : {p_aff}\nReal Price   : ${prix:,.2f}\nOrder Book   : {prs:.1f}% 买盘压力\nMarket Trend : {tend}\nAI Decision  : {dec}")
            log_action("=========================================\n是否为智能代理安排定投(DCA)买入订单？")
            chx = input("人工授权验证 (yes/no/是/否) : ").strip().lower()
            if chx in ['yes', 'y', '是', 'sh', 'shi']: log_action("[执行] 订单已为自动交易子账户准备就绪。")
            else: log_action("[取消] 操作员已拒绝此交易提案。")
        elif langue == "EN":
            log_action(f"Asset        : {p_aff}\nReal Price   : ${prix:,.2f}\nOrder Book   : {prs:.1f}% Buy Pressure\nMarket Trend : {tend}\nAI Decision  : {dec}")
            log_action(f"=========================================\nSchedule a DCA buy order for {p_aff}?")
            chx = input("Human validation (yes/no) : ").strip().lower()
            if chx in ['yes', 'y', 'oui', 'o']: log_action("[EXECUTION] Order prepared for Agentic sub-account.")
            else: log_action("[CANCELLATION] Proposal rejected by operator.")
        else:
            log_action(f"Asset        : {p_aff}\nReal Price   : ${prix:,.2f}\nOrder Book   : {prs:.1f}% Pression Achat\nMarket Trend : {tend}\nAI Decision  : {dec}")
            log_action(f"=========================================\nPlanifier un achat DCA sur {p_aff} ?")
            chx = input("Validation humaine (oui/non) : ").strip().lower()
            if chx in ['oui', 'o', 'yes', 'y']: log_action("[EXECUTION] Ordre prepare pour le sous-compte Agentic.")
            else: log_action("[ANNULATION] Proposition rejetee par l'operateur.")
        log_action("=========================================")
    else:
        log_action("[VIREVO] Erreur reseau Binance. Réessayez.")
        def main():
    log_action("=========================================")
    log_action("      VIREVO AGENT v1.0.0 IS ONLINE      ")
    log_action("=========================================")
    log_action("[VIREVO] Synchronisation avec Binance...")
    cryptos_valides = recuperer_toutes_les_cryptos()
    log_action(f"[VIREVO] Succes ! {len(cryptos_valides)} actifs synchronises.")
    log_action("\n[VIREVO] Initialisation des flux...")
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
            if langue == "ZH": log_action(f"\n[VIREVO] 感谢使用！🍀\n[AI 金句] {random.choice(citations_zh)}\n正在关闭... 再见！")
            elif langue == "EN": log_action(f"\n[VIREVO] Thank you! 🍀\n[AI Quote] {random.choice(citations_en)}\nGoodbye!")
            else: log_action(f"\n[VIREVO] Merci d'avoir utilise mon systeme ! 🍀\n[Citation] {random.choice(citations_fr)}\nAu revoir !")
            break
            est_salut_fr = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_fr) for m in mots)
        est_salut_en = any(any(calculer_ressemblance(m, s) >= 70 for s in saluts_en) for m in mots)
        v_ok = any(calculer_ressemblance(m, "VIREVO") >= 55 for m in mots) or "VIREVO" in cmd_upper or langue == "ZH"
        a_ok = any(calculer_ressemblance(m, "ANALYSE") >= 55 or calculer_ressemblance(m, "ANALYZE") >= 55 for m in mots) or langue == "ZH"
        
        cry = None
        for m in mots:
            if m in cryptos_valides: 
                cry = m
                break
        if not cry:
            for m in mots:
                if f"{m}USDT" in cryptos_valides or m in ["BTC", "ETH", "BNB", "SOL", "XRP", "DOGE"]:
                    cry = m
                    break

        if (est_salut_fr or est_salut_en or (langue == "ZH" and not cry)) and not cry:
            if langue == "ZH": log_action("[VIREVO] 你好！我是您的助手。今天您想分析哪种货币？")
            elif langue == "EN": log_action("[VIREVO] Hello! I am your AI assistant. Which crypto to analyze?")
            else: log_action("[VIREVO] Bonjour ! Je suis votre assistant. Quelle crypto analyser aujourd'hui ?")
            continue
            
        if cry:
            if (not v_ok or not a_ok) and langue != "ZH":
                if langue == "EN":
                    log_action(f"[VIREVO] Crypto {cry} detected. Analyze on Binance?")
                    rep = input("Confirm (yes/no) : ").strip().lower()
                    if rep in ['yes', 'y']: executer_analyse(cry, langue)
                else:
                    log_action(f"[VIREVO] Crypto {cry} detectee. Lancer l'analyse ?")
                    rep = input("Confirmer (oui/non) : ").strip().lower()
                    if rep in ['oui', 'o']: executer_analyse(cry, langue)
                continue
            executer_analyse(cry, langue)
        else:
            mot_inconnu = mots[-1] if len(mots) > 0 else "saisie"
            if langue == "ZH": log_action(f'[VIREVO] 对不起，未能识别您输入的资产。')
            elif langue == "EN": log_action(f'[VIREVO] Sorry, "{mot_inconnu}" is not recognized.')
            else: log_action(f'[VIREVO] Desole, "{mot_inconnu}" n\'est pas reconnu par mon systeme.')

if name == "main":
    main() 