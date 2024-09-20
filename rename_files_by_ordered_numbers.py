import os
import argparse

# Function to rename files in the directory
def rename_files(directory):
    # List all files in the directory
    files = sorted(os.listdir(directory))
    
    # Count the number of files to determine the number of digits needed for zero-padding
    num_digits = len(str(len(files)))

    # Iterate through the files and rename them
    for count, filename in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Construct the new filename with leading zeros
        new_filename = f"{str(count).zfill(num_digits)}{file_extension}"

        # Get the full path for the current and new filename
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')

# Main function to handle the argument
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rename files in a directory to be ordered by numbers.")
    parser.add_argument('directory', type=str, help="The path to the directory containing the files.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the rename_files function with the directory
    rename_files(args.directory)

if __name__ == "__main__":
    main()