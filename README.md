# SiteEye

A visual website monitoring tool that detects and alerts you when changes occur on a webpage.

## Overview

SiteEye is a powerful Python-based tool designed to monitor websites by capturing periodic screenshots and detecting visual changes. When significant changes are detected on the monitored website, SiteEye alerts the user with both visual and audio notifications.

## Features

- Automated screenshot capture of websites at regular intervals
- Visual comparison to detect changes between screenshots
- Customizable sensitivity threshold for change detection
- Audio alerts when significant changes are detected
- Headless Chrome browser integration for reliable screenshot capture
- Color-coded console output for easy monitoring status recognition

## Requirements

- Python 3.6+
- Required Python packages:
  - opencv-python (cv2)
  - selenium
  - webdriver-manager
  - colorama
  - playsound
  - Chrome browser installed on your system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/everythingBlackkk/SiteEye.git
cd SiteEye
```

2. Install the required dependencies:
```bash
pip install selenium webdriver-manager colorama opencv-python playsound
```

3. Make sure you have Google Chrome installed on your system, as the tool uses Chrome to capture screenshots.

## Usage

Run the script from the command line:

```bash
python site_eye.py
```

You will be prompted to enter:
1. The website URL you want to monitor
2. The wait time in seconds (how long to wait after page load before taking a screenshot)
3. The monitoring interval in seconds (how frequently to check for changes)

## How It Works

1. SiteEye launches a headless Chrome browser to capture full-page screenshots
2. Screenshots are saved in a `screenshots` directory
3. Each new screenshot is compared with the previous one using OpenCV
4. If the difference exceeds the threshold (default 0.01%), an alert is triggered
5. The tool continues monitoring until interrupted with Ctrl+C

## Important Note

⚠️ **Please ensure that the `alert.mp3` file is present in the same directory as the script.**

If this file is missing, the audio alert feature will not work properly. The audio file is used to alert you when changes are detected on the monitored website.

## Customization

You can modify the following parameters in the code:
- `diff_threshold`: Change detection sensitivity (default: 0.01%)
- Chrome options: Add or modify browser settings for screenshot capture
- Screenshot resolution: Change the window size in Chrome options

## Troubleshooting

If you encounter issues:

1. Make sure Chrome is installed and accessible
2. Check that all dependencies are correctly installed
3. Verify the `alert.mp3` file exists in the script directory
4. For websites that load dynamically, try increasing the wait time

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

everythingBlackkk

## Repository

https://github.com/everythingBlackkk/SiteEye
