import numpy
from db_connection.connection import get_database


def main():
    dbname = get_database()
    collection_blocks = dbname["consecutive_mining_final"]

    sql_list = list(collection_blocks.find())

    # a = numpy.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    numpy.save("./testes", sql_list, allow_pickle=True)

    print(numpy.load('./testes.npy', allow_pickle=True))


if __name__ == "__main__":
    main()
