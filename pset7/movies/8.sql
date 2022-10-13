/* escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram Toy Story. */

SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE title = "Toy Story"))