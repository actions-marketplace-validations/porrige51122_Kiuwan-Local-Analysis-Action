# Kiuwan Local Analysis Action

This is a GitHub action that runs the Kiuwan Local Analyzer (KLA) on your repository.

This is not created by Kiuwan (as of this release) as they do not provide a GitHub action which does this function.
Therefore please check the source code and use this action sensibly to prevent any security risks.

## Parameters

| Parameter Name | Kiuwan Input | Description | Required |
| -- | -- | -- | -- |
| user | --user | Kiuwan username | ✓ |
| pass | --pass | Kiuwan password | ✓ |
| software_name | --softwareName | Name of the target application | ✓ |
| source_path | --sourcePath | Directory with code to analyze (default ".") |   |
| domain_id | --domain-id | Domain identifier to use when authenticating |
| label | --label | Label for the analysis |
| create | --create | Create software at kiuwan service if not exists |
| model_name | --model-name | The model name to use when analyzing |
| wait_for_results | --wait-for-results | Wait for kiuwan to return complete results once the local analysis has finished. |

## Example Usage

```YAML
steps:
      - name: Checkout the repository
        uses: actions/checkout@v3
      - name: Kiuwan Local Analysis
        uses: porrige51122/Kiuwan-Local-Analysis-Action@v1.3
        with:
          # (REQUIRED) Username for Kiuwan
          # Recommended to use GitHub secrets to prevent account leaks
          user: ${{ secrets.KIUWAN_USER }}

          # (REQUIRED) Password for Kiuwan
          # Recommended to use GitHub secrets to prevent account leaks
          pass: ${{ secrets.KIUWAN_PASS }}

          # (REQUIRED) Name of the target Application on Kiuwan
          software_name: ${{ github.repository }}

          # (OPTIONAL) Directory to analyze
          source_path: ${{ github.workspace }}

          # (OPTIONAL) Domain identifier to use when authenticating (Required for SSO)
          # Recommended to use GitHub secrets to prevent leaks
          domain-id: ${{ secrets.KIUWAN_SSO_DOMAIN }}

          # (OPTIONAL) Label to distinguish analysis' on Kiuwan site
          label: ${{ github.head_ref }} # Branch name

          # (OPTIONAL) Create Application if it doesn't exist already (true/false)
          create: "False"

          # (OPTIONAL) The Model to use when analyzing
          model: "CQM"

          # (OPTIONAL) Wait for analysis to complete before finishing the action
          # If errors occur, this can take up to 45 minutes to finish
          wait_for_results: "False"
```

## Notes

To prevent parameter injection, all inputs have been sanitized to the regex:
```
[^a-zA-Z0-9_!@#%*-]
# All letters a-z, A-z. All numbers 0-9. _ and - characters.
```
This prevents Special Characters:
```
&
;
Newline (0x0a or \n)
&&
|
||
command `
$(command )
```

This protection includes passwords, therefore if errors occur, please make sure your password is within this regex.

## Acknowledgments

Project inspired, and modified from: lsacera/KiuwanBaselineAction
It has been updated in the aim of making it secure, faster, and more modifiable for the
future
