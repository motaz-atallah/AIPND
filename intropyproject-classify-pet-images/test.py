import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--test', dest='accumulate', action='store_const',
                        const=sum, default=min,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='increase output verbosity')

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode activated!")

    result = args.accumulate(args.integers)
    print("Result:", result)

if __name__ == '__main__':
    main()
