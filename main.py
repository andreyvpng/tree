import os
import sys


SIZE_OF_TAB = 2

num_of_dir = 0
num_of_file = 0


def print_item(tabs, item):

    if tabs:
        related = '    |  ' * tabs
    else:
        related = ''

    print('|{related}-- {item}'.format(
        related=related,
        item=item,
    ))


def show_dir(path, tabs=0):
    list = os.listdir(path)
    for item in sorted(list):
        if os.path.isdir(path + '/' + item):
            global num_of_dir
            num_of_dir += 1

            print_item(item=item, tabs=tabs)
            show_dir(path + '/' + item, tabs + 1)
        else:
            global num_of_file
            num_of_file += 1

            print_item(item=item, tabs=tabs)


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        path = os.getcwd()
    print(os.path.basename(path))
    show_dir(path)
    print('\n{} directories, {} files'.format(num_of_dir,
                                              num_of_file))


if __name__ == '__main__':
    main()
