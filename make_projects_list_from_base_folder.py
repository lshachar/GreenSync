# GreenSync by Shachar Liberman
# https://github.com/lshachar/GreenSync
# Published under GNU GPLv3
# Enjoying GreenSync? please show me your love -  https://paypal.me/lshachar  :)

# This script populates the list of projects inside greensync_config.yaml
# Useful when a user have a large number of projects
# and typing up the list of projects manually into the configuration file becomes tedious.


# Bug: keys are not encased in single quote ''. that's lame.
# Bug: The comment after the last "project" key and before the "operation" key gets deleted by this script.
# - It also removes the new line space between them.
# Bad script! Bad! should fix. tired.

import os
import sys
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096   # prevent line wrapping


# --------------------------------------------
# DEFAULT INPUT / OUTPUT FILES
# --------------------------------------------
def_configs_in  = "greensync_config.yaml"
def_configs_out = "greensync_config-updated.yaml"

# --------------------------------------------
# HELP MESSAGE
# --------------------------------------------

if any(a in ["/?", "-h", "/h", "--help"] for a in sys.argv[1:]):
    print("")
    print("This script populates the list of projects inside greensync_config.yaml")
    print("Useful when a user have a large number of projects")
    print("and typing up the list of projects manually into the configuration file becomes tedious.")
    print("By default it will use the path defined by \"base_local\" inside greensync's config file, (1st user)")
    print("scanning that folder for subfolders. Each subfolder will define a project in the list of projects, exported to the output file.")
    print("The default output file will have an \"-updated\" suffix added to its file name,")
    print("so the original, input file won't get overwritten.")
    print("")
    print("Usage:")
    print("python make_projects_list_from_base_folder.py [-s input.yaml] [-o output.yaml] [-d directory]")
    print("")
    print("Options:")
    print(f"  -s <file>     Input GreenSync configuration file (.YAML)    | default: {def_configs_in}")
    print(f"  -o <file>     Output GreenSync configuration file (.YAML)   | default: {def_configs_out}")
    print( "  -d <dir>      Optional directory to scan instead of base_local inside the input file")
    print("")
    sys.exit(0)
else:
    print(f" use either argument:  /? , -h , /h , --help   for help\n")


# --------------------------------------------
# PARSE ARGUMENTS
# --------------------------------------------
args = sys.argv[1:]
i = 0

configs_in  = None
configs_out = None
scan_dir    = None


while i < len(args):
    if args[i] == "-s" and i + 1 < len(args):
        configs_in = args[i+1]
        i += 2
    elif args[i] == "-o" and i + 1 < len(args):
        configs_out = args[i+1]
        i += 2
    elif args[i] == "-d" and i + 1 < len(args):
        scan_dir = args[i+1]
        i += 2
    else:
        i += 1

print("")

# --------------------------------------------
# HANDLE DEFAULT INPUT FILE
# --------------------------------------------
if not configs_in:
    configs_in = def_configs_in
    print(f"No input file given as an argument. Using default file: {configs_in}")

if not os.path.isfile(configs_in):
    print(f"ERROR: Input file not found: {configs_in}")
    sys.exit(1)


# --------------------------------------------
# HANDLE DEFAULT OUTPUT FILE
# --------------------------------------------
if not configs_out:
    configs_out = def_configs_out
    print(f"No output file given as an argument. Using default file: {configs_out}")

if os.path.isfile(configs_out):
    print(f"\nWarning! Output file already exists. OVERWRITING the output file: {configs_out}\n")



# --------------------------------------------
# LOAD YAML WHILE PRESERVING FORMAT
# --------------------------------------------
with open(configs_in, "r", encoding="utf-8") as f:
    data = yaml.load(f)


# --------------------------------------------
# DETERMINE DIRECTORY TO SCAN
# --------------------------------------------
if scan_dir is None:
    scan_dir = data["users"][0]["base_local"]
    if not scan_dir:
        print("ERROR: No [-d directory] given and base_local directory is missing from the input YAML file.")
        sys.exit(1)
    print(f"No base directory supplied as an argument. Using base_local directory from the input file")

scan_dir = os.path.abspath(scan_dir)

if not os.path.isdir(scan_dir):
    print(f"ERROR: Directory does not exist: {scan_dir}")
    sys.exit(1)
else:
    print(f"Scanning the physical base directory for subfolders: {scan_dir}")


# --------------------------------------------
# SCAN SUBDIRECTORIES
# --------------------------------------------
subdirs = []
for entry in os.listdir(scan_dir):
    full = os.path.join(scan_dir, entry)
    if os.path.isdir(full):
        subdirs.append(entry)


# --------------------------------------------
# BUILD NEW PROJECTS LIST
# --------------------------------------------
new_projects = yaml.seq()  # preserves list formatting

for folder in subdirs:
    proj = yaml.map()
    proj["name"] = folder
    proj["local"] = f"\\{folder}"
    proj["remote"] = f"\\{folder}"

    new_projects.append(proj)

# Replace the projects list
data["projects"] = new_projects

# Add a blank line between each project in the YAML output
for idx in range(1, len(new_projects)):
    new_projects.yaml_set_comment_before_after_key(idx, before='\n')


# --------------------------------------------
# WRITE OUTPUT YAML (preserves formatting)
# --------------------------------------------
with open(configs_out, "w", encoding="utf-8") as f:
    yaml.indent(offset=1, sequence=3, mapping=3)
    yaml.dump(data, f)


print("")
print(f" New projects list created with {len(new_projects)} entries.")
print(f" Saved output to: {configs_out}")