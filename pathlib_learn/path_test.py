from pathlib import Path, PurePath


def main():
    p = Path('/home/vskesha/Python')
    list_dir = [x for x in p.iterdir() if x.is_dir()]
    print(list_dir)

    print(list(p.glob('**/*.py')))

    p = Path('/etc')
    q = p/'init.d'/'reboot'
    print(p)
    print(q)
    print(q.resolve())


if __name__ == '__main__':
    main()
