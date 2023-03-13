import markdown
import sys

def main():
    if len(sys.argv) != 4:
        print('Usage: python3 markdown.py markdown input.md output.html')
        sys.exit(1)

    command = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    with open(inputfile, "r") as i, open(outputfile, "w") as o:
        contents = i.read()
        html = markdown.markdown(contents)
        o.write(html)

if __name__ == "__main__":
    main()