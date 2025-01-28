
# 🧙‍♂️ Invisible Cloak Effect using OpenCV  

✨ This project demonstrates an **Invisible Cloak Effect** using OpenCV, allowing users to make selected cloak colors disappear and seamlessly blend into the background.  

---

## 🌟 **Features**  

- 🎨 **Color Selection**: A pop-up window lets you choose from the following cloak colors:  
  - 🔴 **Red**  
  - 🔵 **Sky Blue**  
  - 🌟 **Bright Yellow**  
  - 🫒 **Olive Green**  

- 🖥️ **Full-Screen Display**: Enjoy an immersive experience with the video feed displayed in **full-screen mode**.  

- 📷 **Dynamic Background Capture**: Captures the background dynamically, ensuring precise and accurate cloak replacement.  

- 🎭 **Robust Masking**: Uses **HSV color space** and **morphological operations** for creating a clean and precise mask for the cloak color.  

---

## 🛠️ **How It Works**  

### 🏞️ **Background Capture**  
- At the program's start, a static background is captured by averaging multiple frames.  
- Move out of the frame during this process.  

### 🎨 **Color Masking**  
- Based on the selected color, a **mask** is generated using predefined **HSV ranges**.  
- **Morphological operations** (like opening and dilation) refine the mask.  

### 🪄 **Invisible Effect**  
- The masked region of the cloak is replaced with the background, creating an **illusion of invisibility**.  

---

## 🧩 **Requirements**  

- 🐍 **Python 3.x**  
- 👓 **OpenCV**  
- 🧮 **NumPy**  
- 🖼️ **Tkinter** (for GUI)  

---

## 🚀 **How to Run**  

1. Install the required libraries:  
   ```bash  
   pip install opencv-python numpy  
   ```  

2. Run the script:  
   ```bash  
   python invisible_cloak.py  
   ```  

3. Select a color from the pop-up window and follow the instructions displayed in the terminal.  

4. To exit the program, press **'q'**.  

---
## **Screenshots**
![Colour Selection](https://github.com/Manya0407/Invisible-Cloak/blob/main/ss1.png?raw=true)

![Colour Selection](https://github.com/Manya0407/Invisible-Cloak/blob/main/ss2.png?raw=true)

