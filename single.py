# Import #
import io
import os
import shutil
import zipfile
import yaml

# Input #
PackName = input("Type in the Pack Name: ")
author = input("Type in the Note Designer: ")
tempDir, inputDir, outputDir, defaultPng = [os.path.join(os.getcwd(), i) for i in ["temp", "input", "output", "default.png"]]


# Setting up temp folder #
if author in os.listdir(tempDir):
    maxF = [int(f.split(":")[1]) for f in os.listdir(tempDir) if (author in f) and (":" in f)]
    tempFolder = os.path.join(tempDir, f"{author}:{max(maxF)+1 if maxF else '1'}")
else:
    tempFolder = os.path.join(tempDir, author)

directory = f"{author}_{PackName.replace(' ', '')}"f"{author}_{PackName.replace(' ', '')}"

# Init yml #
index = [
    {
        "directory": directory,
        "identifier": f"com.{author}.{PackName.replace(' ', '')}.pack",
        "settingsFile": "pack.yml",
        "version": 0,
        "type": "pack"
    }
]
pack = {
    "imagePath": "pack.png",
    "levelIdentifiers": [],
    "packName": PackName
}


for file in os.listdir(inputDir):
    if file.endswith(".arcpkg"):
        with zipfile.ZipFile(os.path.join(inputDir, file)) as zip_ref:
            with zip_ref.open("index.yml") as index_ref:
                data = yaml.safe_load(index_ref)
                pack["levelIdentifiers"].append(data[0]["identifier"])
                index.append(data[0])
                print(f"Processing {data[0]['directory']}")
            zip_ref.extractall(tempFolder)

# Write YAML file #
with io.open(os.path.join(tempFolder, "index.yml"), "w", encoding="utf8") as outfile:
    yaml.dump(index, outfile, default_flow_style=False, allow_unicode=True)

# Write Pack file #
os.mkdir(os.path.join(tempFolder, directory))
with io.open(os.path.join(tempFolder, directory, "pack.yml"), "w", encoding="utf8") as outfile:
    yaml.dump(pack, outfile, default_flow_style=False, allow_unicode=True)
if "pack.png" in os.listdir(inputDir):
    shutil.copyfile(os.path.join(inputDir, "pack.png"), os.path.join(tempFolder, directory, "pack.png"))
else:
    shutil.copyfile(defaultPng, os.path.join(tempFolder, directory, "pack.png"))

print("Compressing...")
shutil.make_archive(os.path.join(outputDir, f"{directory}.arcpkg"), 'zip', tempFolder)

print("Done.")
