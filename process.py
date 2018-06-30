import os
import re


def main():
    results = set()
    with open(os.path.join('original', 'purevolume-artists'), 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) != 0 and not re.search('[^A-Za-z0-9]+', line):
                results.add('artist:' + line)
    with open('0000_artists.txt', 'w') as f:
        f.write('\n'.join(sorted(results)))

if __name__ == '__main__':
    main()

