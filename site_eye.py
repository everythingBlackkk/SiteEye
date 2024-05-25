import os  # Control in OS like Make Dir
import cv2  # OpenCv
import time  # Stop Tool in some time
import pyfiglet  # Create Ascii Text
from colorama import Fore, init  # color text
import yagmail  # send Gmail
from selenium import webdriver  # Control Web App
from selenium.common.exceptions import WebDriverException

init(autoreset=True)

text = """
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
    """
print(Fore.LIGHTGREEN_EX + text)
print(Fore.LIGHTYELLOW_EX + "    # Site Eye , Coded By Yassin Abd-elrazik ")
print(Fore.LIGHTYELLOW_EX + "          GitHub : everythingBlackkk")

def take_full_screenshot(driver, url, wait_time, screenshot_path):
    try:
        driver.get(url)
        driver.refresh()
        time.sleep(wait_time)

        total_width = driver.execute_script("return document.body.scrollWidth")
        total_height = driver.execute_script("return document.body.scrollHeight")

        driver.set_window_size(total_width, total_height)
        time.sleep(wait_time)

        screenshot_file = os.path.join(screenshot_path, "current_screenshot.png")
        success = driver.save_screenshot(screenshot_file)
        if success:
            print(Fore.GREEN + "Screenshot taken successfully!")
            return screenshot_file
        else:
            print(Fore.RED + "Error: Failed to save screenshot.")
            return None
    except WebDriverException as e:
        print(Fore.RED + "Error: Failed to take screenshot:", e)
        return None

def compare_images(img1_path, img2_path):
    try:
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        if img1 is None or img2 is None:
            print(Fore.RED + "Error: One of the images could not be loaded.")
            return 0

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(gray1, None)
        kp2, des2 = sift.detectAndCompute(gray2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        match_count = len(good)

        if match_count > 0:
            similarity = match_count / max(len(kp1), len(kp2))
            return similarity
        else:
            return 0
    except Exception as e:
        print(Fore.RED + "Error: Failed to compare images:", e)
        return 0

def send_email(subject, message, recipient_email, sender_email, sender_password):
    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=recipient_email,
            subject=subject,
            contents=message
        )
        print(Fore.GREEN + "Email sent successfully!")
    except Exception as e:
        print(Fore.RED + "Error: Failed to send email:", e)

def main():
    try:
        sender_email = os.environ.get('SENDER_EMAIL')
        sender_password = os.environ.get('SENDER_PASSWORD')
        if GMAIL_SENDER is None or API is None:
            print(Fore.RED + "Error: Missing environment variables.")
            return

        website_link = input("[+] Enter the website link: ")
        wait_time = int(input("[+] Enter the number of seconds to wait: "))
        recipient_email = input("[+] Enter the recipient's email: ")
        sender_email = GMAIL_SENDER
        sender_password = API

        screenshot_path = "screenshots/"
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

        previous_screenshot = None
        old_similarity = 0

        while True:
            current_screenshot = take_full_screenshot(driver, website_link, wait_time, screenshot_path)
            if not current_screenshot:
                continue

            total_width = driver.execute_script("return document.body.scrollWidth")
            total_height = driver.execute_script("return document.body.scrollHeight")
            driver.set_window_size(total_width, total_height)
            time.sleep(wait_time)

            if previous_screenshot:
                print("Comparing screenshots...")
                similarity = compare_images(previous_screenshot, current_screenshot)
                print(Fore.GREEN + "Similarity is:", similarity)
                
                if similarity != old_similarity:
                    print(Fore.RED + "Changes detected! Similarity:", similarity)
                    ascii_art_2 = pyfiglet.figlet_format("Alert!!!")
                    print(Fore.RED + ascii_art_2)
                    send_email("Hello From Site Eye! The Content Has Changed", 
                               "The content of the webpage has changed.", 
                               recipient_email, sender_email, sender_password)
                    old_similarity = similarity
            else:
                print("Initial screenshot captured.")
                old_similarity = compare_images(current_screenshot, current_screenshot)

            previous_screenshot = current_screenshot
            time.sleep(2)

    except KeyboardInterrupt:
        print(Fore.LIGHTCYAN_EX + "Exiting...")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
