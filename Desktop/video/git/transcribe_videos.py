import os
import wave
import json
import logging
from tqdm import tqdm
from vosk import Model, KaldiRecognizer
import moviepy.editor as mp
from pydub import AudioSegment

# Path to the Vosk model (update with your local path)
model_path = "/path/to/your/vosk/model"

# Folder containing the video files
video_folder = "videos"

# Configure logging to both a file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("transcription.log"),
        logging.StreamHandler()  # Console output
    ]
)

# Check if the model exists at the provided path
if not os.path.exists(model_path):
    logging.error("Model not found! Please download and extract the model from: https://alphacephei.com/vosk/models")
    exit(1)

# Load the model
model = Model(model_path)

# Step 1: Extract audio from video
def extract_audio_from_video(video_path, audio_path):
    logging.info(f"Extracting audio from video: {video_path}")
    try:
        video = mp.VideoFileClip(video_path)
        # Extract audio and save it as WAV format
        video.audio.write_audiofile(audio_path)
        logging.info(f"Audio saved: {audio_path}")
        
        # Convert audio to mono and set the frequency to 16000 Hz using Pydub
        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_channels(1)  # Convert to mono
        audio = audio.set_frame_rate(16000)  # Set frequency to 16000 Hz
        audio.export(audio_path, format="wav")  # Save back as WAV
        logging.info(f"Audio converted to mono, 16000 Hz, and saved: {audio_path}")
        
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        exit(1)

# Step 2: Transcribe audio with Vosk and show progress bar
def transcribe_audio(audio_path, transcription_file_path):
    logging.info(f"Starting transcription of audio: {audio_path}")
    try:
        # Open the audio file
        wf = wave.open(audio_path, "rb")

        # Check if the audio is mono and has a frequency of 16000 Hz
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            logging.error("Audio file must be mono with a sample rate of 16000 Hz")
            exit(1)

        # Initialize the recognizer
        recognizer = KaldiRecognizer(model, wf.getframerate())

        # String to store the transcription
        transcription = ""

        # Get the total frames for progress bar
        total_frames = wf.getnframes()
        logging.info(f"Total frames in audio file: {total_frames}")

        # Read the audio file and recognize using progress bar
        with tqdm(total=total_frames, desc="Transcribing", unit="frames") as pbar:
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    result_json = json.loads(result)
                    transcription += result_json['text'] + " "
                pbar.update(4000)

        # Process the final fragment
        final_result = recognizer.FinalResult()
        final_json = json.loads(final_result)
        transcription += final_json['text']

        # Save the transcription to a file
        with open(transcription_file_path, "w") as f:
            f.write(transcription)
        logging.info(f"Transcription saved to file: {transcription_file_path}")

    except Exception as e:
        logging.error(f"Error during transcription: {e}")
        exit(1)

# Step 3: Main program logic
def main():
    # Process video files from lesson1.mp4 to lesson277.mp4
    for i in range(1, 278):  # lesson1.mp4 to lesson277.mp4
        video_file = f"lesson{i}.mp4"
        video_path = os.path.join(video_folder, video_file)
        
        if os.path.exists(video_path):  # Check if file exists
            audio_path = video_path.replace('.mp4', '.wav')
            transcription_file_path = video_path.replace('.mp4', '.txt')

            logging.info(f"Starting to process file: {video_file}")
            
            # Extract audio from video
            extract_audio_from_video(video_path, audio_path)

            # Transcribe the extracted audio
            transcribe_audio(audio_path, transcription_file_path)

            # Remove the temporary audio file
            if os.path.exists(audio_path):
                os.remove(audio_path)
                logging.info(f"Temporary audio file removed: {audio_path}")
        else:
            logging.warning(f"File {video_file} not found. Skipping...")

# Run the program
if __name__ == "__main__":
    logging.info("Starting transcription program for all video files.")
    main()
    logging.info("Program completed successfully.")