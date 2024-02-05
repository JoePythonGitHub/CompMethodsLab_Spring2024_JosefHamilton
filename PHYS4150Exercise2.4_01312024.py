import argparse
parser = argparse.ArgumentParser()

parser.add_argument('v',type=float) 
parser.add_argument('x',type=float)
args = parser.parse_args()
print(args.v, args.x)
t = args.x / args.v