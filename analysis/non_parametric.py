import random

from db_connection.connection import get_database


def main():
    dbname = get_database()
    collection_blocks = dbname["consecutive_mining_final"]
    consecutive_final_structure = list(collection_blocks.find())
    print(len(consecutive_final_structure))

    non_parametric_analysis(2, consecutive_final_structure)

def non_parametric_analysis(limit_distance, structure):

    miners_analysis = []

    for miner in structure:

        miner_analysis = {}
        miner_analysis['miner_hash'] = miner['miner']

        for i in range(1, 13):
            consecutive_list = miner[str(i)]
            base_consecutive_value = consecutive_list[0]
            month_analysis = {}

            higher_values = 0
            non_relevant = 0
            lower_values = 0

            for j in range(1,1001):
                if(base_consecutive_value - consecutive_list[j]) < -limit_distance:
                    higher_values += 1
                    continue
                if (base_consecutive_value - consecutive_list[j]) > limit_distance:
                    lower_values += 1
                    continue
                non_relevant += 1

            month_analysis['higher_values'] = higher_values
            month_analysis['non_relevant'] = non_relevant
            month_analysis['lower_values'] = lower_values

            miner_analysis[str(i)] = month_analysis

            miners_analysis.append(miner_analysis)

    print(miners_analysis)

if __name__ == "__main__":
    main()
