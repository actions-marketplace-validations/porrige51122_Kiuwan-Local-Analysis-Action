from pathlib import Path
import urllib
import zipfile
import requests
import io
import os
import subprocess
import sys
import re

INPUT_PARAMS = [
    ["USER", "--user"],
    ["PASS", "--pass"],
    ["SOURCE_PATH", "--sourcePath"],
    ["DOMAIN_ID", "--domain-id"],
    ["SOFTWARE_NAME", "--softwareName"],
    ["LABEL", "--label"],
    ["CREATE", "--create"],
    ["WAIT_FOR_RESULTS", "--wait-for-results"],
    ["MODEL_NAME", "--model-name"],
]


def main():
    print_custom_title()
    kla_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    output_dir = "./tmp"
    agent = f"{output_dir}/KiuwanLocalAnalyzer/bin/agent.sh"
    download_and_extract_file(kla_url, output_dir)
    os.chmod(agent, 0x777)
    cmd_params = build_kla_parameters()
    return_code = execute_command(f"{agent} {cmd_params}")
    print(f"::set-output name=result::{return_code}")


def execute_command(cmd):
    print(f"Executing: {cmd}")
    output = os.system(cmd)
    return os.waitstatus_to_exitcode(output)


def build_kla_parameters():
    print("Building parameters...")
    cmd_parameters = ""
    filter = "[^a-zA-Z0-9_!@#%*-]"
    for param in INPUT_PARAMS:
        try:
            env = re.sub(filter, "", os.environ[f"INPUT_{param[0]}"])
            if env != "":
                cmd_parameters += f"{param[1]} {env}"
        except KeyError:
            pass
    return cmd_parameters


def print_custom_title():
    print(
        "\u001b[33m\n"
        + bytes.fromhex(
            "205F2020205F5F205F202020202020205F5F5F2020202020205F5F5F202020202020205F2020205F0A7C207C202F202F7C207C20202020202F205F205C202020202F205F205C20202020207C207C20285F290A7C207C2F202F207C207C202020202F202F5F5C205C20202F202F5F5C205C205F5F5F7C207C5F205F20205F5F5F20205F205F5F0A7C202020205C207C207C202020207C20205F20207C20207C20205F20207C2F205F5F7C205F5F7C207C2F205F205C7C20275F205C0A7C207C5C20205C7C207C5F5F5F5F7C207C207C207C20207C207C207C207C20285F5F7C207C5F7C207C20285F29207C207C207C207C0A5C5F7C205C5F2F5C5F5F5F5F5F2F5C5F7C207C5F2F20205C5F7C207C5F2F5C5F5F5F7C5C5F5F7C5F7C5C5F5F5F2F7C5F7C207C5F7C0A42792040706F72726967653531313232"
        ).decode("ASCII")
        + "\u001b[0m\n"
    )


def download_file_from_url(url):
    print("Downloading KLA...")
    return urllib.request.urlopen(url)


def extract_zip_file(file, output_dir):
    print("Extracting agent from zip...")
    zip_file = zipfile.ZipFile(io.BytesIO(file.read()))
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    zip_file.extractall(output_dir)


def download_and_extract_file(url, output_dir):
    file = download_file_from_url(url)
    extract_zip_file(file, output_dir)


if __name__ == "__main__":
    main()
