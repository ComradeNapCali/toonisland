# Toon Island Contributing Document 🔨 

## 💻 Windows
### Easy Way
1. Clone the main [toonisland](https://github.com/toonisland/toonisland) repo with submodules.
2. Download a precompiled TIA **Panda3D** from **[here](https://drive.google.com/file/d/1ZFpg7aBVhBCXh7Xg1YSG2JYEZI8L4tPg/view?usp=sharing)** and install it.
3. Download a precompiled **LibpandaDNA** from **[here](https://drive.google.com/file/d/1719bHjdnivooJy_jn3OJKzSkFsYOGUCA/view?usp=sharing)** and add it to **dependenices/panda/windows** in the main source code.
4. **Optional**, Download a set of precompiled LibDisney binaries from [here](https://drive.google.com/file/d/1lxkT1P-9aXNB76oqPtPBUDefwnYsRaF4/view?usp=sharing) and add it to **tools/leveleditor** folder if you plan to use the level editor.
8. Run **start_win32.bat** in the main [toonisland](https://github.com/toonisland/toonisland) repo

### Correct Way
1. Clone the main [toonisland](https://github.com/toonisland/toonisland) repo with submodules.
2. Clone the [panda3d](https://github.com/toonisland/panda3d) repo.
3. Clone the [libpandadna](https://github.com/toonisland/libpandadna) repo.
4. Clone the [libdisney](https://github.com/toonisland/libdisney) repo.
5. Run the **build_win32.bat** in the [panda3d](https://github.com/toonisland/panda3d) repo followed by the **install_win32.bat**.
6. Run the **build_win32.bat** in the [libpandadna](https://github.com/toonisland/libpandadna) repo and copy contents of the bin folder to **dependenices/panda/windows**.
7. Run the **build_win32.bat** in the [libdisney](https://github.com/toonisland/libdisney) repo and copy contents of the **build/cmake/otp/Release** and **build/cmake/toontown/Release** folder to the root of the **tools/leveleditor** folder.
8. Run **start_win32.bat** in the main [toonisland](https://github.com/toonisland/toonisland) repo

## 🍎 MacOS
TBA

## 🐧 Linux
TBA
