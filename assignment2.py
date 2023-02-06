#Name: CHUO SING JEAN / TAN JIN WEN 
#MATRICS NO: A19MJ0026 / A19MJ0128 

import pyautogui #screenshot 
import pytesseract #text recognition 
from PIL import Image 

# Define the region to capture 
left, top, width, height = 0, 150, 800, 500

# function to capture screenshot 
def screen_capture(filename):
    img = pyautogui.screenshot(region=(left, top, width, height))

    # Save the screenshot to a file
    img.save('screenshot.png')

# function to intepret the image using ORC text recognition from pytesseract 
def ocr_text_recognition(image_filename):
    text = pytesseract.image_to_string(Image.open(image_filename))
    return text

# function to generate text file from the screenshot input 
def screen_scraping_ocr_generation(screenshot_input, text_output):
    screen_capture(screenshot_input)
    text = ocr_text_recognition(screenshot_input)
    with open(text_output, 'w') as file:
        file.write(text)
    
# calling the function to automate the screen scrapping and 
screen_scraping_ocr_generation("screenshot.png","output.txt") 