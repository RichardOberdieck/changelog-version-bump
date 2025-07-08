import os
import re
import glob
import tomllib
from pathlib import Path

breakpoint()

def read_options():
    tomlpath = Path("pyproject.toml")
    toml_text = tomlpath.read_text(encoding="utf-8")
    data = tomllib.loads(toml_text)
    try:
        options = data["tool"]["changelog-version-bump"]
    except KeyError:
        # No settings for us
        return

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
    main()
    clean()
    os.remove("temp.md")
    