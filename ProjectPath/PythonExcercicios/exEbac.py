#De alguma forma, obtivemos uma lista de filmes com valores duplicados.
#Utilize a conversão para conjunto e, em seguida, novamente para lista para remover os duplicados. Armazene o resultado de volta na variável filmes.
#Imprima o resultado

filmes = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    'The Godfather Part II',
    'The Godfather',
    '12 Angry Men',
    'Schindler\'s List',
    'The Lord of the Rings: The Return of the King',
    'Pulp Fiction',
    'The Shawshank Redemption',
    'The Lord of the Rings: The Fellowship of the Ring',
    'The Good, the Bad and the Ugly',
    'Pulp Fiction'
]

filmes_conj = set(filmes)
filmes = list(filmes_conj)
print(filmes)
