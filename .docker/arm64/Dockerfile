FROM ghcr.io/jonko0493/clangd:master AS clangd

FROM skylyrac/blocksds:slim-latest

# Install clangd-21 from Jonko's ARM64 docker container build
COPY --link --from=clangd /clangd /clangd

RUN apt update && \
    apt install python3-full python3-pip ninja-build wget cmake libfreetype-dev g++ gcc unzip -y

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
# RUN git clone https://github.com/Garhoogin/ptexconv.git && \
#     cd ptexconv && \
#     make && \
#     mkdir -p /opt/wonderful/thirdparty/blocksds/external/ptexconv && \
#     mv ptexconv /opt/wonderful/thirdparty/blocksds/external/ptexconv/ptexconv && \
#     cd .. && \
#     rm -rf ptexconv

# Uncomment to install fontbm
# RUN git clone https://github.com/vladimirgamalyan/fontbm.git && \
#     cd fontbm && \
#     cmake . && \
#     make && \
#     mkdir -p /bmfont && \
#     mv fontbm /bmfont/fontbm && \
#     cd .. && \
#     rm -rf fontbm

# Install the official ARM toolchain (for gdb)
RUN ARM_TOOLCHAIN_VERSION=$(curl -s https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads | grep -Po '<h4>Version \K.+(?=</h4>)') && \
    curl -Lo gcc-arm-none-eabi.tar.xz "https://developer.arm.com/-/media/Files/downloads/gnu/${ARM_TOOLCHAIN_VERSION}/binrel/arm-gnu-toolchain-${ARM_TOOLCHAIN_VERSION}-aarch64-arm-none-eabi.tar.xz" && \
    mkdir /opt/gcc-arm-none-eabi && \
    tar xf gcc-arm-none-eabi.tar.xz --strip-components=1 -C /opt/gcc-arm-none-eabi && \
    rm gcc-arm-none-eabi.tar.xz

# Clone Maxmod and libnds sources for debugging
RUN git clone https://github.com/blocksds/maxmod && \
    git clone https://github.com/blocksds/libnds

ENTRYPOINT [ "/bin/bash" ]