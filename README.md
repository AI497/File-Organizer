# File Organizer

A simple Python program that scans a folder, detects files based on their extensions, and automatically sorts them into separate folders.

## Features

* Detects document files
* Detects image files
* Detects video files
* Automatically moves files into their corresponding folders
* Identifies unknown file types
* Simple `y/n` prompt to start organizing
* Uses standard Python libraries

## Technologies Used

* Python
* `os`
* `shutil`
* `pathlib`
* `time`

## Folder Setup

The files you want to organize **must be placed in the same folder as the Python script**.

The program sorts files into three different folders:

* `Document_Type`
* `Image_Type`
* `Video_Type`

The folder structure should look like this:

```text
File Organizer/
│
├── file_organizer_main_code.py
│
├── Document_Type/
├── Image_Type/
├── Video_Type/
│
├── homework.pdf
├── notes.txt
├── picture.png
├── vacation.jpg
├── video.mp4
└── movie.mov
```

### Document Files

The following file types are recognized as documents:

* `.txt`
* `.pdf`
* `.docx`

These files will be moved into:

```text
Document_Type/
```

### Image Files

The following file types are recognized as images:

* `.png`
* `.jpg`
* `.jpeg`

These files will be moved into:

```text
Image_Type/
```

### Video Files

The following file types are recognized as videos:

* `.mp4`
* `.mov`

These files will be moved into:

```text
Video_Type/
```

## Important

All files that you want the program to organize must be located in the **same folder as the Python script**.

The three destination folders must also be in that folder.

The program will automatically create the destination folders if they do not already exist.

## How to Run

1. Download or clone this repository.
2. Place the files you want to organize into the same folder as the Python script.
3. Run the Python script.
4. The program will scan the folder and identify the files.
5. When prompted, enter `y` to organize the files or `n` to leave them unchanged.

Example:

```text
Would you like to sort the files by their type? (y/n): y

Organizing Files. . .
Files Have Been Organized!
```

## How It Works

The program first gets a list of files in the current directory:

```python
files = os.listdir()
```

It then uses `os.path.splitext()` to separate the filename from its extension:

```python
y = os.path.splitext(x)
```

The program compares the extension against predefined lists:

```python
documents = [".txt", ".pdf", ".docx"]
images = [".png", ".jpg", ".jpeg"]
videos = [".mp4", ".mov"]
```

If the file matches one of these categories, `shutil.move()` moves it into the appropriate folder.

For example:

```python
if y[1] in documents:
    shutil.move(x, "Document_Type")
```

Files with unsupported extensions are left untouched.

## Supported File Types

| Category  | File Types              |
| --------- | ----------------------- |
| Documents | `.txt`, `.pdf`, `.docx` |
| Images    | `.png`, `.jpg`, `.jpeg` |
| Videos    | `.mp4`, `.mov`          |

## Unknown File Types

If a file does not match any of the supported extensions, the program identifies it as an unknown file type and leaves it where it is.

## Future Improvements

Possible improvements for future versions include:

* Add support for more file types
* Add additional categories such as audio and programs
* Allow the user to choose which folder to organize
* Add a graphical user interface
* Allow users to create custom file categories
* Add duplicate-file handling
* Organize files automatically without requiring user input

## Author

Created as a Python programming project to practice file handling, loops, functions, conditional statements, and working with the operating system.
