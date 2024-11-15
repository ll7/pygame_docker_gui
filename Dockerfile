FROM python:3.12
WORKDIR /workspace
RUN "echo" "ls"
RUN apt update
RUN apt install python3-pip -y
RUN python3 -m pip install -r ./requirements.txt

ENV DISPLAY=host.docker.internal:0.0

CMD ["/usr/local/bin/python3", "simple_pygame_example.py"]