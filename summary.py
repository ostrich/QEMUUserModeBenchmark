#! /usr/bin/python3
import json
import argparse
from pathlib import Path

ARCH_FILE = Path("architectures.txt")
RESULTS_DIR = Path("results")

# Function to process the result file for a given architecture


def load_architectures():
    with ARCH_FILE.open('r') as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.lstrip().startswith("#")
        ]


def process_result_file(arch):
    file_path = RESULTS_DIR / f'benchmark.{arch}.json'
    with file_path.open('r') as file:
        data = json.load(file)
        results = data['results'][0]

        # Extract relevant information
        mean = results['mean']
        stddev = results['stddev']

        return mean, stddev

# Function to print data summary in plain text format


def print_plain_text(data):
    print(f"{'Architecture': <8}\t{'Mean (s)': <15}\t{'StdDev (s)': <15}")
    print("="*40)
    for arch, mean, stddev in data:
        print(f"{arch: <8}\t{mean:.6f}\t{stddev:.6f}")

# Function to print data summary in CSV format


def print_csv(data):
    print("Architecture,Mean (s),StdDev (s)")
    for arch, mean, stddev in data:
        print(f"{arch},{mean:.6f},{stddev:.6f}")

# Function to print data summary in Markdown format


def print_markdown(data):
    print(f"|{'Architecture': <8}|{'Mean (s)': <15}|{'StdDev (s)': <15}|")
    print("|" + "-"*10 + "|" + "-"*17 + "|" + "-"*17 + "|")
    for arch, mean, stddev in data:
        print(f"|{arch: <8}|{mean:.6f}|{stddev:.6f}|")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process benchmark results.')
    parser.add_argument('--format', choices=['text', 'csv', 'markdown'],
                        default='text', help='Output format (text, csv, markdown)')
    args = parser.parse_args()

    # Process each architecture and store the results
    architectures = load_architectures()
    data = []
    for arch in architectures:
        mean, stddev = process_result_file(arch)
        data.append((arch, mean, stddev))

    # Print data summary based on the selected format
    if args.format == 'text':
        print_plain_text(data)
    elif args.format == 'csv':
        print_csv(data)
    elif args.format == 'markdown':
        print_markdown(data)
