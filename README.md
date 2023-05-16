# CSV to Espanso YAML Config Converter

This Python script converts a CSV file to a YAML configuration file that can be used with [Espanso](https://espanso.org/), a cross-platform text expander.

## Purpose

Espanso works by detecting when you type a specific keyword and replaces it with something else. This tool helps you generate Espanso configuration files from a CSV source, making it easy to manage and update your text expansions.

## How to Use

### Prerequisites

- Python 3.7 or higher
- PyYAML module installed (use `pip install pyyaml` to install)

### Steps

1. Prepare a CSV file with two columns: `act` and `prompt`. `act` will be converted to the trigger keyword, and `prompt` will be the replacement text.

    Example:

    ```
    "act","prompt"
    "Linux Terminal","I want you to act as a Linux terminal."
    ```

2. Run the Python script and provide the input CSV file and the desired output YAML file as command-line arguments:

    ```bash
    python3 convert_csv_to_yml_for_espanso.py input.csv output.yml
    ```

    Replace `input.csv` and `output.yml` with your actual filenames.

3. The script will create a YAML file with the following structure:

    ```yaml
    matches:
    - trigger: ":lt"
      replace: "I want you to act as a Linux terminal."
    ```

    This YAML file can be used as a configuration file for Espanso.
    This Python script also processes the `act` field of the CSV file to create the           trigger keyword for Espanso. It follows these rules:

    If the act field contains multiple words, the script takes the first letter of each word to form the keyword. For example, "Linux Terminal" becomes "lt".
    If the act field contains a single word, the script uses the whole word in lowercase as the keyword. For example, "Friend" becomes "friend".
    This feature allows you to use more descriptive phrases in your CSV file while keeping your Espanso triggers short and easy to type.

### Run Script

If you are on a Unix-based system like Linux, you can use the included `run.sh` script to run the Python script. First, make the script executable:
```
chmod +x run.sh
```
Then you can run it:
```bash
run.sh
```
The run.sh script is preset to run the Python script with prompts.csv as the input file and gpt.yml as the output file. You can edit run.sh in a text editor to use different filenames.