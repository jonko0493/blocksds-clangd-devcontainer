from architectds import *
import json
import os
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
compile_commands = []
for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.c') or file.endswith('.cpp'):
            compile_commands.append({
                "directory": os.getcwd(),
                # Swap to the first line if you're using a custom ARM7 binary
                # "arguments": f"/opt/wonderful/toolchain/gcc-arm-none-eabi/bin/arm-none-eabi-g{'cc' if file.endswith('.c') else '++'} -mthumb -fno-exceptions -fno-rtti -ffunction-sections -fdata-sections {(arm7.cflags if "arm7" in root else arm9.cflags) if file.endswith('.c') else (arm7.cxxflags if "arm7" in root else arm9.cxxflags)} -MMD -MP -c -o {os.getcwd()}/build/{root[4:]}/{file}.o {os.getcwd()}/{root}/{file}".split(' '),
                "arguments": f"/opt/wonderful/toolchain/gcc-arm-none-eabi/bin/arm-none-eabi-g{'cc' if file.endswith('.c') else '++'} -mthumb -fno-exceptions -fno-rtti -ffunction-sections -fdata-sections {arm9.cflags if file.endswith('.c') else arm9.cxxflags} -MMD -MP -c -o {os.getcwd()}/build/{root[4:]}/{file}.o {os.getcwd()}/{root}/{file}".split(' '),
                "file": f'{os.getcwd()}/{root}/{file}'
            })
with open('compile_commands.json', 'w+') as f:
    json.dump(compile_commands, f)