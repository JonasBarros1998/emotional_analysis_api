FROM python:3.8.2
COPY . /home/jonas/Code
WORKDIR /home/jonas/Code
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
