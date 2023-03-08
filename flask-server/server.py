from flask import Flask
import os
import whisper
from pytube import YouTube
import gradio as gr

app = Flask(__name__)

model = whisper.load_model("base")
ytURL = "https://www.youtube.com/watch?v=sagpI6DSgeE"

# Members API Route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2","Member3"]}

@app.route("/members2")
def members2():
    return {"members": ["Member3", "Member4","Member5"]}

@app.route("/transcript")
def getTranscript():
  yt = YouTube("https://www.youtube.com/watch?v=sagpI6DSgeE")
  video = yt.streams.filter(only_audio=True).first()
  out_file=video.download(output_path=".")
  base, ext = os.path.splitext(out_file)
  new_file = base+'.mp3'
  os.rename(out_file, new_file)
  result = model.transcribe(new_file)
  output = result['text'].strip()
  os.remove(new_file)
  return output

if __name__ == "__main__":
    app.run(host="https://transcriptai.connectup.cloud/", port=5050)