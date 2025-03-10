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
                total_thb = (17000 * usd_rate) + (0 * sgd_rate) + (0 * cny_rate)
                print(f"{current_time} - Total in THB: {total_thb:.2f} - USD-THB: {usd_rate:.4f}")
            
        except:
            # Silent handling for any errors
            pass
        
        # Wait for 1 hour before next update
        time.sleep(900)

if __name__ == "__main__":
    convert_to_thb()