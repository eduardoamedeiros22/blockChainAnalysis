import matplotlib.pyplot as plt
import nltk as nltk
import random
import numpy as np

nltk.download('inaugural')


def main():
    # Bloco mais antigo =  height: 684192, tempo: 2021-05-19 12:49:40 , tempo unix: 1621428580
    # Bloco mais novo =  height: 737327, tempo: 2022-05-21 17:37:25, tempo unix: 1653154645
    block_list = list(np.load('../resources/block_array.npy'))
    contador = 0

    x_height_total = []
    y_hash_total = []

    x_height_first_20k = []
    y_hash_first_20k = []

    x_height_middle_20k = []
    y_hash_middle_20k = []

    x_height_last_20k = []
    y_hash_last_20k = []

    x_height_middle = []
    y_hash_midle= []
    print(block_list[45001])
    # for block in block_list:
    #     x_height_total.append(block_list.index(block))
    #     y_hash_total.append(block)
    #     if 45000 < contador < 50000:
    #         x_height_middle.append(block_list.index(block))
    #         y_hash_midle.append(block)
        # if 10000 < contador < 20000:
        #     x_height_first_20k.append(block_list.index(block))
        #     y_hash_first_20k.append(block)
        # elif 40000 >= contador > 20000:
        #     x_height_middle_20k.append(block_list.index(block))
        #     y_hash_middle_20k.append(block)
        # else:
        #     x_height_last_20k.append(block_list.index(block))
        #     y_hash_last_20k.append(block)

        # contador += 1

    # plt.scatter(x=x_height_total, y=y_hash_total, marker='|')
    # plt.gca().axes.get_yaxis().set_visible(False)
    # plt.show()


if __name__ == "__main__":
    main()
