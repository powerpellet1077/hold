from hold import Hold
from hold.log import Loggable
from argparse import ArgumentParser
from sys import stdout

parser = ArgumentParser(
    prog='hold',
    description='a cli tool for "holding" text or output temporarily. effectively a clipboard made only for terminals',
    add_help=False)

parser.add_argument("-k", "--key", nargs="?", default="global", help="target key to take or store from [default = global]")
parser.add_argument("-d", "--data", nargs="?", default=None, help="data to hold")
parser.add_argument("-r", "--retrieve", help="set mode to retrieve", action='store_true')
parser.add_argument("-h", "--hold", help="set mode to hold", action='store_true')
parser.add_argument("-n", "--newline", help="text returned would output a newline in addition", action='store_true')
parser.add_argument("-l", "--list", help="list all saved elements", action='store_true')
parser.add_argument("-c", "--clear", help="clears set key", action='store_true')
parser.add_argument("-?", "--help", help="provides help", action='store_true')

args = parser.parse_args()
logger = Loggable()
hold = Hold()

if args.help:
    parser.print_help()
elif args.list:
    stdout.write(hold.list())
elif args.clear:
    if args.key:
        hold.clear(key=args.key)
elif args.retrieve and args.hold:
    logger.error("cannot specify two modes at once")
elif args.retrieve:
    if args.newline:
        stdout.write(hold.retrieve(args.key)+"\n")
    else:
        stdout.write(hold.retrieve(args.key))
elif args.hold:
    if args.data:
        hold.hold(key=args.key, dat=args.data)
    else:
        logger.error("no data to hold")
else:
    logger.error("please specify a mode [r/h]")