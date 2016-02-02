# generate random data
import random
import string
import argparse
import sys

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--size", type=int, help="The size in bytes")

    return parser

def parse_arguments(arguments, parser):
    args = parser.parse_args(arguments)
    return args

def main():

    # initiate parser
    parser = create_parser()
    args = parse_arguments(sys.argv[1:], parser)

    nb = args.size
    return generate_str(nb)

def generate_str(nb):
    generated_str = ''.join(random.choice(string.ascii_lowercase +
                                          string.ascii_uppercase + string.digits) for _ in range(nb))
    return generated_str

if __name__ == "__main__":
    main()
