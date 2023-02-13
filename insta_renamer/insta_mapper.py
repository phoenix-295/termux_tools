import os

downloadsFolder = "C:\\Users\\Nikhil\\Downloads"


def find_webp_files(path):
    zip_files = []
    files = os.listdir(path)
    for file in files:
        if file.endswith(".webp"):
            zip_files.append(file)
    return zip_files

def rename_webp(path):
    for each in path:
        base, ext = os.path.splitext(each)
        new_file = base + ".jpeg"
        # print(f"{downloadsFolder}\{each}")
        # print(f"{downloadsFolder}\{new_file}")
        os.rename(f"{downloadsFolder}\{each}", f"{downloadsFolder}\{new_file}")
        print(new_file)

def main():
    doc_files = find_webp_files(downloadsFolder)
    print(doc_files)
    rename_webp(doc_files)

if __name__ == "__main__":
    main()