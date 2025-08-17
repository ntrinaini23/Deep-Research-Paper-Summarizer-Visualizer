import cv2

def enhance_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    enhanced = cv2.GaussianBlur(gray, (3,3), 0)
    output_path = image_path.replace(".png", "_enhanced.png")
    cv2.imwrite(output_path, enhanced)
    return output_path
