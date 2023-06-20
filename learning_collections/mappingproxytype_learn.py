from types import MappingProxyType


def main():
    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)

    # The proxy is read-only:
    print(read_only)

    # Updates to the original are reflected in the proxy:
    writable['one'] = 42
    print(read_only)
    read_only['one'] = 23  # raises TypeError


if __name__ == '__main__':
    main()
