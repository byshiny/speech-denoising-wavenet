from pydub import AudioSegment
import os
def convert_files_to_wav(directory):
     for filename in os.listdir(directory):
          if filename.endswith(".mp3"):
               filename_without_ext = os.path.splitext(filename)[0]
               filename_wav = filename_without_ext + ".wav"
               if not os.path.isfile(directory + filename_wav):
                    print("converting " + filename)
                    mp3_path = os.path.join(directory, filename)
                    mp3_audio = AudioSegment.from_file(mp3_path, format="mp3")
                    # I am not an audio expert, not sure if I shuld use this instead of above
                    # Will defer to this later.
                    # raw_audio = AudioSegment.from_file("audio.wav", format="raw",
                    # frame_rate=44100, channels=2, sample_width=2)
                    wav_path = os.path.join(directory, filename_wav)
                    mp3_audio.export(wav_path, format="wav")

"""
Convert mp3 files to wav files, if the matching
wave file in the directory is not found. """
def main():
     convert_files_to_wav("data/NSDTSEA/noisy_testset_wav/Knuth")

main()

