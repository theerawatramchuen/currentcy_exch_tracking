### Deepseek Prompt
Pls give me python code to convert 17,000 USD, 200 SGD and 5,000 CNY sum to THB in real time. <br>
Pls modify the code to for endless loop and printout the result every hour with timestamp. Incase connection error pls do not print anything just keep it quite.
### Installation
```
pip install yfinance
```
```
import yfinance as yf
from datetime import datetime
import time

def convert_to_thb():
    while True:
        try:
            # Get current timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Fetch real-time exchange rates
            usd_rate = yf.Ticker("USDTHB=X").fast_info.last_price
            sgd_rate = yf.Ticker("SGDTHB=X").fast_info.last_price
            cny_rate = yf.Ticker("CNYTHB=X").fast_info.last_price
            
            # Calculate only if all rates are available
            if all([usd_rate, sgd_rate, cny_rate]):
                total_thb = (17000 * usd_rate) + (200 * sgd_rate) + (5000 * cny_rate)
                print(f"{current_time} - Total in THB: {total_thb:.2f}")
            
        except:
            # Silent handling for any errors
            pass
        
        # Wait for 1 hour before next update
        time.sleep(3600)

if __name__ == "__main__":
    convert_to_thb()
```
