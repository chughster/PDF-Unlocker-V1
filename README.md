
# PDF Password Remover

A simple Python tool that unlocks password-protected PDF files using a graphical interface. If the PDF is encrypted, it prompts for a password and creates an unlocked copy.

## Features

- Select a PDF file via a file dialog.
- Automatically unlocks PDFs without a password prompt if not encrypted.
- Prompts for a password if needed.
- Saves the unlocked PDF in the same directory with "_unlocked" appended to the filename.

## Requirements

- Python 3.x
- [pikepdf](https://pikepdf.readthedocs.io/)  
- Tkinter (usually included with Python)

## Installation

1. Clone the repository or download the script.
2. Install the required package:
   ```bash
   pip install pikepdf
   ```

## Usage

Run the script:
```bash
python your_script_name.py
```
A file selection dialog will appear for you to choose the PDF file. Follow the on-screen prompts if a password is required.

## Troubleshooting

- **No file selected:** The script will exit if no file is chosen.
- **Incorrect password:** An error message will display if the entered password is incorrect.
- **Other errors:** General exceptions are caught and reported.

## License

This project is open-source. Feel free to use or modify it as needed.
```
