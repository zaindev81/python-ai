FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    iproute2 \
    iputils-ping \
    bridge-utils \
    iptables \
    tcpdump \
    conntrack \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN mkdir -p /app

WORKDIR /app

CMD ["/bin/bash"]