from db_connection.connection import get_database
from blockchain import blockexplorer
import time

# Baseado na média de 10 minutos para a aparição de um novo bloco
BLOCKS_PER_DAY = 144
BLOCKS_PER_YEAR = 52560
# Mês com 30 dias
BLOCKS_PER_MONTH = 4320


def main():
    # Instanciando o banco
    dbname = get_database()
    collection_name = dbname["blocos"]

    # Pegando o hash do ultimo bloco minerado
    # lasted_block = blockexplorer.get_latest_block()
    bloco = collection_name.find_one({"hash": "hash do bloco inicial"})

    # Bloco completo e transformação em dicionário (recebe o hash do block ou height)
    block = blockexplorer.get_block(str(bloco['height']))

    # Preparação do json final com endereço do minerador
    block_dict = coin_base_tx(block)

    # Primeira inserção no banco
    collection_name.insert_one(block_dict)
    print(block_dict)

    # Hash do bloco anterior
    block_hash = block.previous_block

    # Número de blocos a serem buscados
    block_count = BLOCKS_PER_MONTH

    # Inserção em loop utilizando o bloco anterior
    for i in range(1125):
        time.sleep(2)
        if i % 10 == 0:
            print("Number of blocks processed: " + str(i))
        prev_block = blockexplorer.get_block(block_hash)
        prev_block_dict = coin_base_tx(prev_block)
        collection_name.insert_one(prev_block_dict)
        block_hash = prev_block.previous_block


def coin_base_tx(block):
    block_dict = vars(block)
    miner_adress = str(block.transactions[0].outputs[0].address)
    coin_base_output = str(block.transactions[0].outputs[0].value)
    block_dict['tx_indexes'] = []
    block_dict['transactions'] = []
    block_dict['miner_adress'] = miner_adress
    block_dict['coin_base_output'] = coin_base_output
    return block_dict


if __name__ == "__main__":
    main()
