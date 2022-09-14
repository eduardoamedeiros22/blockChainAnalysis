from db_connection.connection import get_database


def main():
    dbname = get_database()
    collection_miner = dbname["miner"]
    collection_consecutive = dbname["consecutive_mining"]
    mineradores = list(collection_miner.find())
    for minerador in mineradores:
        structure_consecutive_miner = {}
        block_list = minerador['blocks']
        previous_block = 0
        consecutive = 0
        max_consecutive = 0
        for block in block_list:
            if block == previous_block + 1:
                consecutive += 1
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
            else:
                consecutive = 1
            previous_block = block
        structure_consecutive_miner['miner'] = minerador['address']
        structure_consecutive_miner['consecutive_mining'] = max_consecutive
        collection_consecutive.insert_one(structure_consecutive_miner)


if __name__ == "__main__":
    main()
