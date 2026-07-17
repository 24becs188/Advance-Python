import cv2

# Define the absolute file path to the image on your computer
# Note: Use forward slashes (/) to avoid path syntax errors in Python
file_path = r"C:\Users\hi\OneDrive\Documents\Pictures\Screenshots\Screenshot 2026-04-24 211738.png"
# Read the image file from the path
img = cv2.imread(file_path)

# Verify if the image was successfully found and loaded
if img is None:
    print("Error: Could not open or find the image. Check the file path layout.")
else:
    # Display the loaded image in a window
    cv2.imshow("Loaded Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
