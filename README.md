# 🎥 Video Transcription Script 🎧

This project is a Python-based video transcription tool that extracts audio from video files, processes it using the Vosk speech-to-text engine, and outputs a text transcription. The project is designed to help users quickly convert videos into written content, making it ideal for content creators, researchers, or anyone who needs to work with audio data.

## ✨ Key Features

- **Video to Audio Conversion**: Automatically extracts audio from video files.
- **Speech-to-Text Transcription**: Utilizes the Vosk engine to transcribe audio into text.
- **Multi-Video Support**: Processes multiple video files in sequence.
- **Progress Visualization**: Displays a progress bar during transcription.
- **Automatic Cleanup**: Deletes temporary audio files after transcription.

## 🔧 Technologies and Libraries Used

- **[Vosk](https://alphacephei.com/vosk/models)**: A lightweight and efficient speech recognition model for many languages.
- **[moviepy](https://zulko.github.io/moviepy/)**: A Python module for video editing, used here to extract audio from videos.
- **[pydub](https://github.com/jiaaro/pydub)**: A high-level audio manipulation library used to convert audio to mono and adjust the sample rate.
- **[tqdm](https://github.com/tqdm/tqdm)**: A fast, extensible progress bar for providing real-time feedback during transcription.
- **Logging**: Provides detailed logs of each process step (both in the terminal and in a log file).

## 📦 Installation

### Prerequisites:
- Python 3.6+
- FFmpeg (required by `moviepy` for audio extraction). Install it via [FFmpeg official website](https://ffmpeg.org/download.html) or using a package manager like Homebrew:
    ```bash
    brew install ffmpeg
    ```

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/mrkorzun/transcription_project.git
    cd transcription_project
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download and extract the Vosk model from [here](https://alphacephei.com/vosk/models), and place it in a directory of your choice. Update the `model_path` variable in `transcribe_videos.py` to point to your Vosk model directory.

## 🚀 Usage

1. Place your video files in the `lessons` folder (or any folder of your choice, just update the `video_folder` path in the script).
   
2. Run the transcription script:
    ```bash
    python transcribe_videos.py
    ```

3. The script will extract audio from each video file, process the transcription, and save the text to a `.txt` file with the same name as the video. For example, `lesson1.mp4` will output `lesson1.txt`.

### Customizing the Script:
- Modify the `video_folder` variable to process videos from another directory.
- Adjust the `model_path` variable to use different Vosk models.
- You can customize the number of videos to process by updating the range in the `main()` function.

## 📄 Example

- **Input**: A video file named `lesson1.mp4`.
- **Output**: A transcription file named `lesson1.txt` containing the spoken words from the video.

### Sample Console Output:
```bash
    INFO: Extracting audio from video: lesson1.mp4
    INFO: Audio saved: lesson1.wav
    INFO: Audio converted to mono and saved with 16000 Hz sample rate: lesson1.wav
    INFO: Starting transcription of lesson1.wav
    Transcription: 80% [█████████████████████—] frames
    INFO: Transcription saved to file: lesson1.txt
```
## 📚 Future Improvements

- **Multi-language Support**: Integrate additional Vosk models for transcription in different languages.
- **Advanced Error Handling**: Improve error management for unsupported video formats.
- **Parallel Processing**: Add support for multithreading to speed up transcription of large video batches.

## 💡 Troubleshooting

1. **Vosk Model Not Found**: Ensure that you've downloaded and extracted the Vosk model and updated the `model_path` in the script.
2. **FFmpeg Errors**: Ensure FFmpeg is correctly installed on your system and accessible via the terminal.
3. **Performance Issues**: Ensure your audio files are mono and have a 16000 Hz sample rate. The script automatically handles this, but any deviations could cause errors.

## 🤝 Contributing

Feel free to submit pull requests or report issues. Any contributions to help improve the script are welcome!

### How to Contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📝 Contact

Created by [mrkorzun](https://github.com/mrkorzun). Feel free to reach out for feedback or questions.

---

This is an open-source project aimed at helping people automate video transcription easily with minimal setup. Contributions and suggestions are highly appreciated!

---

### Example Badges:

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green
