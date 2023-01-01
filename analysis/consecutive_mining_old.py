import random

from db_connection.connection import get_database


def main():
    dbname = get_database()
    collection_blocks = dbname["blocos"]
    blocks = list(collection_blocks.find())

    # Separação dos blocos em meses
    n = int(len(blocks) / 12)
    blocos_separados = [
        blocks[idx:idx + n] for idx in range(0, len(blocks), n)
    ]

    print(len(blocos_separados))

    # Utilizado para começar a analise de permutação a partir de um mês diferente do primeiro
    # month_count = 7

    # Função que une as análises em um único index no banco
    # unify_months(13)

    # O primeiro mês de blocos era diferente do resto, precisando de uma função so pra ele
    # for grupo_blocos in blocos_separados:
    #     primary_block_ordenation_consecutive_count(month_count, grupo_blocos)
    #     permutation_block_ordenation_consecutive_count(1000, month_count, grupo_blocos)
    #     month_count += 1


def permutation_block_ordenation_consecutive_count(number_of_permutations, month_count, blocks):
    dbname = get_database()
    collection_consecutive = dbname["consecutive_mining_month_" + str(month_count)]
    blocos = blocks
    miners = list(collection_consecutive.find())

    previous_block = {}
    structure_consecutive_miner_list = []

    while number_of_permutations > 0:
        random.shuffle(blocos)
        for miner in miners:
            repetition_count = 0
            for bloco in blocos:
                if previous_block:
                    if bloco['miner_adress'] == miner['miner']:
                        if bloco['miner_adress'] == previous_block['miner_adress']:
                            repetition_count += 1
                previous_block = bloco
            miner[str(month_count)].append(repetition_count)
            structure_consecutive_miner_list.append(dict(miner))

        for miner_dict in structure_consecutive_miner_list:
            collection_consecutive.replace_one({'miner': miner_dict['miner']}, dict(miner_dict))
        number_of_permutations -= 1


def primary_block_ordenation_consecutive_count(month_count, blocks):
    dbname = get_database()
    collection_consecutive = dbname["consecutive_mining_month_" + str(month_count)]
    collection_miner = dbname["miner"]
    blocos = blocks
    miners = list(collection_miner.find())

    previous_block = {}
    structure_consecutive_miner = {}
    structure_consecutive_miner_list = []

    for miner in miners:
        repetition_count = 0
        structure_consecutive_miner['miner'] = miner['address']
        structure_consecutive_miner[str(month_count)] = []
        for bloco in blocos:
            if previous_block:
                if bloco['miner_adress'] == structure_consecutive_miner['miner']:
                    if bloco['miner_adress'] == previous_block['miner_adress']:
                        repetition_count += 1
            previous_block = bloco
        structure_consecutive_miner[str(month_count)].append(repetition_count)
        structure_consecutive_miner_list.append(dict(structure_consecutive_miner))

    for structure_consecutive_miner_dict in structure_consecutive_miner_list:
        collection_consecutive.insert_one(dict(structure_consecutive_miner_dict))


def unify_months(number_of_months_saved):
    dbname = get_database()
    collection_consecutive = dbname["consecutive_mining_month_1"]
    collection_consecutive_final = dbname['consecutive_mining_final']
    miners = list(collection_consecutive.find())

    for miner in miners:
        collection_consecutive_final.insert_one(dict(miner))

    while number_of_months_saved > 1:
        collection_consecutive_sequencial = dbname["consecutive_mining_month_" + str(number_of_months_saved)]
        miners_replace = list(collection_consecutive_sequencial.find())
        miners_final = list(collection_consecutive_final.find())
        final_structure_consecutive_analysis = {}
        final_structure_list = []
        for miner_final in miners_final:
            for miner_rep in miners_replace:
                if miner_rep['miner'] == miner_final['miner']:
                    final_structure_consecutive_analysis = dict(miner_final)
                    final_structure_consecutive_analysis[str(number_of_months_saved)] = miner_rep[
                        str(number_of_months_saved)]
                    final_structure_list.append(final_structure_consecutive_analysis)
                continue

        for final in final_structure_list:
            collection_consecutive_final.replace_one({'miner': final['miner']}, dict(final))

        number_of_months_saved -= 1


if __name__ == "__main__":
    main()
