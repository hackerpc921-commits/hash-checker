#!/usr/bin/env python3
"""
Hash Checker - Verify file integrity using various hash algorithms
"""

import hashlib
import argparse
import sys
import os


def calculate_hash(filepath, algorithm):
    algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
    }

    if algorithm not in algorithms:
        print(f"Error: Unsupported algorithm '{algorithm}'")
        print(f"Supported: {', '.join(algorithms.keys())}")
        sys.exit(1)

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    hash_func = algorithms[algorithm]()

    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def main():
    parser = argparse.ArgumentParser(description='Verify file integrity with hashes')
    parser.add_argument('file', help='File to hash')
    parser.add_argument('-a', '--algo', default='sha256',
                        choices=['md5', 'sha1', 'sha256', 'sha512'],
                        help='Hash algorithm (default: sha256)')
    parser.add_argument('-c', '--compare', help='Compare against expected hash')

    args = parser.parse_args()

    file_hash = calculate_hash(args.file, args.algo)
    print(f"{args.algo.upper()}: {file_hash}")

    if args.compare:
        if file_hash.lower() == args.compare.lower():
            print("✓ Hash matches!")
            sys.exit(0)
        else:
            print("✗ Hash does NOT match!")
            sys.exit(1)


if __name__ == '__main__':
    main()