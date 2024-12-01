@echo off
python -m pyinstaller --onefile --add-data "Tool/Offsets/offsets.json;Tool/Offsets" Burware.py
python Burware.py
pause