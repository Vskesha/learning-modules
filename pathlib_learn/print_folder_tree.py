from pathlib import Path
import sys


def print_tree_folder(path, depth=0, curr_depth=0):
    for child in path.iterdir():
        if child.is_dir():
            print('    ' * curr_depth, child.name, sep='')
            if not depth or curr_depth < depth:
                print_tree_folder(child, depth, curr_depth + 1)
    for child in path.iterdir():
        if child.is_file():
            print('    ' * curr_depth, child.name, sep='')


def get_path() -> Path:
    folder = ''
    p = None
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    while True:
        if not folder:
            folder = input('Enter the path to folder (c - current): ')
        else:
            if folder == 'c':
                p = Path()
                break
            p = Path(folder)
            if p.exists() and p.is_dir():
                break
            else:
                print(f'There is no such folder: "{folder}"')
                folder = ''
    return p


def get_depth():
    num = ''
    if len(sys.argv) > 2:
        num = sys.argv[2]
    while True:
        if not num:
            num = input('Enter the depth of tree to show (0 - max size): ')
        try:
            d = int(num)
        except ValueError:
            print(f'{num} - is not a number. Please enter number')
            num = ''
        else:
            if d < 0:
                print('Please enter a positive number')
                num = ''
            else:
                return d


def main():
    path = get_path()
    depth = get_depth()
    print_tree_folder(path, depth)


if __name__ == '__main__':
    main()
