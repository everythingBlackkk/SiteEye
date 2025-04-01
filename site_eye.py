import os
import cv2
import time
import hashlib
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound

init(autoreset=True)

class SiteMonitor:
    def __init__(self, url, wait_time=5):
        self.url = url
        self.wait_time = wait_time
        self.screenshot_path = "screenshots/"
        os.makedirs(self.screenshot_path, exist_ok=True)
        
        # Chrome settings
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Install and run Chrome
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def take_full_screenshot(self):
        try:
            self.driver.get(self.url)
            self.driver.refresh()
            time.sleep(self.wait_time)

            screenshot_file = os.path.join(self.screenshot_path, f"screenshot_{int(time.time())}.png")
            success = self.driver.save_screenshot(screenshot_file)
            
            return screenshot_file if success else None
        except Exception as e:
            print(Fore.RED + f"Error taking screenshot: {e}")
            return None

    def compare_images(self, img1_path, img2_path):
        try:
            if not os.path.exists(img1_path) or not os.path.exists(img2_path):
                print(Fore.RED + "Error: One of the images does not exist")
                return 0

            img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

            if img1 is None or img2 is None:
                print(Fore.RED + "Error: Failed to load images")
                return 0

            diff = cv2.absdiff(img1, img2)
            diff_percentage = (cv2.countNonZero(diff) * 100) / diff.size
            
            return diff_percentage
        except Exception as e:
            print(Fore.RED + f"Error comparing images: {e}")
            return 0

    def monitor_site(self, interval=60, diff_threshold=0.01):
        previous_screenshot = None
        
        try:
            while True:
                current_screenshot = self.take_full_screenshot()
                if not current_screenshot:
                    continue

                if previous_screenshot:
                    diff_percentage = self.compare_images(previous_screenshot, current_screenshot)

                    if diff_percentage > diff_threshold:
                        print(Fore.RED + f"[!] Change detected! Difference: {diff_percentage:.2f}%")
                        playsound("alert.mp3")
                    else:
                        print(Fore.GREEN + f"[+] No significant changes. Difference: {diff_percentage:.2f}%")
                else:
                    print(Fore.YELLOW + ">> First screenshot captured!")
                
                previous_screenshot = current_screenshot
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print(Fore.LIGHTCYAN_EX + "Closing...")
        finally:
            self.driver.quit()

def main():
    print(Fore.LIGHTGREEN_EX + """
               ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
    """)
    
    website_link = input("[+] Enter website URL: ")
    wait_time = int(input("[+] Enter wait time in seconds: "))
    interval = int(input("[+] Enter monitoring interval in seconds: "))

    monitor = SiteMonitor(website_link, wait_time)
    monitor.monitor_site(interval)

if __name__ == "__main__":
    main()
