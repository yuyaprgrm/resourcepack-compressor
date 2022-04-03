import imp
import shutil
import os

workspace = os.environ['GITHUB_WORKSPACE']
pack_path = os.environ['PACK_PATH']
pack_name = os.environ['PACK_NAME']

resource_pack_path = os.path.join(workspace, 'resource_pack', pack_path)
resource_pack_filtered_path = os.path.join(workspace, 'resource_pack_filtered')

# if folder or file start with dot, then ignore it.
rule = shutil.ignore_patterns(".*")

# copy resource pack from workspace directory
shutil.copytree(resource_pack_path, resource_pack_filtered_path, ignore=rule)

# make zip archive
file_name_zip = shutil.make_archive(os.path.join(workspace, pack_name), 'zip', resource_pack_filtered_path)
file_name_mcpack = f"{pack_name}.mcpack"

print(f"archive was created in {file_name_zip}")

# rename zip to 
os.rename(file_name_zip, file_name_mcpack)
