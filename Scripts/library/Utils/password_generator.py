#!/usr/bin/env python3
"""Secure password generator for this repo.

Usage:
  python Scripts/library/Utils/password_generator.py 20 --no-symbols

Arguments:
  length            Password length (default 16)
  --no-upper        Exclude uppercase letters
  --no-lower        Exclude lowercase letters
  --no-digits       Exclude digits
  --no-symbols      Exclude symbols
"""
from __future__ import annotations
import argparse
import secrets
import string
import random
from typing import List


def generate_password(length: int = 16, use_upper: bool = True, use_lower: bool = True,
                      use_digits: bool = True, use_symbols: bool = True) -> str:
    pools: List[str] = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        # A conservative symbol set similar to other utils in this repo
        pools.append('!@#$%^&*()-_=+[]{};:,.<>?')

    if not pools:
        raise ValueError('At least one character class must be enabled')

    if length < len(pools):
        raise ValueError(f'Length {length} is too small for the number of enabled classes ({len(pools)})')

    # Pick at least one character from each selected pool
    chars: List[str] = [secrets.choice(pool) for pool in pools]

    # Fill the rest
    all_chars = ''.join(pools)
    while len(chars) < length:
        chars.append(secrets.choice(all_chars))

    # Securely shuffle
    sysrand = random.SystemRandom()
    sysrand.shuffle(chars)
    return ''.join(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description='Secure password generator')
    parser.add_argument('length', nargs='?', type=int, default=16, help='Password length (default 16)')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        print(pwd)
    except ValueError as e:
        parser.error(str(e))


if __name__ == '__main__':
    main()
