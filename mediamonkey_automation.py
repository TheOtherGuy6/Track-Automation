"""
Script Name: mediamonkey_automation.py
Version: 1.0
Author: Wayne
Copyright © 2023 Wayne Fry. All rights reserved.

License Agreement:
By using this script, you agree to the following terms and conditions:
1. This script is provided for educational and informational purposes only.
2. You may modify and distribute this script for personal use or within your organization.
3. You may not use this script for any commercial purposes without explicit permission from the author and copyright holder.
4. The author and copyright holder are not responsible for any damages or liabilities arising from the use of this script.
5. This script is provided as-is, without any warranty or guarantee of any kind.

Installation:
Before running this script, make sure you have the following libraries installed:
- time
- pyautogui

To install the required libraries, you can use the following command:
pip install pyautogui

"""

import time
import pyautogui

# Positions of Track # column header and Confirm button
track_column_x = 446
track_column_y = 192
confirm_button_x = 3277
confirm_button_y = 1998

# Define the color pixel values to wait for during the lookup process
R = 251
G = 140
B = 0

# Delay before starting the automation
time.sleep(5)

while True:
    # Delay before clicking the "Track #" column header
    print("Waiting for 10 seconds before clicking the 'Track #' column header...")
    time.sleep(10)

    # Click the "Track #" column header to select all tracks
    print("Clicking the 'Track #' column header...")
    pyautogui.click(track_column_x, track_column_y)

    # Wait for the lookup process to complete
    print("Waiting for the lookup process to complete...")
    while not pyautogui.pixelMatchesColor(confirm_button_x, confirm_button_y, (R, G, B)):
        time.sleep(1)
        print("Still waiting for the lookup process to complete...")

    # Delay before clicking the "Confirm" button
    print("Waiting for 60 seconds before clicking the 'Confirm' button...")
    time.sleep(60)

    # Click the "Confirm" button
    print("Moving the mouse to the 'Confirm' button position...")
    pyautogui.moveTo(confirm_button_x, confirm_button_y)
    time.sleep(2)
    print("Clicking the 'Confirm' button...")
    pyautogui.click()

    # Delay before starting the next iteration
    time.sleep(2)
