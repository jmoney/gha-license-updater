import argparse
import datetime
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Update LICENSE file with current year")
    parser.add_argument('--file', '-f', type=str, default='LICENSE', help='Path to LICENSE file', dest='file')
    parser.add_argument('--year', '-y', type=int, default=datetime.date.today().year, help='Year to update LICENSE file to', dest='year')
    parser.add_argument('--transform', '-t', type=str, default='\[(\d{4})\]', help='Transform string to replace with year', dest='transform')
    parser.add_argument('--output', '-o', type=str, default='/dev/stdout', help='Path to output LICENSE file', dest='output')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        data = f.read()

    with open(args.output, 'w') as f:
        f.write(re.sub(args.transform, f"[{args.year}]", data))