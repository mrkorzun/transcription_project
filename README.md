# Video Transcription Script

This project extracts audio from videos, transcribes the audio using the Vosk speech-to-text engine, and saves the transcription.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mrkorzun/transcription_project.git
    cd transcription_project
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and extract the Vosk model, and set the path in `config.py`.

## Usage

Run the script using:
```bash
python transcribe_videos.py