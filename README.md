# URL QR Code Generator

A small command-line program that asks for a web address and creates a QR code image.

## Requirements

- Python 3.9 or newer
- Internet access during the initial dependency installation

## Installation

Clone or download this repository, then open a terminal in its folder.

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python URLqr.py
```

If PowerShell prevents virtual-environment activation, you can run it directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe URLqr.py
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python URLqr.py
```

## Usage

Enter a complete URL or a domain name:

```text
Enter the URL: example.com
QR code generated for: https://example.com
Saved at: /path/to/URLQR/qrcode_YYYYMMDD_HHMMSS_microseconds.png
```

The generated PNG is saved in the project folder. Generated images and local virtual environments are excluded from Git by `.gitignore`.
# URL_to_QR
