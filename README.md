# Site Eye
WARN!! # The tool is under development and you will need an email to send from it. This is the version for it and it is being developed Thanks.
_____
Site Eye is a tool designed to monitor changes in a web page's content by taking screenshots at regular intervals and comparing them to detect any differences. This tool can be useful for tracking updates or modifications on a website over time.

## Features

- Takes full screenshots of a specified web page.
- Compares current and previous screenshots to identify changes in content.
- Sends email notifications when changes are detected.
- Utilizes OpenCV for image comparison using SIFT (Scale-Invariant Feature Transform) algorithm.
- Supports Chrome browser for headless operation.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/everythingBlackkk/Site-Eye.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Site-Eye
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have Chrome browser installed on your system.

## Usage

1. Run the `main.py` script to start monitoring a website:

    ```bash
    python main.py
    ```

2. Follow the prompts to enter the website link, wait time between screenshots, recipient's email, your email, and your email password.

3. Site Eye will continuously monitor the specified web page and send email alerts if any changes are detected.

verview
This guide will walk you through the process of generating a Google App Password. Google App Passwords are one-time passwords that can be used instead of your regular account password for specific apps or devices, providing an added layer of security.

Prerequisites
Before you begin, make sure you have the following:

A Google account with two-step verification enabled
Access to your Google account settings
Steps to Get A Google App Password
Sign in to your Google Account

Go to Google Account and sign in with your credentials.
Access App Passwords

In the Security section, click on "App passwords" or visit Google App Passwords.
Generate App Password

Choose the app and device you want to generate the password for from the drop-down menus.
Click on "Generate" or "Generate App Password."
Use the App Password

Copy the generated password.
Paste it into the password field of the app or device where you want to use it.
Important Notes
App passwords are one-time passwords, meaning they can only be used for the specific app and device you generated them for.
You can revoke or regenerate app passwords at any time from your Google Account settings.
Conclusion
By following these steps, you can easily generate a Google App Password and enhance the security of your account when using third-party apps or devices.
## Dependencies

- Python 3.x
- OpenCV (cv2)
- pyfiglet
- colorama
- yagmail
- selenium
- Pillow (PIL)

## Notes

- Make sure to configure your email settings correctly to enable email notifications.
- Site Eye uses the SIFT algorithm for image comparison, which requires OpenCV installation with non-free modules enabled.

## Contributing

Contributions to enhance or add new features to Site Eye are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

