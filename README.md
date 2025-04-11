# 🎨 Color Detection with OpenCV — Real-Time RGB Classifier

This project is a **Python + OpenCV-based color detection tool** that identifies the closest matching **Skin Tone**, **Fabric Dye**, and **Soil Type** based on RGB values from any image. It’s interactive, fast, and logs all the detections with precise color data.

> 📍 Developed as a personal project to enhance my skills in **computer vision**, **color science**, **CSV data management**, and **GUI-based interaction using OpenCV**.

---

## 🔍 Features

- ✅ Real-time RGB color detection from image via double-click.
- ✅ Matches color to:
  - 🌸 **Skin Tones**
  - 👕 **Fabric Dyes**
  - 🌱 **Soil Types**
- ✅ Color match is based on **Manhattan Distance** in RGB space.
- ✅ Visual color highlighting & classification overlay.
- ✅ Results logged with timestamp in `color_log.csv`.

---

## 💡 Tech Stack

- **Python 3.10+**
- **OpenCV**
- **Pandas**
- **CSV-based dataset handling**
- **Basic GUI via OpenCV windows**

---

## 📸 Screenshots

### 🔍 Color Detection in Action

![Color Detection GUI](./assets/screenshot_gui.png)  
> *Double-clicked pixel analyzed and categorized as: Skin Tone: Porcelain_343, Fabric Dye: Pink_496, Soil Type: Sandy Soil*

### 📊 CSV Logging

![CSV Log Example](./assets/screenshot_log.png)  
> *Each interaction gets logged with category, detected name, RGB values, and timestamp*

---

## 🗃️ Directory Structure

```
Color-Detection-OpenCV-main/
│
├── main.py                         # 🔧 Core Python Script
├── color_log.csv                   # 📋 Log of all detected colors
├── colorpic.jpg                    # 🖼️ Sample image
├── skintones_realistic.csv        # 🎨 Skin tone dataset
├── fabric_dyes_realistic.csv      # 🎽 Fabric dye dataset
├── soil_colors.csv                # 🌍 Soil color dataset
└── ...
```

---

## 📌 How It Works

1. **Load image + CSV datasets** containing color names and their RGB values.
2. **On double-click**: Grab pixel RGB from the image.
3. Compare pixel RGB with dataset values using **Manhattan Distance**.
4. Show the closest match of each category on the image.
5. Log the results in `color_log.csv` with timestamp.

---

## 🧠 Key Concepts in Computer Vision Used

- **Pixel-Level Image Processing**
- **Color Space Representation (RGB)**
- **Distance Metrics (Manhattan Distance)**
- **Human-Computer Interaction** via Mouse Events
- **Data Logging & Analysis with CSV**

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/color-detection-opencv.git
cd color-detection-opencv
pip install -r requirements.txt
python main.py
```

> Ensure your dataset CSVs follow this format: `Name,R,G,B`

---

## 📁 Sample Entry in CSV

```
Name,R,G,B
Porcelain_343,199,199,201
Pink_496,199,199,201
Sandy Soil,199,199,201
```

---

## 📈 Applications

- 🌾 **Agriculture**: Soil color classification
- 🎨 **Fashion**: Textile/fabric dye detection
- 💅 **Cosmetics**: Skin tone analysis
- 🧠 **Education**: Computer vision demos

---

## 👨‍💻 Author

**[Devang Anilkumar Kanjaria]**  
B.E. in Information Technology (2025)  
Passionate about computer vision, Python automation, and full-stack development.
