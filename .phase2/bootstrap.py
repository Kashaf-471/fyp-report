"""Install only workspace-local compiler/optional verification dependencies."""
from pathlib import Path
import argparse
import io
import subprocess
import sys
import urllib.request
import zipfile

HERE = Path(__file__).resolve().parent
COMPILER = HERE / "tools/tectonic/tectonic.exe"
URL = "https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.17.0/tectonic-0.17.0-x86_64-pc-windows-msvc.zip"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", action="store_true")
    args = parser.parse_args()
    if not COMPILER.exists():
        if sys.platform != "win32":
            raise SystemExit("This bootstrap installs the Windows compiler; use a system TeX toolchain on other platforms.")
        print("Downloading official Tectonic 0.17.0 into ignored .phase2/tools/...")
        with urllib.request.urlopen(URL, timeout=120) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
        COMPILER.parent.mkdir(parents=True, exist_ok=True)
        COMPILER.write_bytes(archive.read("tectonic.exe"))
    if args.pdf:
        target = HERE / "tools/python"
        sys.path.insert(0, str(target))
        try:
            import pymupdf
            import PIL
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "--target", str(target),
                            "pymupdf==1.28.2", "Pillow"], check=True)
    print("Workspace build tools ready.")

if __name__ == "__main__":
    main()
