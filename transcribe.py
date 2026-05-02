from faster_whisper import WhisperModel
import sys

def transcribe_audio(wav_path, model_size="base", device="cpu"):
    """
    Transcribe a WAV file (16KHz mono) using the Faster Whisper.
    model_size can be one of: tiny, base, small, medium, large-v2, large-v3
    device="cpu" or "cuda" (if GPU is available)
    """    
    # Initialize the model (downloads automatically on first user)
    model = WhisperModel(model_size, device=device, commute_type="int8")

    # Run the Transcription, "en" means English language. You can specify other languages or None for auto-detection.
    segments, info = model.transcribe(wav_path, beam_size=5, language="en")

    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})")
    print("Transcription:")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

    # Return the full transcription text
    full_text = " ".join(seg.text for seg in segments)
    return full_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <input_audio_file>")
        sys.exit(1)

    wav_file = sys.argv[1]
    transcription = transcribe_audio(wav_file, model_size='base', device='cpu')
    print("\nFull Transcription:")
    print(transcription)
