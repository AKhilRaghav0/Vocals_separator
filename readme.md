# Voice Separator Script (v4) README

This repository contains a Python script for separating vocals from an audio input using a pre-trained model. The script is designed to work with audio files and uses the "demucs" model for source separation. It is built with Gradio, a web-based interface that allows users to interact with the script easily.

## How to Use

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running: `pip install gradio scipy`.
3. Ensure you have Python 3 installed on your system.

## Running the Script Locally

Once you have set up the environment, you can run the script on your local machine using the following command:

```bash
python vocal_separator.py
```

## Source Separation

The script's purpose is to separate the vocals from an input audio file. To use the script, follow these steps:

1. Launch the script.
2. Upload an audio file containing vocals.
3. Wait for the script to process the audio.
4. The script will return two audio files: one with the isolated vocals and one with the instrumental part.

## Colab (GPU Runtime)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/AKhilRaghav0/069cd9af13fca6e17a403db93e7b586e/vocals_seperator.ipynb)

Click the badge above to access the Colab notebook with GPU runtime and use the script interactively.

## HuggingFace (CPU Runtime)

[![Hugging Face Model](https://img.shields.io/badge/Hugging%20Face-Model%20Hub-blue)](https://huggingface.co/spaces/HawkEye098432/Vocals_seperator)

Click the badge above to access the script in HuggingFace with CPU runtime.

## Note

Please ensure that you have enough system resources to run the script, especially when using the GPU runtime in Colab. Larger audio files or complex models may require more memory and processing power.

Feel free to experiment with different audio files and models to explore various source separation results.

### About the Model

The script uses the "demucs" model for source separation, specifically targeting vocals. The model may have been trained on a large dataset to effectively separate vocals from instrumental sounds. If you are interested in the model details or training data, you can refer to the original "demucs" repository or model documentation.

Happy voice separation!
