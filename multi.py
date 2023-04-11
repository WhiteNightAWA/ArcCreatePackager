# Import #
import io
import os
import shutil
import zipfile

# Input #
print("Program starting...")
tempDir, inputDir, outputDir, defaultPng = [os.path.join(os.getcwd(), i) for i in
                                            ["temp", "input", "output", "default.png"]]

def makePack(path):
    tempDir, inputDir, outputDir, defaultPng = [os.path.join(os.getcwd(), i) for i in
                                                ["temp", "input", "output", "default.png"]]
    inputDir = os.path.join(inputDir, path)

    author = path
    PackName = author

    # Setting up temp folder #
    if author in os.listdir(tempDir):
        maxF = [int(f.split(":")[1]) for f in os.listdir(tempDir) if (author in f) and (":" in f)]
        tempFolder = os.path.join(tempDir, f"{author}:{max(maxF) + 1 if maxF else '1'}")
    else:
        tempFolder = os.path.join(tempDir, author)

    directory = f"{author}_{PackName.replace(' ', '')}"

    # Init yml #
    index = f"""- directory: {directory}
      identifier: com.{author}.{PackName.replace(' ', '')}.pack
      settingsFile: pack.yml
      version: 0
      type: pack
    """
    levelIdentifiers = ['']

    for file in os.listdir(inputDir):
        if file.endswith(".arcpkg"):
            with zipfile.ZipFile(os.path.join(inputDir, file)) as zip_ref:
                zip_ref.extractall(tempFolder)
                with open(os.path.join(tempFolder, "index.yml")) as index_ref:
                    data = index_ref.read()
                    levelIdentifiers.append(data.split("identifier: ")[1].split()[0])
                    index += data

    # Write YAML file #
    with io.open(os.path.join(tempFolder, "index.yml"), "w", encoding="utf8") as outfile:
        outfile.write(index)

    pack = f"""imagePath: pack.png
    levelIdentifiers:""" + "\n- ".join(levelIdentifiers) + f"\npackName: {PackName}"

    # Write Pack file #
    os.mkdir(os.path.join(tempFolder, directory))
    with io.open(os.path.join(tempFolder, directory, "pack.yml"), "w", encoding="utf8") as outfile:
        outfile.write(pack)
    if "pack.png" in os.listdir(inputDir):
        shutil.copyfile(os.path.join(inputDir, "pack.png"), os.path.join(tempFolder, directory, "pack.png"))
    else:
        shutil.copyfile(defaultPng, os.path.join(tempFolder, directory, "pack.png"))

    print(f"Processing {path}...", end="")
    shutil.make_archive(os.path.join(outputDir, f"{directory}.arcpkg"), 'zip', tempFolder)
    print("Done.")


for folder in os.listdir(inputDir):
    if os.path.isdir(os.path.join(inputDir, folder)):
        makePack(folder)

print("All Done.")
