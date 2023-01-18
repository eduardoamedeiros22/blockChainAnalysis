import numpy as np


def main():
    miner_list = list(np.load('../resources/miner_shuffle_array.npy'))
    miner_traduction_table(miner_list)


def miner_traduction_table(miner_list):
    for miner in miner_list:
        print("{} & {}".format(miner_list.index(miner), miner))


if __name__ == "__main__":
    main()
