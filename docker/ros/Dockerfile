FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04


ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt upgrade -y

RUN apt-get install software-properties-common -y

ARG DEBIAN_FRONTEND=noninteractive
RUN add-apt-repository universe &&\
    add-apt-repository restricted &&\
    add-apt-repository multiverse

RUN apt-get update

RUN apt-get install -y gnupg2 lsb-core vim wget python3-pip libpng16-16 libjpeg-turbo8 libtiff5 curl


# Installing ROS-noetic

ENV ROS_DISTRO=noetic
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -
RUN apt update
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN apt -y install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
RUN apt install -y ros-${ROS_DISTRO}-desktop python3-catkin python3-catkin-tools
RUN apt-get install -y python3-rosdep
RUN rosdep init
RUN rosdep update


RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bash_profile


RUN apt-get install -y \
        # Base tools
        cmake \
        build-essential \
        git \
        unzip \
        pkg-config \
        python3-dev \
        # OpenCV dependencies
        python3-numpy \
        # Pangolin dependencies
        libgl1-mesa-dev \
        libglew-dev \
        libeigen3-dev \
        apt-transport-https \
        ca-certificates\
        software-properties-common \
	nano \
	tmux

# Build OpenCV
RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
RUN apt-get install -y libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
RUN apt-get install -y libgtk-3-dev

RUN cd /tmp && git clone https://github.com/opencv/opencv.git && \
    cd opencv && \
    git checkout 4.4.0 && \
    mkdir build && cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D BUILD_EXAMPLES=OFF  -D BUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_TESTS=OFF -D CMAKE_INSTALL_PREFIX=/usr/local .. && \
    make -j$nproc && make install && \
    cd / && rm -rf /tmp/opencv

RUN useradd -m -s /bin/bash -G sudo eduardo

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> \
    /etc/sudoers

USER eduardo

WORKDIR /home/eduardo
CMD /bin/bash

# nvidia-docker run -it -h lianli -v /home/$USERNAME/:/home/chatgpt/ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY
