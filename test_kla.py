import pytest  # For testing
import shutil  # For removing folders added from testing
import os  # For parameter checking
from kla import (
    execute_command,
    build_kla_parameters,
    download_file_from_url,
    extract_zip_file,
    download_and_extract_file,
)

INPUT_PARAMS = [
    "INPUT_USER",
    "INPUT_PASS",
    "INPUT_SOURCE_PATH",
    "INPUT_DOMAIN_ID",
    "INPUT_SOFTWARE_NAME",
    "INPUT_LABEL",
    "INPUT_CREATE",
    "INPUT_WAIT_FOR_RESULTS",
    "INPUT_MODEL_NAME",
    "INPUT_BRANCH_NAME",
]


def test_download_file_from_url():
    test_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    file = download_file_from_url(test_url)
    assert file != None


def test_extract_zip_file():
    test_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    test_output_dir = "./test"
    output_file = download_file_from_url(test_url)
    extract_zip_file(output_file, test_output_dir)


def test_extract_zip_file_with_existing_folder():
    test_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    test_output_dir = "./test"
    output_file = download_file_from_url(test_url)
    extract_zip_file(output_file, test_output_dir)
    shutil.rmtree(test_output_dir)


def test_download_and_extract_file():
    test_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    test_output_dir = "./test"
    download_and_extract_file(test_url, test_output_dir)
    shutil.rmtree(test_output_dir)


def test_kla_parameters_creates_correct_output():
    for var in INPUT_PARAMS:
        set_env_var(var, "")
    assert build_kla_parameters() == ""
    for var in INPUT_PARAMS:
        assert build_kla_parameters() == ""
        assert check_var_works(var)


def test_execute_command():
    assert execute_command("echo 'Hello World!'") == 0


def test_execute_command_kla():
    test_url = "https://www.kiuwan.com/pub/analyzer/KiuwanLocalAnalyzer.zip"
    test_output_dir = "./test"
    download_and_extract_file(test_url, test_output_dir)
    agent = f"{test_output_dir}/KiuwanLocalAnalyzer/bin/agent.sh"
    os.chmod(agent, 0x777)
    # 21 is parameter error, this is because no parameters are passed
    assert 21 == execute_command(agent)
    # Although access denied is 22 and user credentials are wrong, due to access
    # denied, the engine is not created therefore 31 (No engine avaliable) is
    # the error
    assert 31 == execute_command(
        f"{agent} --user TEST --pass TEST --sourcePath . --softwareName TEST"
    )
    shutil.rmtree(test_output_dir)


def check_var_works(name):
    set_env_var(name, name)
    out = build_kla_parameters()
    set_env_var(name, "")
    return out[-len(name) :] == name


def set_env_var(name, value):
    os.environ[name] = value
