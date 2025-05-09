# BlocksDS Devcontainer with clangd

The clangd VS Code extension is far superior to the default cpptools one that Microsoft ships but it was
quite a bit of work for me to set it up to work with BlocksDS. I did eventually get it working, and this repo
is the result of that.

Make sure to copy everything from this repo except the license and README to your repository and then customize the
Docker images for your project. Launch the devcontainer for your platform &ndash; amd64 for x86_64 machines and arm64
for ARM ones. Then just start developing and enjoy the rich intellisense, code completion, and linting that clangd has to offer. 😎

## What Is in the Devcontainer?
The `devcontainer.json` files in the `.devcontainer` directory define plugins and Docker permissions for each configuration (AMD64 or ARM64). The two Dockerfiles in the `.docker` directory define
the contents of the images for each configuration. The devcontainers definitions are essentially the same except for pointing to the two different Dockerfiles, but the Dockerfiles themselves do radically
different things in order to arrive at the same end result container for each architecture.

When expanding your build system, it is important to keep parity between the two architectures in mind. If you plan to dev on a computer running modern macOS (Apple Silicon), a recent Microsoft Surface or other
laptop running Windows on ARM, or are using Asahi Linux or a similar ARM Linux distro, you should make sure you maintain the ARM64 Docker image. If you dev on multiple machines and one of them is x64-based,
you will need to maintain them both.

### Plugins
We install the following plugins:
* `llvm-vs-code-extensions.vscode-clangd` &mdash; This is the star of the show, the clangd extension for VS Code that provides the core functionality
* `ms-azuretools.vscode-docker` &mdash; This is a plugin for editing Dockerfiles which will come in handy as you iterate on what you want in your devcontainer
* `ms-python.python` &mdash; The Python extension; this repo is set up to use ArchitectDS which uses Python for its build scripts
* `ms-vscode.cpptools` and `ms-vscode.cpptools-extension-pack` &mdash; While we turn off Intellisense for these so the majority of their functionality is not used, we do need the official Microsoft VS code extensions for debugging with gdb!
* `ms-vscode.hexeditor` &mdash; The hex editor extension allows us to view memory captures easily while debugging with gdb

### Container Permissions
The Docker container runs as privileged and adds the `host.docker.internal` host gateway so that the container can connect to melonDS's gdb stub running outside of your container.

### Docker Image
The Dockerfiles are intended to be customized; many lines can be uncommented to add more development tools and SDKs to the container and you can of course add your own tools by defining them in the Dockerfile as well.

By default, container images have:
* [BlocksDS](https://blocksds.skylyrac.net/docs/) &mdash; The images are based on the BlocksDS images
* [Clangd-21](https://clangd.llvm.org/) &mdash; Version 21 of clangd supports the features necessary to get it working properly with BlocksDS
* [ArchitectDS](https://github.com/AntonioND/architectds/) &mdash; This fantastic build system from AntonioND is used not only to build the ROM but also to generate the compile_commands.json file necessary for making clangd work properly. If you opt not to use it, ensure you generate that file by some other means.
* [Arm GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) &mdash; The toolchain is installed alongside the Wonderful toolchain because it has arm-none-eabi-gdb which is necessary for debugging programs
* [libnds](https://github.com/blocksds/libnds) and [Maxmod](https://github.com/blocksds/maxmod) sources &mdash; The sources for these libraries are included to make the debugging experience better

Additionally, you can enable the following tools/SDKs by simply uncommenting the relevant lines in the Dockerfiles:
* [Nitro Engine](https://github.com/AntonioND/nitro-engine/) &mdash; A fantastic library from AntonioND for managing the 3D hardware of the Nintendo DS
* [NFLib](https://github.com/knightfox75/nds_nflib) &mdash; An excellent library from NightFox for managing the 2D hardware of the Nintendo DS
* [ptexconv](https://github.com/Garhoogin/ptexconv) &mdash; A wonderful utility from Garhoogin for converting standard image formats into common DS formats; particularly useful if you want to use 4x4 compressed textures
* [fontbm](https://github.com/vladimirgamalyan/fontbm) &mdash; A beautiful tool from Vladimir Gamalyan for creating bitmap fonts for use with NitroEngine's [libdsf](https://github.com/AntonioND/libdsf)

Simply uncomment whatever you need and build the devcontainer to get started!

## Customizing clangd
You can suppress any clangd warnings you want to ignore by adding them to the `Diagnostics: Suppress:` section of the `.clangd` file. Additional information on this configuration file can be found [here](https://clangd.llvm.org/config.html).