# To run script and start an interactive session (REPL):
# $ python -i test.py --host=http://checkboxmini.local:5000

from checkbox import Ping, Config, Keyboard, Mouse, MouseKeys, Screenshot

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--host',
                    help="host of the Checkbox API server\n" + \
                          "default host is http://localhost:5000\n" + \
                           "example:\n  python test.py --host=http://locahost:5000")
args = parser.parse_args()
if args.host:
    host = args.host
else:
    host = "http://localhost:5000"

print("Using API host: %s" % host)

# Class init
c = Config(host)
k = Keyboard(host)
p = Ping(host)
m = Mouse(host)
mk = MouseKeys(host)
s = Screenshot(host)

# Shortcuts
ping = p.ping