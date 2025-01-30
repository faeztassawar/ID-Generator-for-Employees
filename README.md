# Random ID Generator for CSV Files

This Python script automates the process of generating unique IDs for employee records stored in a CSV file. It reads the employee data, generates IDs based on their hired positions, and writes the updated data with IDs to a new CSV file. Additionally, the script offers an option to display the generated IDs on the terminal.

## Table of Contents

- [How It Works](#how-it-works)
- [Usage](#usage)
- [Command-Line Argument Validation](#command-line-argument-validation)
- [Error Handling](#error-handling)
- [Customization](#customization)
- [Note](#note)
- [Contributing](#contributing)

## How It Works

1. The script reads the input CSV file containing employee data, including columns such as "name," "hired_position," and "decided_salary."

2. It generates unique IDs by combining the initials of each hired position with a random three-digit number. The script ensures ID uniqueness by checking against a list of previously generated IDs.

3. The updated data with generated IDs is written to the specified output CSV file.

4. The script prompts the user whether to display the generated IDs on the terminal. This can help verify the uniqueness and structure of the generated IDs.

## Usage

1. Ensure you have Python installed on your system.

2. Open a terminal or command prompt.

3. Run the script using the following command format:

   ```bash
   python script.py input.csv output.csv
   ```

   Replace `script.py` with the actual script filename, `input.csv` with the name of the input CSV file containing employee data, and `output.csv` with the desired name of the output CSV file.

4. The script will process the input file, generate IDs, and create the output file.

5. After completion, you will be prompted to decide whether to display the generated IDs on the terminal.

## Command-Line Argument Validation

The script includes robust validation for command-line arguments:

- It checks that the correct number of arguments is provided.
- It verifies that both the input and output filenames have the ".csv" extension.

## Error Handling

- If the input CSV file is not found, the script will exit with an appropriate error message.
- If incorrect command-line arguments are provided, the script will exit with informative error messages.

## Customization

- The script's ID generation logic is based on the initials of hired positions and random numbers. Depending on your needs, you can modify the `generate_initials` and `generate_id` functions to adapt the ID generation strategy.

## Note

- While the script generates IDs unlikely to collide, the randomness is not cryptographically secure. It's advised not to use this script for applications requiring highly secure IDs.

- Remember to keep backups of your original data before using this script, especially when writing data to an output file, as it will overwrite any existing content.

## Contributing

Contributions are welcome! If you find any issues, have suggestions for improvements, or want to add new features, please feel free to create issues or pull requests in this repository.