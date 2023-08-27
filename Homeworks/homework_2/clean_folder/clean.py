import shutil
from pathlib import Path
import re
import sys

image_extensions = ('.jpeg', '.png', '.jpg', '.svg')
document_extensions = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
audio_extensions = ('.mp3', '.ogg', '.wav', '.amr')
video_extensions = ('.avi', '.mp4', '.mov', '.mkv')
archive_extensions = ('.zip', '.gz', '.tar')
sort_folders = ('archives', 'video', 'audio', 'documents', 'images', 'unknown type')

TRANSLIT = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd',
            1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z',
            1080: 'i', 1048: 'I', 1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm',
            1052: 'M', 1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R',
            1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h',
            1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch',
            1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 1101: 'e', 1069: 'E',
            1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 1028: 'JE', 1110: 'i', 1030: 'I',
            1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'}


# the function that transliterates file names
def normalize(path):
    path = Path(path)
    for file_folder in path.iterdir():
        if file_folder.name == 'unknown type':
            continue
        if file_folder.is_dir():
            new_name = file_folder.name
            new_name = new_name.translate(TRANSLIT)
            new_name = re.sub(r'\W', '_', new_name)
            new_path = file_folder.parent / new_name
            file_folder.rename(new_path)
            normalize(new_path)
        elif file_folder.is_file():
            new_name = file_folder.name.replace(file_folder.suffix, '')
            new_name = new_name.translate(TRANSLIT)
            new_name = re.sub(r'\W', '_', new_name)
            new_name += file_folder.suffix
            new_path = file_folder.parent / new_name
            file_folder.rename(new_path)


# function that cleans folders
def clean_folders(path):
    path = Path(path)
    for folder in path.iterdir():
        if folder.name not in sort_folders:
            if folder.is_dir():
                clean_folders(folder)
                if not any(folder.iterdir()):
                    folder.rmdir()


# creates folders for further sorting
def create_folders(path, folder_list=sort_folders):
    for folder in folder_list:
        folder_path = Path(path) / folder
        folder_path.mkdir(exist_ok=True)


# unpacks archives into folders
def unpack_archives(file_name, path):
    path_to_unpack = f'{path}/archives/'
    folder_path = Path(path_to_unpack) / Path(file_name).name.replace(Path(file_name).suffix, '')
    folder_path.mkdir(exist_ok=True)

    if file_name.suffix == '.zip':
        shutil.unpack_archive(file_name, folder_path, format='zip')
    elif file_name.suffix == '.tar':
        shutil.unpack_archive(file_name, folder_path, format='tar')
    elif file_name.suffix == '.gz':
        shutil.unpack_archive(file_name, folder_path, format='gz')


# puts files into specific folders
def sort_files(file_name):
    if file_name.suffix in document_extensions:
        target_folder = f'{the_path}/documents/'

        try:
            shutil.move(str(file_name), target_folder)
        except PermissionError:
            print(f'Error while moving the file. Check the \'{file_name.name}\' file.')

    elif file_name.suffix in image_extensions:  # if the file has image format
        target_folder = f'{the_path}/images/'

        try:
            shutil.move(str(file_name), target_folder)
        except PermissionError:
            print(f'Error while moving the file. Check the \'{file_name.name}\' file.')

    elif file_name.suffix in video_extensions:  # if the file has video format
        target_folder = f'{the_path}/video/'

        try:
            shutil.move(str(file_name), target_folder)
        except PermissionError:
            print(f'Error while moving the file. Check the \'{file_name.name}\' file.')

    elif file_name.suffix in audio_extensions:  # if the file has ausio format
        target_folder = f'{the_path}/audio/'

        try:
            shutil.move(str(file_name), target_folder)
        except PermissionError:
            print(f'Error while moving the file. Check the \'{file_name.name}\' file.')

    elif file_name.suffix in archive_extensions:
        unpack_archives(file_name, the_path)
    else:
        target_folder = f'{the_path}/unknown type/'
        shutil.move(str(file_name), target_folder)


def parse(path):
    p = Path(path)

    for items in p.iterdir():
        if items.name in sort_folders:
            continue
        if items.is_dir():
            parse(items)
        elif items.is_file():
            sort_files(items)
        print(items.name)


the_path = sys.argv[1]


# the main loop
def main():
    if len(sys.argv) < 2:
        print("Please define the name of a script file and the path to a folder you need to process")
        sys.exit(1)

    create_folders(the_path)
    parse(the_path)
    normalize(the_path)
    clean_folders(the_path)


if __name__ == '__main__':
    main()
