import random

from db_connection.connection import get_database


def main():
    # primary_block_ordenation_consecutive_count()
    permutation_block_ordenation_consecutive_count(10)


def permutation_block_ordenation_consecutive_count(number_of_permutations):
    dbname = get_database()
    collection_blocks = dbname["blocos"]
    collection_consecutive = dbname["consecutive_mining"]
    blocos = list(collection_blocks.find())
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
            miner['consecutive_mining'].append(repetition_count)
            structure_consecutive_miner_list.append(dict(miner))

        for miner_dict in structure_consecutive_miner_list:
            collection_consecutive.replace_one({'miner': miner_dict['miner']}, dict(miner_dict))
        number_of_permutations -= 1


def primary_block_ordenation_consecutive_count():
    dbname = get_database()
    collection_blocks = dbname["blocos"]
    collection_consecutive = dbname["consecutive_mining"]
    collection_miner = dbname["miner"]
    blocos = list(collection_blocks.find())
    miners = list(collection_miner.find())

    previous_block = {}
    structure_consecutive_miner = {}
    structure_consecutive_miner_list = []

    for miner in miners:
        repetition_count = 0
        structure_consecutive_miner['miner'] = miner['address']
        structure_consecutive_miner['consecutive_mining'] = []
        for bloco in blocos:
            if previous_block:
                if bloco['miner_adress'] == structure_consecutive_miner['miner']:
                    if bloco['miner_adress'] == previous_block['miner_adress']:
                        repetition_count += 1
            previous_block = bloco
        structure_consecutive_miner['consecutive_mining'].append(repetition_count)
        structure_consecutive_miner_list.append(dict(structure_consecutive_miner))

    for structure_consecutive_miner_dict in structure_consecutive_miner_list:
        collection_consecutive.insert_one(dict(structure_consecutive_miner_dict))


if __name__ == "__main__":
    main()
