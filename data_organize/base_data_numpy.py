import json
import random

import numpy as np


def main():
    # npy_block_array_generate()
    # npy_miner_array_generate()
    npy_block_array_generate_with_index()
    # npy_miner_suffhe_array_generate()


def npy_block_array_generate():
    path_blocos = '../resources/blocos.json'
    path_block_array = '../resources/block_array'
    f = open(path_blocos)

    data = json.load(f)
    block_array = []

    for i in data:
        block_array.append(i['miner_adress'])

    np.save(path_block_array, block_array, allow_pickle=True)
    f.close()


def npy_block_array_generate_with_index():
    block_array = np.load('../resources/block_array.npy')
    miner_array = np.load('../resources/miner_shuffle_array.npy')
    miner_array_with_index = list(miner_array)
    block_integer_array_np = ('../resources/block_integer_array')
    block_integer_array = []

    for block in block_array:
        block_integer_array.append(miner_array_with_index.index(block))

    np.save(block_integer_array_np, block_integer_array, allow_pickle=True)


def npy_miner_array_generate():
    path_miner = '../resources/miner.json'
    path_miner_array = '../resources/miner_array'
    f = open(path_miner)

    data = json.load(f)
    miner_array = []

    for i in data:
        miner_array.append(i['address'])

    np.save(path_miner_array, miner_array, allow_pickle=True)
    f.close()

def npy_miner_suffhe_array_generate():
    miner_array = list(np.load('../resources/miner_array.npy'))
    random.shuffle(miner_array)
    path_miner_array = '../resources/miner_shuffle_array'

    np.save(path_miner_array, miner_array, allow_pickle=True)


if __name__ == "__main__":
    main()
