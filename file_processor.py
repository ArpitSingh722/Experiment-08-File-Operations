"""
Experiment No. 8 (CO-3)
Create a Python script to read data from an input file. Perform count lines,
extract the first two lines, and write the extracted data into a new file.
"""

import os


def process_file(input_filepath: str, output_filepath: str) -> tuple[int, list[str]]:
    """Reads input_filepath, counts total lines, extracts the first two lines, and writes them to output_filepath."""
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file not found: '{input_filepath}'")

    with open(input_filepath, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    total_lines = len(lines)
    first_two_lines = lines[:2]

    with open(output_filepath, "w", encoding="utf-8") as outfile:
        outfile.writelines(first_two_lines)

    return total_lines, first_two_lines


def main() -> None:
    input_file = "input.txt"
    output_file = "extracted_output.txt"

    try:
        line_count, extracted_lines = process_file(input_file, output_file)

        print(f"Total number of lines in '{input_file}': {line_count}")
        print("-" * 45)
        print("First two extracted lines:")
        if extracted_lines:
            for idx, line in enumerate(extracted_lines, start=1):
                print(f"Line {idx}: {line.rstrip()}")
        else:
            print("(Input file is empty)")
        print("-" * 45)
        print(f"Extracted data written to '{output_file}'.")

    except FileNotFoundError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
