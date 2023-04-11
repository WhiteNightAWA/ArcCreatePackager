# ArcCreate Packager <sub>v0.3</sub>
A small tool to pack multi song together for ArcCreate.
(I'm not sure that if this against the rules of ArcCreate... If it do, plz content me to tell me to delete this.)
---

## How to use?
## A: Single Mode
#### 0.5. Clone this repository or you can only copy `single.py` and `default.png`, make sure your computer has Python(>3.7) installed.
### 1. Copy all song file(endswith `.arcpkg`) into `./input` folder.
### 2. Run `single.py`.
#### 2.5. Drop the image(png) of the pack into `./input` and rename it to `pack.png`, if no image found, `default.png` will be used.
### 3. Enter the name of the Pack Name and the Note Designer.
### 4. The pack (endswith `.arcpkg.zip`) will appear in `./output`.
### 5. Import the zip file in ArcCreate App, the Song Pack should appear.

## B: Multi Mode
#### 0.5. Clone this repository or you can only copy `multi.py` and `default.png`, make sure your computer has Python(>3.7) installed.
### 1. Copy all folder / create a folder which name by the Note Designer and their song file(endswith `.arcpkg`) in that folder. (if you need custom pack image plz also place in that folder (png only))
### 2. Run `multi.py`.
### 3. All the pack (endswith `.arcpkg.zip`) will appear in `./output`.
### 4. Import the zip file in ArcCreate App, the Song Pack should appear.

---
## Remind
### - You can clear the cache file by delete all files and folders in `./temp`
### - Remember to clear the input folder after every time you use it.
### - It is welcome to create any PR and Issues

## Problems:
### - [#1](https://github.com/WhiteNightAWA/ArcCreatePackager/issues/1)
