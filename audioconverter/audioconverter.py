import os
from pydub import AudioSegment
from pydub.playback import play


# Output directory
OUT_DIR = "output/audio"
os.system(f"mkdir {OUT_DIR}")


def Audio2WAV(input_file, output_type="wav"):
    try:
        song = AudioSegment.from_file(
            input_file, format=f"{input_file.split('.')[-1]}")
        song = song.set_channels(1)
        song = song.set_frame_rate(16000)
    except:
        print("Failed")
    song.export(f"{OUT_DIR}/{input_file.split('.')[0]}.{output_type}",
                format=f"{output_type}", bitrate="256k")


def OGG2MP3(input_file, output_type="mp3"):
    song = AudioSegment.from_ogg(
        input_file)
    song = song.set_channels(1)
    song = song.set_frame_rate(16000)
    song.export(f"{OUT_DIR}/{input_file.split('.')[0]}.{output_type}",
                format=output_type, bitrate="256k")
