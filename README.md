# Mini example for using pygame in WSL 2 docker environment

## Prerequisites

- Windows 11

## Installation

1. Install WSL 2
2. Install Ubuntu 24.04 as WSL 2 distro
3. Install Docker Desktop
4. Enable WSL 2 integration in Docker Desktop for your distro
   1. https://docs.docker.com/desktop/features/wsl/
5. clone repository
6. `docker compose -f docker-compose.yml up --build`

## Tests to run for intermediate steps

### gui test

```bash
sudo apt install x11-apps
xeyes
```

### nvidia-smi test

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
