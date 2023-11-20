import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')


def main():
    # Bloco mais antigo =  height: 684192, tempo: 2021-05-19 12:49:40 , tempo unix: 1621428580
    # Bloco mais novo =  height: 737327, tempo: 2022-05-21 17:37:25, tempo unix: 1653154645

    miners_hashes = ["1GNgwA8JfG7Kc8akJ8opdNWJUihqUztfPe",
                     "1Bf9sZvBHPFGVPX71WX2njhd1NXKv5y7v5",
                     "bc1qadv9a92ln0l58hh6g0e9jeuz4y5cg0m0sjpf8x",
                     "1CK6KHY6MHgYvmRQ4PAafKYDrg1ejbH1cE",
                     "1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY",
                     "38XnPvu9PmonFU9WouPXUjYbW91wa5MerL",
                     "1JvXhnHCi6XqcanvrZJ5s2Qiv4tsmm2UMy",
                     "12dRugNcdxK39288NjcDV4GX7rMsKCGn6B",
                     "12cKiMNhCtBhZRUBCnYXo8A4WQzMUtYjmR",
                     "bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4",
                     "1EepjXgvWUoRyNvuLSAxjiqZ1QqKGDANLW",
                     "191sNkKTG8pzUsNgZYKo7DH2odg39XDAGo",
                     "bc1quyzwwznn97ydemv8l3kzk700gck2tyexd5sz0f",
                     "1JhAQ7UNYXvVvrp4nfNHLoTWTPgfuHGCDp",
                     "35y82tEPDa2wm6tzkEacMG8GPPW7zbMj83",
                     "bc1qf274x7penhcd8hsv3jcmwa5xxzjl2a6pa9pxwm",
                     "125m2H43pwKpSZjLhMQHneuTwTJN5qRyYu",
                     "19dENFt4wVwos6xtgwStA6n8bbA57WCS58"
                     ]




    miners_integers = []
    miner_array = list(np.load('../resources/miner_shuffle_array.npy'))

    for miner_hash in miners_hashes:
        for miner in miner_array:
            if miner == miner_hash:
                # miners_integers.append(miner_array.index(miner))
                miners_integers.append(miner)
                break
    # print(str(len(miners_integers)))

    # blocks = list(np.load('../resources/block_array.npy'))
    # integer_blocks = list(np.load('../resources/block_integer_array.npy'))
    integer_blocks = list(np.load('../resources/block_array.npy'))

    integers_half = integer_blocks[0:int(len(integer_blocks) / 4)]
    integers_half = integer_blocks[4667*11:int(len(integer_blocks) / 12)*12]
    integers_half = integer_blocks


    # print(len(integers_half))

    current_index = 0
    k=100
    delta=10
    mining_power_list = []
    mining_power_dict = {}

    for miner in miners_integers:
        best_hash_rate = 0
        current_delta = 0
        mining_power_miner = []
        while (current_delta + k) <= len(integers_half):
            mining_power = 0
            x = range(current_delta, current_delta + k)
            for i in x:
                if integers_half[i] == miner:
                    mining_power += 1
            mining_power_miner.append(mining_power)
            current_delta += delta
        mining_power_list.append(mining_power_miner)
        mining_power_dict[current_index] = mining_power_miner
        current_index += 1
        print("Minerador " + str(miner) + " executado")
        x = np.arange(0, len(integers_half)-100, delta)
        y = mining_power_miner
        plt.plot(x, y, label=miner, linestyle="-")

        for mp in mining_power_miner:
            if mp > best_hash_rate:
                best_hash_rate = mp
        print(best_hash_rate)


    plt.legend()
    plt.show()
    print()
    print(mining_power_list[1])
    print("Quantidade de mineradores: " + str(len(mining_power_list)))

    # make data
    # x = np.arange(0, len(integers_half)-100, delta)
    # y = np.vstack(mining_power_list)

    # plot
    # fig, ax = plt.subplots()
    #
    # ax.stackplot(x, y, labels=mining_power_dict.keys())
    # ax.legend(loc='upper left')
    #
    # plt.show()


if __name__ == "__main__":
    main()
