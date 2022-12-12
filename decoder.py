import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--alg', help='Algorithm (e.g. viterbi)', required=True)
    parser.add_argument('seq',
                        help='A sequence over the alphabet (e.g. ACTGGACTACGTCATGCA or 1621636142516152416616666166616)')
    parser.add_argument('initial_emission', help='Path to emission table (e.g. initial_emision.tsv)')
    parser.add_argument('p', help='probability to transition from state 1 to state 2 (e.g. 0.01)', type=float)
    parser.add_argument('q', help='probability to transition from state 2 to state 1 (e.g. 0.5)', type=float)
    parser.add_argument('p0', help='intial probability of entering state 1 (e.g. 0.9)', type=float)
    args = parser.parse_args()

    if args.alg == 'viterbi':
        raise NotImplementedError

    elif args.alg == 'forward':
        raise NotImplementedError

    elif args.alg == 'backward':
        raise NotImplementedError

    elif args.alg == 'posterior':
        raise NotImplementedError


if __name__ == '__main__':
    main()
