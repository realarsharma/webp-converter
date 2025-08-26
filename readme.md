# webp-converter 

Version 1.0

This project optimizes images from a source folder and saves the optimized versions in a destination folder. It supports resizing, aspect ratio preservation, and optional WebP conversion.

## Folder Structure

webp-converter/
├── main.py  
├── readme.txt  
├── requirements.txt  
├── run.bat  
├── run.py  
├── webp-converter-env/  
│   ├── pyvenv.cfg  
│   ├── Include/  
│   ├── Lib/  
│   └── Scripts/  
├── Opt-Image/  
├── Org-Image/  
│   ├── sample-images/  

## Important Note About Source Folder

The source folder **Org-Image/** must contain **at least one subfolder** with images.  

Example:

Org-Image/  
└── image-folder-1/  
    ├── image1.jpg  
    ├── image2.png  

If you put images directly in Org-Image/ without a subfolder, the optimizer **will not process them**.

## How to Install and Run (First Time)

1. Place the project folder anywhere on your computer.  
2. Open the folder.  
3. Double-click **run.bat**.  

The batch file will:  
- Create a Python virtual environment (webp-converter-env) if it doesn’t exist.  
- Install required Python packages (requirements.txt).  
- Run the optimizer.

## How to Use from Next Time

- Simply double-click **run.bat** again, or run **run.py** from Python if you prefer.  
- The virtual environment is already set up, so dependencies are already installed.

## Where to Place Source & Destination Folders

Place the images you want to optimize in subfolders inside Org-Image/. The optimized images will be automatically saved in Opt-Image/ with the same name.

Both folders are relative to the project root.

## User Settings (in run.py)

You can configure the following options by editing **run.py**:

MAX_DIMENSION  : 1000  
    Maximum width or height for resized images. Aspect ratio is preserved.  

QUALITY        : 80  
    WebP conversion quality (0-100).  

CONVERT_WEBP   : True  
    Set to True to convert all images to WebP format; False to keep original format.  

Example:

MAX_DIMENSION = 1200  
QUALITY = 90  
CONVERT_WEBP = False  

## That’s it!

Just place your images in subfolders of Org-Image/, configure settings in run.py if needed, and run the optimizer.
