import argparse
import argparse_addons


parser = argparse.ArgumentParser()

parser.add_argument('--min-max',
                    type=argparse_addons.Integer(0, 255),
                    help='an integer in the range 0..255')
parser.add_argument('--min',
                    type=argparse_addons.Integer(0, None),
                    help='an integer in the range 0..inf')
parser.add_argument('--max',
                    type=argparse_addons.Integer(None, 255),
                    help='an integer in the range -inf..255')
parser.add_argument('--any',
                    type=argparse_addons.Integer(),
                    help='any integer')

args = parser.parse_args()

print(f'--min-max: {args.min_max}')
print(f'--min:     {args.min}')
print(f'--max:     {args.max}')
print(f'--any:     {args.any}')
