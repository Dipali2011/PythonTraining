import argparse

parse = argparse.ArgumentParser(description='example')
parse.add_argument('-a',action="store_true", default=False)
parse.add_argument('-b',action="store", dest='a')
parse.add_argument('-c',action="store", dest='c',type=int)


print(parse.parse_args(['-a','-b','priti', '-c', '3']))
