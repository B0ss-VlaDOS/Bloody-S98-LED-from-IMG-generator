import os
from PIL import Image
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to define key positions directly without reading a configuration file
# 800x240
def define_key_positions():
    key_positions = {
        'Button_000': (52, 1, 37, 37),
        'Button_016': (120, 1, 37, 37),
        'Button_024': (157, 1, 37, 37),
        'Button_032': (194, 1, 37, 37),
        'Button_040': (231, 1, 37, 37),
        'Button_048': (268, 1, 37, 37),
        'Button_056': (305, 1, 37, 37),
        'Button_064': (342, 1, 37, 37),
        'Button_072': (379, 1, 37, 37),
        'Button_080': (416, 1, 37, 37),
        'Button_088': (453, 1, 37, 37),
        'Button_096': (490, 1, 37, 37),
        'Button_104': (526, 1, 37, 37),
        'Button_GAME': (580, 1, 37, 37),  # GAME key next to F12
        'Button_001': (52, 44, 37, 37),
        'Button_009': (90, 44, 37, 37),
        'Button_017': (126, 44, 37, 37),
        'Button_025': (162, 44, 37, 37),
        'Button_033': (199, 44, 37, 37),
        'Button_041': (235, 44, 37, 37),
        'Button_049': (272, 44, 37, 37),
        'Button_057': (308, 44, 37, 37),
        'Button_065': (345, 44, 37, 37),
        'Button_073': (381, 44, 37, 37),
        'Button_081': (418, 44, 37, 37),
        'Button_089': (454, 44, 37, 37),
        'Button_097': (491, 44, 37, 37),
        'Button_105': (527, 44, 37, 37),
        'Button_002': (52, 80, 54, 37),
        'Button_010': (108, 80, 37, 37),
        'Button_018': (144, 80, 37, 37),
        'Button_026': (181, 80, 37, 37),
        'Button_034': (217, 80, 37, 37),
        'Button_042': (253, 80, 37, 37),
        'Button_050': (290, 80, 37, 37),
        'Button_058': (327, 80, 37, 37),
        'Button_066': (363, 80, 37, 37),
        'Button_074': (399, 80, 37, 37),
        'Button_082': (436, 80, 37, 37),
        'Button_090': (472, 80, 37, 37),
        'Button_098': (509, 80, 37, 37),
        'Button_106': (546, 80, 54, 37),
        'Button_003': (52, 117, 63, 37),
        'Button_011': (116, 117, 37, 37),
        'Button_019': (153, 117, 37, 37),
        'Button_027': (189, 117, 37, 37),
        'Button_035': (226, 117, 37, 37),
        'Button_043': (263, 117, 37, 37),
        'Button_051': (299, 117, 37, 37),
        'Button_059': (336, 117, 37, 37),
        'Button_067': (373, 117, 37, 37),
        'Button_075': (409, 117, 37, 37),
        'Button_083': (445, 117, 37, 37),
        'Button_091': (482, 117, 37, 37),
        'Button_099': (518, 117, 82, 37),
        'Button_004': (52, 153, 81, 37),
        'Button_020': (135, 153, 37, 37),
        'Button_028': (172, 153, 37, 37),
        'Button_036': (208, 153, 37, 37),
        'Button_044': (245, 153, 37, 37),
        'Button_052': (281, 153, 37, 37),
        'Button_060': (317, 153, 37, 37),
        'Button_068': (354, 153, 37, 37),
        'Button_076': (391, 153, 37, 37),
        'Button_084': (427, 153, 37, 37),
        'Button_092': (463, 153, 37, 37),
        'Button_100': (500, 153, 98, 37),
        'Button_005': (52, 189, 44, 37),
        'Button_013': (98, 189, 44, 37),
        'Button_021': (144, 189, 44, 37),
        'Button_053': (191, 189, 226, 37),
        'Button_085': (418, 189, 37, 37),
        'Button_093': (455, 189, 37, 37),
        'Button_109': (492, 189, 37, 37),
        'Button_113': (564, 1, 37, 37),
        'Button_124': (575, 158, 37, 37),
        'Button_117': (538, 194, 37, 37),
        'Button_125': (575, 194, 37, 37),
        'Button_133': (612, 194, 37, 37),
        'Button_136': (621, 1, 37, 37),
        'Button_144': (658, 1, 37, 37),
        'Button_152': (695, 1, 37, 37),
        'Button_160': (732, 1, 37, 37),
        'Button_137': (621, 44, 37, 37),
        'Button_145': (658, 44, 37, 37),
        'Button_153': (695, 44, 37, 37),
        'Button_161': (732, 44, 37, 37),
        'Button_138': (621, 80, 37, 37),
        'Button_146': (658, 80, 37, 37),
        'Button_154': (695, 80, 37, 37),
        'Button_162': (732, 80, 37, 71),
        'Button_139': (621, 117, 37, 37),
        'Button_147': (658, 117, 37, 37),
        'Button_155': (695, 117, 37, 37),
        'Button_140': (621, 153, 37, 37),
        'Button_148': (658, 153, 37, 37),
        'Button_156': (695, 153, 37, 37),
        'Button_164': (732, 153, 37, 71),
        'Button_141': (658, 189, 71, 37),
        'Button_157': (695, 189, 37, 37),
    }
    return key_positions

# Function to generate lighting configuration based on the image
def generate_lighting_config(image_file, key_positions, output_file):
    img = Image.open(image_file)
    img = img.convert('RGB')  # Convert to RGB to get colors

    root = ET.Element("Root")
    description = ET.SubElement(root, "Description")
    frame_time = ET.SubElement(root, "FrameTime")
    frame_time.text = "1000"
    loop_time = ET.SubElement(root, "LoopTime")
    loop_time.text = "0"
    repeat = ET.SubElement(root, "Repeat")
    repeat.text = "true"
    frame_count = ET.SubElement(root, "FrameCount")
    frame_count.text = "1"
    spi = ET.SubElement(root, "SPI")
    spi.text = "5"
    single_color = ET.SubElement(root, "SingleColor")
    single_color.text = "1"

    # Create frame element
    frame = ET.SubElement(root, "Frame", Value="0")

    for key, (x, y, width, height) in key_positions.items():
        # Get average color of the key area from the image
        key_img = img.crop((x, y, x + width, y + height))
        avg_color = key_img.resize((1, 1)).getpixel((0, 0))
        hex_color = f"#{avg_color[0]:02x}{avg_color[1]:02x}{avg_color[2]:02x}"
        led = ET.SubElement(frame, "LED", Value=key.split('_')[1] if key != 'Button_GAME' else '165')
        led.text = hex_color

    # Write to output XML file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Function for GUI to select files and save configuration
def gui_main():
    def open_image():
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image_path.set(file_path)

    def save_config():
        output_path = filedialog.asksaveasfilename(defaultextension=".kbdPannel", filetypes=[("Keyboard Panel Files", "*.kbdPannel")])
        if output_path:
            key_positions = define_key_positions()
            try:
                generate_lighting_config(image_path.get(), key_positions, output_path)
                messagebox.showinfo("Success", f"Lighting configuration saved to {output_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate configuration: {e}")

    # Creating GUI window
    root = tk.Tk()
    root.title("Keyboard Lighting Config Generator")

    # Variables
    image_path = tk.StringVar()

    # Layout
    tk.Label(root, text="Select Background Image:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=image_path, width=50).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=open_image).grid(row=0, column=2, padx=10, pady=10)
    
    tk.Button(root, text="Generate Config", command=save_config).grid(row=1, column=1, pady=20)

    root.mainloop()

if __name__ == "__main__":
    gui_main()