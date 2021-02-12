FROM python:3

COPY server.py ./

CMD ["python3","./server.py"]
