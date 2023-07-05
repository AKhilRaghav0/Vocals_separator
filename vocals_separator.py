import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals  test.wav -o out")
  return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/no_vocals.wav"

title = "Source Separation (v4)"

gr.Interface(
    inference,
    gr.Audio(type="numpy", label="Input"),
    [gr.Audio(type="filepath", label="Vocals"),gr.Audio(type="filepath", label="No Vocals / Instrumental")],
    title=title,
    ).launch(enable_queue=True)
