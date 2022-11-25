from Module1 import hostblacklist


import argparse


parser = argparse.ArgumentParser(prefix_chars='-')

parser.add_argument('hostname', type=str, nargs=1)


var = parser.parse_args()

print(hostblacklist(var.hostname[0]))





