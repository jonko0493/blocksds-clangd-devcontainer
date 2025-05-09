FROM skylyrac/blocksds:slim-latest

RUN apt update && \
    apt install -y wget unzip python3-full python3-pip ninja-build

# Install clangd-21 from official snapshot build
RUN wget https://github.com/clangd/clangd/releases/download/snapshot_20250504/clangd-linux-snapshot_20250504.zip && \
    unzip clangd-linux-snapshot_20250504.zip && \
    mv clangd_snapshot_20250504 /clangd && \
    rm clangd-linux-snapshot_20250504.zip

# Install the official ARM toolchain (for gdb)
RUN ARM_TOOLCHAIN_VERSION=$(curl -s https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads | grep -Po '<h4>Version \K.+(?=</h4>)') && \
    curl -Lo gcc-arm-none-eabi.tar.xz "https://developer.arm.com/-/media/Files/downloads/gnu/${ARM_TOOLCHAIN_VERSION}/binrel/arm-gnu-toolchain-${ARM_TOOLCHAIN_VERSION}-x86_64-arm-none-eabi.tar.xz" && \
    mkdir /opt/gcc-arm-none-eabi && \
    tar xf gcc-arm-none-eabi.tar.xz --strip-components=1 -C /opt/gcc-arm-none-eabi && \
    rm gcc-arm-none-eabi.tar.xz

# Installs ArchitectDS
# Comment this out (and remove python and ninja from the apt install above) if you would rather use a different build system,
# but be aware that you will have to generate your compile_commands.json yourself if you decide to do that
RUN git clone https://github.com/AntonioND/architectds.git && \
    cd ./architectds && \
    pip3 install wheel setuptools --break-system-packages && \
    python3 setup.py bdist_wheel && \
    pip3 install dist/architectds-*-py3-none-any.whl --break-system-packages && \
    cd ../ && \
    rm -rf architectds

# Uncomment the to install Nitro Engine
# RUN wf-pacman -Sy --noconfirm blocksds-nitroengine

# Uncomment to install NFLib
# RUN wf-pacman -Sy --noconfirm blocksds-nflib

# Uncomment to install ptexconv
# RUN wget https://github.com/Garhoogin/ptexconv/releases/download/v1.5.0.1/ptexconv_linux_x64 && \
#     mkdir -p /opt/wonderful/thirdparty/blocksds/external/ptexconv && \
#     mv ptexconv_linux_x64 /opt/wonderful/thirdparty/blocksds/external/ptexconv/ptexconv && \
#     chmod +x /opt/wonderful/thirdparty/blocksds/external/ptexconv/ptexconv

# Uncomment to install fontbm
# RUN wget https://github.com/vladimirgamalyan/fontbm/releases/download/v0.6.1/fontbm && \
#     mkdir -p /bmfont && \
#     mv fontbm /bmfont/fontbm && \
#     chmod +x /bmfont/fontbm

# Clone Maxmod and libnds sources for debugging
RUN git clone https://github.com/blocksds/maxmod && \
    git clone https://github.com/blocksds/libnds

ENTRYPOINT [ "/bin/bash" ]