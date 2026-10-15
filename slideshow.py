from  itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk
import time

root = tk.Tk()
root.title("Image Slideshow Viewer")

# list of image file paths
image_paths=[
    
    r"C:\Users\aariz\Downloads\Baku Tour  Tab Travels\WhatsApp Image 2026-10-07 at 1.13.16 PM.jpeg",
    r"C:\Users\aariz\Downloads\Baku Tour  Tab Travels\WhatsApp Image 2026-10-06 at 5.01.17 PM (1).jpeg",
    r"C:\Users\aariz\Downloads\Baku Tour  Tab Travels\WhatsApp Image 2026-10-06 at 5.01.17 PM.jpeg",
   
]

# Resizing images and converting them to 1080x1080 pixels
image_size=[1080,1080]
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)  # Display each image for 3 seconds
        
slideshow=cycle(photo_images)  # Create an infinite cycle of images

def start_slideshow():
    for _ in range(len(image_paths)):
         update_image()
        
play_button=tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
    
