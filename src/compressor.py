import imp
import shutil
import os
from json_minify import json_minify

pack_src = os.environ['PACK_SRC']
pack_dest = os.environ['PACK_DEST']
pack_name = os.environ['PACK_NAME']
minify = os.environ['MINIFY']
workspace = 'resourcepack_workspace'

# if folder or file start with dot, then ignore it.
rule = shutil.ignore_patterns(".*")

# copy resource pack from workspace directory
shutil.copytree(pack_src, workspace, ignore=rule)
if minify:
    # minify json
    for root, dirs, files in os.walk(workspace):
        for file in filter(lambda file: file.endswith(".json"), files):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
                minified = json_minify(content)
            with open(path, 'w') as f:
                f.write(minified)

# make zip archive
shutil.make_archive(os.path.join(pack_dest, pack_name), 'zip', workspace)

file_name_zip = f"{pack_name}.zip"
file_name_mcpack = f"{pack_name}.mcpack"

# rename zip to 
os.rename(os.path.join(pack_dest, file_name_zip), os.path.join(pack_dest, file_name_mcpack))
