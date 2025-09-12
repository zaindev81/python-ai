FROM ubuntu:22.04

# Install required network tools and Python
RUN apt-get update && apt-get install -y \
    iproute2 \
    iputils-ping \
    bridge-utils \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# Create /app directory
RUN mkdir -p /app

# Set working directory
WORKDIR /app


# Default command when container starts
CMD ["/bin/bash"]