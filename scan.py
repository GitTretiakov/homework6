import sys
from pathlib import Path

JPEG_files = list()
PNG_files = list()
JPG_files = list()
SVG_files = list()

AVI_files = list()
MP4_files = list()
MOV_files = list()
MKV_files = list()

DOC_files = list()
DOCX_files = list()
TXT_files = list()
PDF_files = list()
XLSX_files = list()
PPTX_files = list()

MP3_files = list()
OGG_files = list()
WAV_files = list()
AMR_files = list()

ARCHIVE_files = list()
GZ_files = list()
TAR_files = list()

OTHER_files = list()
UNKNOWN_files = set()
extensions = set()
folders = list()

registered_extensions = {

    "JPEG": JPEG_files,
    "PNG": PNG_files,
    "JPG": JPG_files,
    "SVG": SVG_files,

    "AVI": AVI_files,
    "MP4": MP4_files,
    "MOV": MOV_files,
    "MKV": MKV_files,

    "DOC": DOC_files,
    "DOCX": DOCX_files,
    "TXT": TXT_files,
    "PDF": PDF_files,
    "XLSX": XLSX_files,
    "PPTX": PPTX_files,

    "MP3": MP3_files,
    "OGG": OGG_files,
    "WAV": WAV_files,
    "AMR": AMR_files,

    "ZIP": ARCHIVE_files,
    "GZ": ARCHIVE_files,
    "TAR": ARCHIVE_files
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("archives", "video", "audio", "documents", "images", "others"):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name

        if not extension:
            OTHER_files.append(new_name)

        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)

            except KeyError:
                UNKNOWN_files.add(extension)
                OTHER_files.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")


    folder = Path(path)

    scan(folder)

    print(f"JPEG: {JPEG_files}")
    print(f"PNG: {PNG_files}")
    print(f"JPG: {JPG_files}")
    print(f"SVG: {SVG_files}")

    print(f"AVI: {AVI_files}")
    print(f"MP4: {MP4_files}")
    print(f"MOV: {MOV_files}")
    print(f"MKV: {MKV_files}")

    print(f"DOC: {DOC_files}")
    print(f"DOCX: {DOCX_files}")
    print(f"TXT: {TXT_files}")
    print(f"PDF: {PDF_files}")
    print(f"XLSX: {XLSX_files}")
    print(f"PPTX: {PPTX_files}")

    print(f"MP3: {MP3_files}")
    print(f"OGG: {OGG_files}")
    print(f"WAV: {WAV_files}")
    print(f"AMR: {AMR_files}")

    print(f"ZIP: {ARCHIVE_files}")
    print(f"GZ: {ARCHIVE_files}")
    print(f"TAR: {ARCHIVE_files}")

    print(f"OTHER: {OTHER_files}")
    print(f"UNKNOWN: {UNKNOWN_files}")
    print(f"EXTENSIONS: {extensions}")
    print(f"FOLDERS: {folders}")





