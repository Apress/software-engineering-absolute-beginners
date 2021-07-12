SELECT * FROM clients cl JOIN cities cit ON cl.city_id = cit.id

SELECT * FROM clients cl JOIN cities cit ON cl.city_id = cit.id WHERE cit.city = 'London'

SELECT * FROM clients c JOIN client_languages cl ON c.id=cl.client_id
JOIN languages l ON l.id = cl.language_id

SELECT *
FROM clients c JOIN client_languages cl ON c.id=cl.client_id
JOIN languages l ON l.id = cl.language_id
WHERE l.language = 'German'


SELECT * FROM
clients c JOIN client_languages cl ON c.id=cl.client_id
JOIN languages l ON l.id = cl.language_id
JOIN salutations s on s.id=c.salutation_id

SELECT * FROM
clients cl JOIN cities cit ON cl.city_id = cit.id
WHERE cit.city = 'London'
