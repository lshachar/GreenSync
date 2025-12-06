# GreenSync by Shachar Liberman
# https://github.com/lshachar/GreenSync
# Enjoying GreenSync? please show me your love -  https://paypal.me/lshachar  :)

# This is the main GreenSync script

import os
import sys
from ruamel.yaml import YAML

yaml = YAML()

# Default file paths
template_file = "greensync_template.xml"
config_file = "greensync_config.yaml"


output_path = '' # defaults to [base_local\local folder of the 1st project]. ie c:\GreenSync\ZZ GreenSync Operations\
                 # (it's also possible to run the script with -d <dir> argument to change the default save path)

def load_yaml(Path_File):
    if not os.path.isfile(Path_File):
        print(f"ERROR: .yaml file not found: {Path_File}")
        sys.exit(1)
    with open(Path_File, "r", encoding="utf-8") as f:
        return yaml.load(f)

def load_template(Path_File):
    if not os.path.isfile(Path_File):
        print(f"ERROR: Template file not found: {Path_File}")
        sys.exit(1)
    with open(Path_File, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_ffsgui(config, template, output_path):
    if output_path:
        basepath = output_path
    else:
        basepath = config["users"][0]["base_local"]  # if no output path is given, use the local projects folder of the 1st user

    # Prepare include/exclude list xml
    include_xml = "\n        ".join(f"<Item>{item}</Item>" for item in config["include"])
    exclude_xml = "\n        ".join(f"<Item>{item}</Item>" for item in config["exclude"])

    for user in config["users"]:
        print('Creating files for user:',user)
        uname = user["name"]
        ubase_local = user["base_local"]
        ubase_remote = user["base_remote"]

        for project in config["projects"]:
            pname = project["name"]
            plocal = project["local"]
            premote = project["remote"]
            if "op_savepath" in project:
                popsavepath = project["op_savepath"]
                if popsavepath.startswith('\\'):
                    popsavepath = popsavepath[1:]
            else:
                popsavepath = ''

            for op in config["operations"]:
                oname = op["name"]
                onotes = op["notes"]

                # Operation rules
                l = op["left"]
                r = op["right"]

                # Build file content
                xml = template
                xml = xml.replace("{{BASE_LOCAL}}", ubase_local)
                xml = xml.replace("{{BASE_REMOTE}}", ubase_remote)
                xml = xml.replace("{{PROJECT_LOCAL}}", plocal)
                xml = xml.replace("{{PROJECT_REMOTE}}", premote)
                xml = xml.replace("{{NOTES}}", onotes)
                xml = xml.replace("{{INCLUDE_LIST}}", include_xml)
                xml = xml.replace("{{EXCLUDE_LIST}}", exclude_xml)


                # Replace left/right rule placeholders
                xml = xml.replace("{{LEFT_CREATE}}",  l["Create"])
                xml = xml.replace("{{LEFT_UPDATE}}",  l["Update"])
                xml = xml.replace("{{LEFT_DELETE}}",  l["Delete"])

                xml = xml.replace("{{RIGHT_CREATE}}", r["Create"])
                xml = xml.replace("{{RIGHT_UPDATE}}", r["Update"])
                xml = xml.replace("{{RIGHT_DELETE}}", r["Delete"])

                # Output filename
                filename = f"{pname} - {oname}.ffs_gui"
                outpath = os.path.join(basepath,(config["projects"][0]["local"][1:]),uname, popsavepath, filename)
                
                print(f"Creating: {outpath}")
                write_file(outpath, xml)
                

if __name__ == "__main__":

    if any(arg in ["/?", "-h", "/h", "--help"] for arg in sys.argv[1:]):
        print("\nUsage:")
        print("  python make_sync_operations.py [-t greensync_template.xml] [-c greensync_config.yaml] [-d output_path]")
        print("")
        print("Options:")
        print("  -c <file>  Use a different (C)onfiguration file (.YAML)  | default: greensync_config.yaml")
        print("  -t <file>  Use a different (T)emplate file (.XML)        | default: greensync_template.xml")
        print("  -d <dir>   Use a different output (D)irectory            | default: the 1st project local directory in the projects definitions list")
        print("                                                        | ie c:\\GreenSync\\ZZ GreenSync Operations\\")
        print("")
        print("Example:")
        print("python create_sync_operations.py -t template-other.xml -c config-project2.yaml -d c:\\tempfolder\\ ")
    else:
        print(f" use either argument:  /? , -h , /h , --help   for help\n")

        args = sys.argv[1:]
        i = 0
        while i < len(args):
            if args[i] == "-t" and i + 1 < len(args):
                template_file = args[i + 1]
                i += 2
            elif args[i] == "-c" and i + 1 < len(args):
                config_file = args[i + 1]
                i += 2
            elif args[i] == "-d" and i + 1 < len(args):
                output_path = args[i + 1]
                i += 2
            else:
                i += 1        


        config = load_yaml(config_file)
        template = load_template(template_file)
        generate_ffsgui(config, template, output_path)
