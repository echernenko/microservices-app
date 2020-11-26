FROM python:3
COPY server.py /
RUN pip install aiohttp
CMD [ "python", "-u", "server.py" ]
