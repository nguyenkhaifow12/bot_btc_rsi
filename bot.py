import requests
import time

TOKEN = "7902677031:AAF8KfXS1nkjBSj4ICsJu0Lo1J-nGrAKezc"
CHAT_ID = "6005841734"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

def get_rsi():  # Ví dụ tạm thời, bạn thay bằng real data
    import random
    return random.uniform(20, 80)

def main_loop():
    while True:
        rsi = get_rsi()
        print(f"RSI hiện tại: {rsi:.2f}")
        if rsi < 30:
            send_telegram(f"⚠️ RSI thấp: {rsi:.2f} - Cơ hội mua vào?")
        elif rsi > 70:
            send_telegram(f"⚠️ RSI cao: {rsi:.2f} - Cảnh báo bán ra?")
        time.sleep(300)  # 5 phút chạy lại

if __name__ == "__main__":
    main_loop()
