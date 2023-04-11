# Import #
import io
import os
import shutil
import zipfile
import yaml

# Input #
print("Program starting...")
tempDir, inputDir, outputDir, defaultPng = [os.path.join(os.getcwd(), i) for i in
                                            ["temp", "input", "output", "default.png"]]

def makePack(path):
    tempDir, inputDir, outputDir, defaultPng = [os.path.join(os.getcwd(), i) for i in
                                                ["temp", "input", "output", "default.png"]]
    inputDir = os.path.join(inputDir, path)

    author = path

    # Setting up temp folder #
    if author in os.listdir(tempDir):
        maxF = [int(f.split(":")[1]) for f in os.listdir(tempDir) if (author in f) and (":" in f)]
        tempFolder = os.path.join(tempDir, f"{author}:{max(maxF)+1 if maxF else '1'}")
    else:
        tempFolder = os.path.join(tempDir, author)

    # Init yml #
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


    for file in os.listdir(inputDir):
        if file.endswith(".arcpkg"):
            with zipfile.ZipFile(os.path.join(inputDir, file)) as zip_ref:
                with zip_ref.open("index.yml") as index_ref:
                    data = yaml.safe_load(index_ref)
                    pack["levelIdentifiers"].append(data[0]["identifier"])
                    index.append(data[0])
                zip_ref.extractall(tempFolder)

    # Write YAML file #
    with io.open(os.path.join(tempFolder, "index.yml"), "w", encoding="utf8") as outfile:
        yaml.dump(index, outfile, default_flow_style=False, allow_unicode=True)

    # Write Pack file #
    os.mkdir(os.path.join(tempFolder, f"{author}_pack"))
    with io.open(os.path.join(tempFolder, f"{author}_pack", "pack.yml"), "w", encoding="utf8") as outfile:
        yaml.dump(pack, outfile, default_flow_style=False, allow_unicode=True)
    if "pack.png" in os.listdir(inputDir):
        shutil.copyfile(os.path.join(inputDir, "pack.png"), os.path.join(tempFolder, f"{author}_pack", "pack.png"))
    else:
        shutil.copyfile(defaultPng, os.path.join(tempFolder, f"{author}_pack", "pack.png"))

    print(f"Processing {path}...", end="")
    shutil.make_archive(os.path.join(outputDir, f"{author}_pack.arcpkg"), 'zip', tempFolder)
    print("Done.")


for folder in os.listdir(inputDir):
    if os.path.isdir(os.path.join(inputDir, folder)):
        makePack(folder)

print("All Done.")
