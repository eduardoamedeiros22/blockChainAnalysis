from db_connection.connection import get_database
from model.miner import Miner


def main():
    dbname = get_database()
    collection_miner = dbname["miner"]
    mineradores = list(collection_miner.find())

    for minerador in mineradores:
        block_count = len(minerador['blocks'])
        ordened_blocks = sorted(minerador['blocks'])
        miner = Miner(minerador['address'], ordened_blocks, block_count)
        collection_miner.replace_one({'address': minerador['address']}, vars(miner))


if __name__ == "__main__":
    main()
