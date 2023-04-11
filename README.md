# ArcCreate Packager <sub>v0.1</sub>
A small tool to pack mutil song together for ArcCreate.

---

## How to use?
## A: Single Mode
### 1. Drop all song file (endswith `.arcpkg`) into `./input` folder.
#### 1.5. Install package `pyyaml` by using command `pip install pyyaml`.
### 2. Run `single.py`.
#### 2.5. Drop the image(png) of the pack into `./input` and rename it to `pack.png`, if no image found, `default.png` will be used.
### 3. Enter the name of the Note Designer and hit Enter.
### 4. The pack (endswith `.arcpkg.zip`) will show up in `./output`.
### 5. Import the zip file in ArcCreate App, the Song Pack should appear.

## B: Multi Mode (in process)

---
## Remind
### - You can clear the cache file by delete all files and folders in `./temp`
### - Remember to clear the input folder after every time you use it.
### - It is welcome to create any PR and Issues

## Problems:
### - Trying to get rid of `pyypaml`
