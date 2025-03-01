from fastapi import FastAPI, UploadFile
import tempfile
import whisper
import os

app = FastAPI()
model = whisper.load_model("turbo").to("cuda")

# Endpoint that recieves audio file and transcribes it with openai whisper
@app.post("/upload/")
async def upload_audio(file: UploadFile):
    # Temp path
    temp_dir = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', dir=temp_dir) as temp_file:
        # Creating temporary file
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
        
    # Process the audio with whisper
    result = model.transcribe(temp_file_path)

    # Clean up the temporary file
    os.remove(temp_file_path)

    return {"transcription": result['text']}
