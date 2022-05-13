# Kiuwan Local Analysis Action

This is a github action that runs the Kiuwan Local Analyzer (KLA) for your repository.

| Parameter Name | Kiuwan Input | Description | Required |
| -- | -- | -- | -- |
| USER | --user | Kiuwan username | ✓ |
| PASS | --pass | Kiuwan password | ✓
| SOURCE_PATH | --sourcePath | Directory with code to analyze | ✓ |
| SOFTWARE_NAME | --softwareName | Name of the target application | ✓ |
| DOMAIN_ID | --domain-id | Domain identifier to use when authenticating |
| LABEL | --label | Label for the analysis |
| CREATE | --create | Create software at kiuwan service if not exists |
| WAIT_FOR_RESULTS | --wait-for-results | Wait for kiuwan to return complete results once the local analysis has finished. |
| MODEL_NAME | --model-name | The model name to use when analyzing |
