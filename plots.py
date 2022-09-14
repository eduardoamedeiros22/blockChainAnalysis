import matplotlib.pyplot as plt
import nltk as nltk

nltk.download('inaugural')
from db_connection.connection import get_database


def main():
    # Bloco mais antigo =  height: 684192, tempo: 2021-05-19 12:49:40 , tempo unix: 1621428580
    # Bloco mais novo =  height: 737327, tempo: 2022-05-21 17:37:25, tempo unix: 1653154645
    dbname = get_database()
    collection_blocos = dbname["blocos"]
    mineradores = list(collection_blocos.find())
    contador = 0

    x_height_total = []
    y_hash_total = []

    x_height_first_20k = []
    y_hash_first_20k = []

    x_height_middle_20k = []
    y_hash_middle_20k = []

    x_height_last_20k = []
    y_hash_last_20k = []
    for minerador in mineradores:
        x_height_total.append(minerador['height'])
        y_hash_total.append(minerador['miner_adress'])
        if 10000 < contador < 20000:
            x_height_first_20k.append(minerador['height'])
            y_hash_first_20k.append(minerador['miner_adress'])
        elif 40000 >= contador > 20000:
            x_height_middle_20k.append(minerador['height'])
            y_hash_middle_20k.append(minerador['miner_adress'])
        else:
            x_height_last_20k.append(minerador['height'])
            y_hash_last_20k.append(minerador['miner_adress'])

        contador += 1

    plt.scatter(x=x_height_total, y=y_hash_total, marker='|')
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()


if __name__ == "__main__":
    main()
