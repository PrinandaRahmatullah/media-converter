from PIL import Image
import os
import pyheif
import whatimage
import uuid
import cv2


# Output directory
OUT_DIR = "../output"
os.system(f"mkdir {OUT_DIR}")


# function to convert jpg (sometimes flipped)
def JPG2JPG(filename, rescale_size=80):
    image = cv2.imread(filename, cv2.IMREAD_LOAD_GDAL)

    scale_percent = rescale_size  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(
        f"{OUT_DIR}/{filename}.jpg", image)
