# Fast Whisper
 An API designed to run OpenAI Whisper locally on your device. The /upload/ endpoint expects a file and it returns the transcription of the audio.

## Requirements
I've made this API with Python 3.12. To run it you first need to install some requirements.

First you need to install PyTorch and make sure it's enabled with CUDA. Please check the official [NVidia site](https://developer.nvidia.com/cuda-zone) and [PyTorch site](https://pytorch.org/get-started/locally/) to run a clean installation of them.

You can check if it was installed correctly by running the following script:

```python
import torch
print(torch.cuda.is_available())
```

Then you'll need to install OpenAI Whisper. You can do so by running these commands:

```bash
pip install -U openai-whisper
```

You'll also need to have the command-line tool ffmpeg. Check the [Whisper Github](https://github.com/openai/whisper) for more information. I installed with Chocolatey using following command. 

```bash
choco install ffmpeg
```

Finally, you'll need to install FastAPI to host the endpoints.

```bash
pip install "fastapi[standard]"
```

## Running the API
You can locally host the API quickly by running [fast_whisper.bat](./fast_whisper.bat). The server will run on the port 8200, but you can change it by editing the ```--port``` parameter of the bat. Afterwards, you can send a POST request to ```http://localhost:8200/upload/``` with a file in it's form-data to recieve the transcsription.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
