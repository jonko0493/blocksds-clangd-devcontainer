from architectds import *
import json
import os
import subprocess
import sys

argv = sys.argv

arm9 = Arm9Binary(
    sourcedirs=['src/arm9'],
    libs=['nds9'],
    defines=[],
    cflags='-g',
    cxxflags='-g -Og -Werror -Wno-psabi -fpermissive -std=gnu++20',
    libdirs=['${BLOCKSDS}/libs/libnds']
)
arm9.generate_elf()

# arm7 = Arm7Binary(
#     sourcedirs=['src/arm7'],
#     libs=['nds7', 'dswifi7'],
#     defines=[],
#     cflags='',
#     cxxflags='-Os -Werror -Wno-psabi -fpermissive',
#     libdirs=['${BLOCKSDS}/libs/libnds', '${BLOCKSDS}/libs/dswifi']
# )
# arm7.generate_elf()

nds = NdsRom(
    binaries=[arm9],
    nds_path="blocksds-container.nds",
    game_title='Sample BlocksDS Devcontainer',
    game_subtitle='2025',
    game_author='Jonko'
)
nds.generate_nds()

nds.run_command_line_arguments(args=argv)

# Create compile_commands.json for use by clangd
# Create compile_commands.json for use by clangd
with open('compile_commands.json', 'w+') as cc:
    subprocess.call(['ninja', '-t', 'compdb'], stdout=cc)