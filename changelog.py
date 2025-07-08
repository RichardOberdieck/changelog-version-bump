import os
import re
import glob
import sys

def main():
    "Must run after scriv print, to get the correct changes."

    with open("temp.md") as file:
        lines = file.readlines()


    for line in lines:
        if line.startswith("## Major:"):
            print("major")
            return

    for line in lines:
        if line.startswith("## Minor:"):
            print("minor")
            return


    for line in lines:
        if line.startswith("## Patch:"):
            print("patch")
            return


def clean():
    "Clean out the bump size indicators in changelog.d fragments"

    for file_path in glob.iglob('changelog.d/*'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        updated_content = re.sub(r'### (Major|Minor|Patch):', '###', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean()
        os.remove("temp.md")
        exit(0)
    else:
        main()

    
    