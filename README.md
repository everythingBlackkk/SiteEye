# Site Eye
WARNING!! The tool is currently under development, and you will need an email to send from it. This version is specifically designed for that purpose and is currently being developed. Thank you.
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

