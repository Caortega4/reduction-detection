import soundfile as sf
import librosa

print("Downsampling...")
y, s = librosa.load("C:\Research\\recordings-reduction\EN_006.wav", sr=16000) # Downsample 44.1kHz to 16000kHz
print("Writing downsampled audio")

sf.write("stereo_file2.wav", y, 16000)