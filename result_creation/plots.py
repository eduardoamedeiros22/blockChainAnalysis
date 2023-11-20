import matplotlib.pyplot as plt
import nltk as nltk
import numpy as np
import random

nltk.download('inaugural')
from db_connection.connection import get_database


def main():
    # Bloco mais antigo =  height: 684192, tempo: 2021-05-19 12:49:40 , tempo unix: 1621428580
    # Bloco mais novo =  height: 737327, tempo: 2022-05-21 17:37:25, tempo unix: 1653154645
    dbname = get_database()
    collection_blocos = dbname["blocos"]
    miners = list(np.load('../resources/miner_shuffle_array.npy'))
    mineradores = list(collection_blocos.find())
    random.shuffle(miners)
    contador = 0

    x_height_total = []
    y_hash_total = []
    for minerador in mineradores:
        contador += 1
        x_height_total.append(minerador['height'])
        y_hash_total.append(return_index_miner(miners, minerador['miner_adress']))
        # if contador == 4000:
        #     break

    plt.scatter(x=x_height_total, y=y_hash_total, marker='|')
    plt.gca().axes.get_yaxis().set_visible(True)
    plt.show()


def return_index_miner(miner_array, miner):
    for miner_hash in miner_array:
        if miner_hash == miner:
            return miner_array.index(miner_hash)



if __name__ == "__main__":
    main()
