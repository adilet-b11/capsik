import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
def limitsEnhancer(limit_image):
    limit_image_rgb = cv2.cvtColor(limit_image, cv2.COLOR_BGR2GRAY)
    limit_image_resized = cv2.resize(limit_image_rgb, (700, 430))
    limit_image_dilated = cv2.dilate(limit_image_resized, (10, 10), iterations=3)
    return limit_image_dilated

def limitsProcess(source_image):
    upper_limit = source_image[6:22, 279:314]
    lower_limit = source_image[216:234, 280:314]
    upper_limit_enhanced = limitsEnhancer(upper_limit)
    lower_limit_enhanced = limitsEnhancer(lower_limit)
    upper_limit_text = pytesseract.image_to_string(upper_limit_enhanced)
    lower_limit_text = pytesseract.image_to_string(lower_limit_enhanced)
    return upper_limit_text, lower_limit_text

img = cv2.imread('Adilet.jpg')
text = limitsProcess(img)
print(text)
