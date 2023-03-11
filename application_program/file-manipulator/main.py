import sys
from os.path import exists

order = sys.argv[1]


def printer(input):
    sys.stdout.buffer.write(input.encode())
    sys.stdout.flush()


def isfile_exite(file):
    if not exists(file):
        printer("please make testfile")


def validateArgs():
    if len(sys.argv) < 4:
        printer("Invalid arguments: Not enough arguments")
        sys.exit(1)

    if order not in ['reverse', 'copy', 'duplicate-contents', 'replace-string']:
        printer(f"Invalid arguments: Invalid order {order}")
        sys.exit(1)

    if order in ['reverse', 'copy', 'duplicate-contents'] and len(sys.argv) != 4:
        printer("Invalid arguments: Invalid number of arguments")
        sys.exit(1)

    if order == 'replace-string' and len(sys.argv) != 5:
        printer("Invalid arguments: Invalid number of arguments")
        sys.exit(1)


def main():
    myfile = 'testfile'

    isfile_exite(myfile)
    validateArgs()

    with open(myfile) as f:
        content = f.read()

        if (order == 'reverse' or order == 'copy'):
            output_file = sys.argv[3]

            with open(output_file, 'a') as f:
                if order == 'reverse':
                    f.write(content[::-1])
                elif order == 'copy':
                    f.write(content)

        elif (order == 'duplicate-contents' or order == 'replace-string'):
            output_file = sys.argv[2]

            if order == 'duplicate-contents':
                with open(output_file, 'a') as f:
                    for l in range(int(sys.argv[3])):
                        f.write(content)
            elif order == 'replace-string':
                with open(output_file, 'w') as f:
                    f.write(content.replace(sys.argv[3], sys.argv[4]))


if __name__ == "__main__":
    main()
