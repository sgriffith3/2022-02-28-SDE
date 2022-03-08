import argparse


parser = argparse.ArgumentParser()
parser.add_argument("color", help="choose a color")
parser.add_argument("body", help="choose a body style of vehicle")
parser.add_argument("-m", "--miles", help="how many miles is on it?", default=12000)
parser.add_argument('-w', '--write', action='store_true', default=False)
args = parser.parse_args()

print(args)
print(args.color)
print(args.body)
print(args.miles)

if args.write:
    with open("argfile.txt", "w") as f:
        f.write(f"I have a {args.color} {args.body} with {args.miles} miles on it.")


