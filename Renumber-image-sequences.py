import os

def renumber_sequences(directory):
    # List of filenames in the directory
    filenames = os.listdir(directory)

    # Dictionary to hold sequences for each extension
    sequences = {}

    # Group files into sequences for each extension
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        if ext.lower() not in sequences:
            sequences[ext.lower()] = []

        sequences[ext.lower()].append(filename)

    # Renaming files in sequences for each extension
    for ext, files in sequences.items():
        files.sort()  # Sort files to maintain order
        digits = len(str(len(files)))  # Get the number of digits required for padding

        # Renaming files in the sequence with 'awesome' followed by a sequential number
        for i, old_name in enumerate(files):
            new_name = f"awesome{str(i + 1).zfill(2)}{ext}"
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)

            # Renaming the files using os.rename()
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")

# Directory path containing the files
directory_path = "/mnt/c/Users/Karthick.Visvesh/iPayroll/code/tests-and-examples/InfrastructureEngineer/photos"

# Call the function with the specified directory path
renumber_sequences(directory_path)
print("Sequence renumbering complete!")
