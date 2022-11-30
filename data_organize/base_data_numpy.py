import json
import numpy as np


def main():
    npy_block_array_generate()
    npy_miner_array_generate()


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


if __name__ == "__main__":
    main()
