import random
import time

import numpy as np


def main():
    ## Busca os dados de mineradores e blocos ##
    ## Vetor de blocos apenas com o hash dos mineradores ##
    block_list = list(np.load('../resources/block_array.npy'))
    miner_list = list(np.load('../resources/miner_shuffle_array.npy'))
    integer_block_list = list(np.load('../resources/block_integer_array.npy'))
    month_count = int(len(integer_block_list) / 12)
    number_of_permutations = 10000
    month = 0

    ini = time.time()

    for i in range(12):

        block_interval = integer_block_list[i * month_count: i * month_count + month_count]

        mining_power_list = mining_power(block_interval)

        final_interval_consecutive_mining, original_consecutive_analysis = \
            permutation_block_integer_ordenation_consecutive_count_improve(number_of_permutations, block_interval)

        consecutive_analisys_organize(final_interval_consecutive_mining, number_of_permutations,
                                      month, mining_power_list, original_consecutive_analysis)

        month += 1
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


def permutation_block_integer_ordenation_consecutive_count_improve(number_of_permutations, block_interval):
    # Zerando os valores de parametro
    structure_consecutive_miner_list = []
    consecutive_mining_count_list = []
    permutations = number_of_permutations
    final_interval_consecutive_mining = []

    for i in range(89):
        consecutive_mining_count_list.append(0)

    # Iniciando as permutações com análise
    while permutations > 0:
        previous_block = -1
        for bloco in block_interval:
            if bloco == previous_block:
                consecutive_mining_count_list[bloco] += 1
            previous_block = bloco
        permutations -= 1
        random.shuffle(block_interval)
        structure_consecutive_miner_list.append(consecutive_mining_count_list)
        consecutive_mining_count_list = []
        for i in range(89):
            consecutive_mining_count_list.append(0)

    first_analisys = structure_consecutive_miner_list.pop(0)
    # Código aqui gera um grande vetor com vários vetores dentro
    # Os vetores internos "consecutive_mining_count_list" possuem 89 posições representando a contagem de minerações consecutivas de cada minerador
    # O vetor maior "structure_consecutive_miner_list" armazena x(numero de permutações) vetores internos

    # Nessa parte serão comparados o valores da distribuição original com as permutações
    # O resultado será salvo em um vetor com os mineradores identificados pelo index , ou seja, um vetor com 89 posições
    for i in range(89):
        final_interval_consecutive_mining.append(0)

    for miner_analisys in structure_consecutive_miner_list:
        for i in range(89):
            if first_analisys[i] > miner_analisys[i]:
                final_interval_consecutive_mining[i] += 1

    # print(final_interval_consecutive_mining)

    return final_interval_consecutive_mining, first_analisys


def mining_power(integer_block_list):
    mining_power_list = []
    for i in range(89):
        mining_power_list.append(0)

    for block in integer_block_list:
        mining_power_list[block] += 1

    return mining_power_list


def consecutive_analisys_organize(analysis_list, number_of_permutations, month, mining_power_list,
                                  original_consecutive_analysis):
    for analysis in analysis_list:
        if analysis >= int(number_of_permutations * 0.95):
            print("Month: {}, Suspicious Miner : {}, Consecutive Analysis: {}, "
                  "Mining_Power: {}, First Consecutive Analysis (Without Shuffle): {}"
                  .format(month, analysis_list.index(analysis), analysis,
                          mining_power_list[analysis_list.index(analysis)],
                          original_consecutive_analysis[analysis_list.index(analysis)]))


if __name__ == "__main__":
    main()
