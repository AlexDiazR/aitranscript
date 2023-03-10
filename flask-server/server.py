from flask import Flask
import os
import whisper
from pytube import YouTube
import gradio as gr
import re

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
  title = yt.title
  forbChar = {"/",":","?","<",">","|"}
  for char in forbChar:
     title = title.replace(char," ")
  title = " ".join(title.split())
  # title = re.sub("/|\|:|*|?|<|>"," ",yt.title)
  video = yt.streams.filter(only_audio=True).first()
  out_file=video.download(output_path=".")
  base, ext = os.path.splitext(out_file)
  new_file = base+'.mp3'
  os.rename(out_file, new_file)

  audio = whisper.load_audio(new_file)
  audio = whisper.pad_or_trim(audio)
  mel = whisper.log_mel_spectrogram(audio).to(model.device)
  # _, probs = model.detect_language(mel)
  # print(f"Detected language: {max(probs, key=probs.get)}")
  # options = whisper.DecodingOptions(fp16 = False,language='en')
  # result = whisper.decode(model, mel, options)

  result = model.transcribe(new_file, verbose=True)
  output = result['text']
  stamps = result['segments']
  output2 = ''
  for x in stamps:
    output2 += '\n' + x['text']
  print(output2)
  os.remove(new_file)
  with open(f"{title} - Transcript.txt", "w") as f:
    f.write(f"Transcription of video {title}\n")
    f.write(output2)
  return output2

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)