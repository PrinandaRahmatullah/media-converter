import os
from pydub import AudioSegment
from pydub.playback import play


# Output directory
OUT_DIR = "../output/audio"
os.system(f"mkdir {OUT_DIR}")


def Audio2WAV(input_file, output_type="wav"):
    try:
        song = AudioSegment.from_file(
            input_file, format=f"{input_file.split('.')[-1]}")
    except:
        print("Failed")
    song.export(f"{OUT_DIR}/{input_file.split('.')[0]}.{output_type}",
                format=f"{output_type}")
