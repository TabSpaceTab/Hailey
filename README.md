# Hailey
For the Writers who need assistance.

## Installation of prerequisites

 ```shell
$ git clone https://github.com/TabSpaceTab/Hailey.git && cd Hailey
$ pip3 install -r requirements.txt
# download huggingface's pytorch model for Linux based OS
$ curl --output gpt2-pytorch_model.bin https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin
# Download huggingface's pytorch model for Windows
$ curl -o gpt2-pytorch_model.bin https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin
# To execute the code
$ python3 app.py
# NOTE:
Windows users will have to make the following changes to the app.py file.
cmd = 'python printer.py --text "%s" --quiet "-"'%(option) from cmd = 'python3 printer.py --text "%s" --quiet "-"'%(option)
```

## Edit Oct 5: Did it wayyyy before it was cool :grin:

## Acknowledgement

[Tae-Hwan Jung(@graykode)](https://github.com/graykode)
[OpenAI(@openai)](https://github.com/oepnai)
[Google-Research(@google-research)](https://github.com/google-research)
and yeah
![](https://media.giphy.com/media/ThpMkGy7mFr12th14M/giphy.gif)
