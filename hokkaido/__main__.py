"""
	hokkaido - geremachek (c) 2020 <http://geremachek.io/>
"""

from .util import start
import argparse
import sys

def main():
    # argparse

    p = argparse.ArgumentParser(prog="hokkaido", description="Add some zen to your terminal")
    g = p.add_mutually_exclusive_group()

    # options/arguments

    p.add_argument("COLOR", help="Hexadecimal color")
    p.add_argument("-D", "--delay", help="Time (in milliseconds) between color changes", type=int, default=500)
    p.add_argument("-c", "--cycles", help="How many 'cycles' to run before returning to the original color", type=int, default=20)

    g.add_argument("-b", "--bright", help="'Bright' breathing", action="store_true")
    g.add_argument("-d", "--dark", help="'Dark' breathing", action="store_true")
    
    args = p.parse_args()

    if not args.bright and not args.dark:
        print("rho: error: the following arguments are required: [-b | -d]", file=sys.stderr)
    else:
        try:
            start(args.COLOR, args.bright, args.dark, args.delay, args.cycles)
        except:
            print("hokkaido: error: something's not right", file=sys.stderr)

if __name__ == "__main__":
	main()
