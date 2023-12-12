# download_folder_cleaner
A python script to organize your download folder in themed folders (e.g. : pdfs, scripts, documents, images, etc...)

To use :
```bash
python cleaner.py
```

To bundle the script into an unix executable : 

```bash
pip install pyinstaller
```

```bash
pyinstaller cleaner.py
```

To bundle the script into a macos app : 

```bash
pyinstaller -w -i recycle.png cleaner.py
```