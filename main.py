from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import whisper
import os

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",    # Change with your frontend URL
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    print(result['text'])
    return {"transcription": result['text']}
