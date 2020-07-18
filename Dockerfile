FROM python
WORKDIR /home/python/app
COPY . .
RUN pip3 install -r requirements.txt
RUN curl --output gpt2-pytorch_model.bin https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin
CMD ["python3", "app.py"]