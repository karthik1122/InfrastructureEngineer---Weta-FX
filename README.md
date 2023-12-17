# Image File Renaming Script

This script helps rename image files in a directory following a specific pattern.

## Description

The script renames image files within a directory according to the pattern:
- All files are renamed as 'awesome01.ext', 'awesome02.ext', and so on, where 'awesome' is the common name, followed by a sequential number.
- File extensions (.jpg, .png, etc.) are retained to differentiate between file types.

## How to Use

1. **Directory Setup**: Place the script in the directory containing the image files you want to rename.
2. **Run the Script**: Execute the script. It will identify image files and rename them according to the specified pattern.
3. **Adjustment**: Modify the 'directory_path' variable inside the script to point to your directory containing image files.

## Example

Suppose you have images named 'example_01.jpg', 'example_02.png', etc., in the directory. Running the script will rename them as 'awesome01.jpg', 'awesome02.png', etc.

## Script Modification

- To change the common name or the numbering pattern, modify the script's variables within the 'renumber_sequences' function.
- Ensure Python 3.x is installed to run the script.

## Author

[Karthick Visvesh]

Feel free to modify the script according to your requirements!

