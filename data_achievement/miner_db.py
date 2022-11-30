from db_connection.connection import get_database
from model.miner import Miner
import json

def main():

    count_blocks = 0
    dbname = get_database()
    collection_blocks = dbname["blocos"]
    collection_miner = dbname["miner"]
    blocos = list(collection_blocks.find())

    print(f'Número de blocos: {len(blocos)}')
    for bloco in blocos:
        count_blocks += 1
        miner_blocks = []
        miner_data = collection_miner.find_one({'address': bloco['miner_adress']})

        if miner_data:
            print("Já existem blocos minerados por esse minerador")
            miner_blocks = miner_data['blocks']
            miner_blocks.append(bloco['height'])
            miner = Miner(miner_data['address'], list(set(miner_blocks)))
            collection_miner.replace_one({'address': bloco['miner_adress']}, vars(miner))
        else:
            miner_blocks.append(bloco['height'])
            miner = Miner(bloco['miner_adress'], miner_blocks)
            collection_miner.insert_one(vars(miner))

    print(f'Busca completa, {count_blocks} minerados ')
    return


if __name__ == "__main__":
    main()