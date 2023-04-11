# Import #
import io
import os
import shutil
import zipfile
import yaml

# Input #
author = input("Type in the Note Designer: ")

if author in os.listdir("./temp"):
    maxF = [int(f.split(":")[1]) for f in os.listdir("./temp") if (author in f) and (":" in f)]
    tempFolder = f"./temp/{author}:{max(maxF)+1 if maxF else '1'}"
else:
    tempFolder = f"./temp/{author}"

index = [
    {
        "directory": f"{author}_pack",
        "identifier": f"com.{author}.pack",
        "settingsFile": "pack.yml",
        "version": 0,
        "type": "pack"
    }
]
pack = {
    "imagePath": "pack.png",
    "levelIdentifiers": [],
    "packName": f"{author} Pack"
}


for file in os.listdir("input"):
    if file.endswith(".arcpkg"):
        with zipfile.ZipFile(f"input/{file}") as zip_ref:
            with zip_ref.open("index.yml") as index_ref:
                data = yaml.safe_load(index_ref)
                pack["levelIdentifiers"].append(data[0]["identifier"])
                index.append(data[0])
            zip_ref.extractall(tempFolder)

# Write YAML file #
with io.open(f"{tempFolder}/index.yml", "w", encoding="utf8") as outfile:
    yaml.dump(index, outfile, default_flow_style=False, allow_unicode=True)

# Write Pack file #
os.mkdir(f"{tempFolder}/{author}_pack")
with io.open(f"{tempFolder}/{author}_pack/pack.yml", "w", encoding="utf8") as outfile:
    yaml.dump(pack, outfile, default_flow_style=False, allow_unicode=True)
if "pack.png" in os.listdir("./input"):
    shutil.copyfile("./input/pack.png", f"{tempFolder}/{author}_pack/pack.png")
else:
    shutil.copyfile("./default.png", f"{tempFolder}/{author}_pack/pack.png")

shutil.make_archive(f"./output/{author}_pack.arcpkg", 'zip', tempFolder)

print("Done.")
