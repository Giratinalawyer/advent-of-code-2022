import argparse
import subprocess
import sys
import pip._vendor.requests 

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5f4e23d5693c9c5b1a986d7c66e6a7f1665cb4e3805ffae6540dd6f7f8297e3996806249043032856335e73e646d3657faa79a45b1c44c27f6'

useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=7)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}"' #-A {useragent} commented out
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)