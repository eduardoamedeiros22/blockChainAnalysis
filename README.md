# Intro

Codigo responsável pelas análises e armazenamento de informações na blockchain.
Trabalho realizado para elaboração do artigo de título : 
"Um método não paramétrico para identificação de anomalias na mineração do bitcoin"

## Utilização

Na pasta resources já estão as informações retiradas do banco em estruturas mais fáceis de lidar pela biblioteca NumPy

Na pasta data_organize o arquivo consecutive_mining possui um método de nome:
"permutation_block_integer_ordenation_consecutive_count_improve"
Ele é o responsável por fazer a análise de mineração consecutiva com os dados já coletados, seus parâmetros são:
    number_of_permutations = numero de permutações que serão realizadas na massa de blocos analisada
    k_value = numero de blocos em um intervalo de análise
    initial_block = bloco inicial da análise
    blocks = vetor com os blocos obtidos na rede

## Contribuição

Código escrito por Eduardo Augusto de Medeiros Silva, estudante de bacharelado em Sistemas de informação na Universidade
Federal de Uberlândia.

O código também conta com contribuição de Ivan da Silva Sendin, docente na Faculdade de Computação da Universidade Federal
de Uberlândia