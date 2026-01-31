#!/usr/bin/env python3
# png_To_jpeg_converter.py
# This script converts a png image file to a jpeg image file and
# saves the converted image to a new file.
# Written by: JakeTheSnake(JMG3000)

from PIL import Image
import os


def converter():
    stop = True
    while stop:
        # Define the path to the desired folder
        pic_path = os.path.expanduser('~/Pictures/headshots')

        user_png_path = input("Please enter the path and name of the png you wish to convert: ")

        if user_png_path == "":
            input_path = pic_path + "/closer_headshot_blackSuitAndRedTie.png"


        else:
            input_path = user_png_path

        user_jpeg_path = input("Please enter the path and name of the converted jpeg you wish to save: ")

        if user_jpeg_path == "":
            output_path = pic_path + "/closer_pro_headshot_high_quality.jpg"

        else:
            output_path = user_jpeg_path


        # attempt to open the file
        try:
            img_data = Image.open(input_path)
            print("Opening {}".format(input_path))

        # catch an exception when the original file is not opened
        except Exception as e:
            print(f"Failed to open {input_path}. Error Code{e}")
            break


        # attempt to convert the file after opening is successful
        try:
            img_data = img_data.convert("RGB")
            print("Converting {}".format(input_path))

        # catch an exception when the original file is not converted
        except Exception as e:
            print(f"Failed to convert {input_path}. Error Code{e}")


        # attempt to save the file after convertion is successful
        try:
            img_data.save(output_path, "JPEG", quality=95)
            print("Saved {}".format(output_path))

        # catch an exception when the converted file is not saved
        except Exception as e:
            print(f"Failed to save {output_path}. Error Code{e}")



if __name__ == "__main__":
    converter()
    print("...Done")

    #print("The png image has been converted to a jpeg!")
    # I used the os.