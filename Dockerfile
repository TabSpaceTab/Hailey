FROM ubuntu:latest
WORKDIR /home/python/app
COPY . .
RUN apt-get update -y 
RUN apt-get install -y curl
RUN apt-get install -y python3-pip
RUN apt-get install gunicorn
RUN pip3 install torch==1.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install -r requirements.txt
RUN curl --output gpt2-pytorch_model.bin https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin
CMD ["gunicorn", "app:app"]
