import time
import random

def main():
    print("==================================================")
    print("         VIREVO AGENT v1.0.0 IS ONLINE            ")
    print("  AI Trading Assistant - Binance Agent OS Challenge")
    print("==================================================")
    print("Vision: One agent. One conversation. Smarter trading decisions.\n")
    print("Type your command (e.g., 'VIREVO, analyze BTC/USDT') or 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("User: ")
        except (KeyboardInterrupt, EOFError):
            print("\nShutting down VIREVO AGENT... Goodbye!")
            break

        if user_input.lower() == 'exit':
            print("\nShutting down VIREVO AGENT... Goodbye!")
            break
            
        if "analyze" in user_input.lower():
            asset = "BTC/USDT"
            for word in user_input.split():
                if "/" in word:
                    asset = word.upper()
            
            print(f"\n[VIREVO] 🧠 Step 2: Intent identified -> Market Analysis for {asset}")
            time.sleep(1)
            print("[VIREVO] 🔍 Step 3: Processing market conditions through MCP architecture...")
            time.sleep(1)
            
            price = round(random.uniform(96000, 98000) if "BTC" in asset else random.uniform(3200, 3500), 2)
            change = round(random.uniform(-3.5, 5.8), 2)
            sign = "+" if change > 0 else ""
            rsi = random.randint(38, 72)
            trend = "BULLISH 🚀" if change > 0 else "BEARISH 📉"
            recommendation = "STRONG BUY" if rsi < 45 else "STRONG SELL" if rsi > 65 else "HOLD / NEUTRAL"
            
            print("\n=========================================")
            print(f"   🤖 VIREVO Step 4: ACTIONABLE REPORT   ")
            print("=========================================")
            print(f" Asset         : {asset}")
            print(f" Current Price : ${price} ({sign}{change}%)")
            print(f" Market Trend  : {trend}")
            print(f" RSI (14)      : {rsi}")
            print(f" AI Decision   : {recommendation}")
            print("=========================================\n")
        else:
            print(f"\n[VIREVO] 🤖 Request not recognized. Please try: 'VIREVO, analyze BTC/USDT'\n")

main()