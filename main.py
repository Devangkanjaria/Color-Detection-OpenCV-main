# Topics in Computer Vision Related to the Code:
# Pixel-level Image Processing: The code operates at the pixel level by extracting RGB values for clicked locations.
# Color Space and Representation: RGB color space is used for representing and comparing colors.
# Distance Metrics in Color Matching: The Manhattan distance is employed to quantify color similarity.
# Human-Computer Interaction (HCI): The use of mouse events and real-time feedback to enable user interaction with the image.
# This type of work is widely applicable in fields like agriculture, healthcare, fashion, and computer vision-assisted applications.

import cv2
import pandas as pd
from datetime import datetime
import os

# Paths to image and CSV files
img_path = r'D:\PROJECT\Color-Detection-OpenCV-main\colorpic.jpg'
skintone_csv_path = r'D:\PROJECT\Color-Detection-OpenCV-main\skintones_realistic.csv'
fabric_csv_path = r'D:\PROJECT\Color-Detection-OpenCV-main\fabric_dyes_realistic.csv'
soil_csv_path = r'D:\PROJECT\Color-Detection-OpenCV-main\soil_colors.csv'  # New path for soil CSV
log_file = r'D:\PROJECT\Color-Detection-OpenCV-main\color_log.csv'

# Check if files exist
for file_path in [img_path, skintone_csv_path, fabric_csv_path, soil_csv_path]:
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}.")
        exit()

# Load the image
img = cv2.imread(img_path)
if img is None:
    print(f"Error: Could not load the image. Check the file at {img_path}.")
    exit()

# Load skin tone, fabric dye, and soil databases
skintone_data = pd.read_csv(skintone_csv_path)
fabric_data = pd.read_csv(fabric_csv_path)
soil_data = pd.read_csv(soil_csv_path)  # Load soil data

required_columns = ["Name", "R", "G", "B"]

for dataset, name in [(skintone_data, "Skin Tone"), (fabric_data, "Fabric Dye"), (soil_data, "Soil Type")]:
    if list(dataset.columns) != required_columns:
        print(f"Error: The {name} CSV file must have columns: {required_columns}.")
        exit()

# Initialize global variables
clicked = False
r = g = b = x_pos = y_pos = 0

# Prepare log file
try:
    open(log_file, 'x').close()
    with open(log_file, 'w') as f:
        f.write("Timestamp,Category,Name,R,G,B\n")
except FileExistsError:
    pass

# Function to find the closest match in a dataset
def get_closest_match(R, G, B, dataset):
    minimum_distance = float("inf")
    closest_name = "Unknown"
    for _, row in dataset.iterrows():
        d = abs(R - row["R"]) + abs(G - row["G"]) + abs(B - row["B"])
        if d < minimum_distance:
            minimum_distance = d
            closest_name = row["Name"]
    return closest_name

# Function to handle mouse events
def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

        # Detect categories
        skintone_name = get_closest_match(r, g, b, skintone_data)
        fabric_name = get_closest_match(r, g, b, fabric_data)
        soil_name = get_closest_match(r, g, b, soil_data)  # Detect soil

        # Log the result
        try:
            with open(log_file, 'a') as f:
                f.write(f"{datetime.now()},Skin Tone,{skintone_name},{r},{g},{b}\n")
                f.write(f"{datetime.now()},Fabric Dye,{fabric_name},{r},{g},{b}\n")
                f.write(f"{datetime.now()},Soil Type,{soil_name},{r},{g},{b}\n")  # Log soil type
            print(f"Logged Skin Tone: {skintone_name}, Fabric Dye: {fabric_name}, Soil Type: {soil_name}, R={r}, G={g}, B={b}")
        except Exception as e:
            print(f"Error logging data: {e}")

cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', draw_function)

while True:
    try:
        cv2.imshow("Color Detector", img)
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        break

    if clicked:
        # Highlight detected color
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Create a text string for skin tone, fabric dye, and soil type
        skintone_name = get_closest_match(r, g, b, skintone_data)
        fabric_name = get_closest_match(r, g, b, fabric_data)
        soil_name = get_closest_match(r, g, b, soil_data)  # Identify soil type
        text = f"Skin Tone: {skintone_name} | Fabric Dye: {fabric_name} | Soil Type: {soil_name} (R={r}, G={g}, B={b})"

        # Display text in a contrasting color
        text_color = (255, 255, 255) if r + g + b < 600 else (0, 0, 0)
        cv2.putText(img, text, (50, 50), 1, 0.8, text_color, 2, cv2.LINE_AA)

        clicked = False

    # Exit the application on 'Esc' key press
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()


