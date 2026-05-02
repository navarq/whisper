from pydub import AudioSegment
import os
import sys

def convert_to_wav(input_path, output_path=None):
    """
    Convert any audio file (MP3, M4A, OGG etc.) to WAV (16 KHz, mono).
    If output_path is not provided, the converted file will be saved in the same directory.
    """
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.wav"

    # Load the audio file (pydub uses ffmpeg)
    audio = AudioSegment.from_file(input_path)
    
    # Convert to mono and set sample rate to 16000 Hz
    audio = audio.set_channels(1).set_frame_rate(16000)

    # Export the audio in WAV format
    audio.export(output_path, format="wav")
    print(f"Converted {input_path} to {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python wavconverter.py <input_audio_file> [output_wav_directory]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    wav_file = convert_to_wav(input_file, output_path)

    print(f"Audio file converted to WAV format: {wav_file}")