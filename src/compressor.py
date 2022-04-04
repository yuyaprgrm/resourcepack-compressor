import imp
import shutil
import os

pack_src = os.environ['PACK_SRC']
pack_dist = os.environ['PACK_DIST']
pack_name = os.environ['PACK_NAME']
workspace = 'resourcepack_workspace'

# if folder or file start with dot, then ignore it.
rule = shutil.ignore_patterns(".*")

# copy resource pack from workspace directory
shutil.copytree(pack_src, workspace, ignore=rule)

# make zip archive
shutil.make_archive(pack_dist, 'zip', workspace)

file_name_zip = f"{pack_name}.zip"
file_name_mcpack = f"{pack_name}.mcpack"

# rename zip to 
os.rename(os.path.join(pack_dist, file_name_zip), os.path.join(pack_dist, file_name_mcpack))
