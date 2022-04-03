import imp
import shutil
import os

workspace = os.environ.get('GITHUB_WORKSPACE')
pack_path = os.environ.get('PACK_PATH')
pack_name = os.environ.get('PACK_NAME')

resource_pack_path = os.path.join(workspace, pack_path, 'resource_pack')
resource_pack_filtered_path = os.path.join(workspace, 'resource_pack_filtered')

# if folder or file start with dot, then ignore it.
rule = shutil.ignore_patterns(".*")

# copy resource pack from workspace directory
shutil.copytree(resource_pack_path, resource_pack_filtered_path, ignore=rule)

# make zip archive
shutil.make_archive(pack_name, 'zip', resource_pack_filtered_path)

file_name_zip = os.path.join(workspace, f"{pack_name}.zip")
file_name_mcpack = os.path.join(workspace, f"{pack_name}.mcpack")

# rename zip to 
os.rename(file_name_zip, file_name_mcpack)
