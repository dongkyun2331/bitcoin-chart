import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import yfinance as yf

def fetch_bitcoin_data():
    # 비트코인 가격 데이터 가져오기
    btc_data = yf.download('BTC-USD', start='2022-01-01', end='2023-01-01')

    # 차트 업데이트
    update_chart(btc_data)

def update_chart(data):
    ax.clear()
    ax.plot(data.index, data['Close'])
    ax.set_title('Bitcoin Price Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    canvas.draw()

# Tkinter 앱 생성
root = tk.Tk()
root.title('Bitcoin Price Viewer')

# 데이터 가져오기 버튼
fetch_button = tk.Button(root, text='Fetch Bitcoin Data', command=fetch_bitcoin_data)
fetch_button.pack(pady=10)

# Matplotlib 차트를 위한 Figure 및 Canvas
fig = Figure(figsize=(8, 6))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 초기 차트 표시
fetch_bitcoin_data()

# 앱 실행
root.mainloop()
