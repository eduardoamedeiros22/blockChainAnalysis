import random
import time

import numpy as np


def main():
    ## Busca os dados de mineradores e blocos ##
    ## Vetor de blocos apenas com o hash dos mineradores ##
    block_list = list(np.load('../resources/block_array.npy'))
    miner_list = list(np.load('../resources/miner_array.npy'))
    integer_block_list = list(np.load('../resources/block_integer_array.npy'))

    ini = time.time()
    # permutation_block_ordenation_consecutive_count(1000, 1000, 30000, block_list, miner_list)
    permutation_block_integer_ordenation_consecutive_count(1000, 1000, 30000, integer_block_list, miner_list)
    fim = time.time()
    print("Tempo em segundos: ", fim - ini)


def permutation_block_ordenation_consecutive_count(number_of_permutations, k_value, initial_block, blocks, miners):

    structure_consecutive_miner_list = []

    for miner in miners:

        # Zerando os valores de parametro
        consecutive_mining_structure = {}
        consecutive_mining_count_list = []
        block_interval = blocks[initial_block: initial_block + k_value]
        permutations = number_of_permutations

        # Iniciando as permutações
        while permutations > 0:
            repetition_count = 0
            previous_block = "none"
            for bloco in block_interval:
                if bloco == miner:
                    if bloco == previous_block:
                        repetition_count += 1
                previous_block = bloco
            consecutive_mining_count_list.append(repetition_count)
            permutations -= 1
            random.shuffle(block_interval)

        # Salva a estrutura por minerador
        consecutive_mining_structure['miner'] = miner
        consecutive_mining_structure['consecutive_analysis'] = consecutive_mining_count_list
        structure_consecutive_miner_list.append(consecutive_mining_structure)

    print(structure_consecutive_miner_list)


def permutation_block_integer_ordenation_consecutive_count(number_of_permutations, k_value, initial_block, blocks, miners):

    structure_consecutive_miner_list = []
    miners_list = list(miners)

    for miner in miners:

        # Zerando os valores de parametro
        consecutive_mining_structure = {}
        consecutive_mining_count_list = []
        block_interval = blocks[initial_block: initial_block + k_value]
        permutations = number_of_permutations

        # Iniciando as permutações com análise
        while permutations > 0:
            repetition_count = 0
            previous_block = -1
            for bloco in block_interval:
                if bloco == miners_list.index(miner):
                    if bloco == previous_block:
                        repetition_count += 1
                previous_block = bloco
            consecutive_mining_count_list.append(repetition_count)
            permutations -= 1
            random.shuffle(block_interval)

        # Salva a estrutura por minerador
        consecutive_mining_structure['miner'] = miner
        consecutive_mining_structure['consecutive_analysis'] = consecutive_mining_count_list
        structure_consecutive_miner_list.append(consecutive_mining_structure)

    print(structure_consecutive_miner_list)


if __name__ == "__main__":
    main()
