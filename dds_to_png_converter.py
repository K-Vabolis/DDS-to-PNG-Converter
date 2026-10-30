import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Error: The 'Pillow' library is required to process images.")
    print("Please install it using: pip install Pillow")
    sys.exit(1)


def convert_dds_to_png(directory="."):
    """
    Searches the specified directory for .dds files and converts them to .png.
    """
    files = [f for f in os.listdir(directory) if f.lower().endswith(".dds")]

    if not files:
        print("No .dds files found in the directory.")
        return

    print(f"Found {len(files)} .dds file(s). Starting conversion...\n")

    converted_count = 0
    for filename in files:
        dds_path = os.path.join(directory, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(directory, png_filename)

        try:
            with Image.open(dds_path) as img:
                # Save as PNG format preserving transparency
                img.save(png_path, "PNG")
                print(f"[✓] Converted: {filename} -> {png_filename}")
                converted_count += 1
        except Exception as e:
            print(f"[X] Failed to convert {filename}: {e}")

    print(f"\nDone! Successfully converted {converted_count}/{len(files)} files.")


if __name__ == "__main__":
    # Get current working directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    convert_dds_to_png(current_dir)