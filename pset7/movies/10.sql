/* escreva uma consulta SQL para listar os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0 */

SELECT DISTINCT(name) FROM people WHERE id IN
(SELECT person_id FROM directors WHERE movie_id IN
(SELECT movie_id FROM ratings WHERE rating >= 9))