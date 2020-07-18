FROM ubuntu:latest
WORKDIR /home/python/app
COPY . .
RUN apt-get install -y python3-pip
RUN pip3 install torch==1.2.0+cpu -r https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install -r requirements.txt
RUN curl --output gpt2-pytorch_model.bin https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin
CMD ["python3", "app.py"]