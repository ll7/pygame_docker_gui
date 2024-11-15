FROM python:3.11-slim
WORKDIR /workspace
RUN apt-get update
RUN apt-get install python3-pygame -y
RUN python3 -m pip install pygame imageio

ENV DISPLAY=host.docker.internal:0.0

CMD ["/usr/local/bin/python3", "simple_pygame_example.py"]