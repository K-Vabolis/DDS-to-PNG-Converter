DDS to PNG Batch Converter
A small Python script that converts .dds image files in the script’s folder to .png files using Pillow. PNG output preserves transparency when it is present in the source image.
Requirements
- Python 3
- Pillow
Install Pillow with:
pip install Pillow
Usage
Place dds_to_png_converter.py in the folder containing the .dds files, then run:
python dds_to_png_converter.py
The script processes .dds files in that folder and saves each .png beside its source file. It reports successful conversions and any files it could not convert.
Notes
- File extensions are matched case-insensitively, so .DDS files are included.
- Existing PNG files with the same names may be overwritten.
- The script processes only files directly in the folder; it does not search subfolders.
- DDS format support can depend on the Pillow version and available codecs.
