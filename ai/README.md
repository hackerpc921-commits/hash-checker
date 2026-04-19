# Hash Checker

A simple CLI tool to verify file integrity using cryptographic hash functions.

## Features

- Calculate MD5, SHA1, SHA256, and SHA512 hashes
- Compare hashes against expected values
- Simple command-line interface

## Installation

```bash
git clone https://github.com/yourusername/hash_checker.git
cd hash_checker
```

## Usage

```bash
# Calculate SHA256 hash (default)
python hash_checker.py file.txt

# Calculate specific hash
python hash_checker.py file.zip -a sha512

# Compare against expected hash
python hash_checker.py file.zip -a sha256 -c "abc123..."
```

## Options

- `-a, --algo` - Hash algorithm: md5, sha1, sha256, sha512 (default: sha256)
- `-c, --compare` - Compare against expected hash

## License

MIT