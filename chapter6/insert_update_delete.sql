INSERT INTO classes (salutation, name, mobile, city, languages) VALUES ('Mrs', 'Richards', '0754896325', 'London', 'German, Dutch')

INSERT INTO clients  (salutation, name, mobile, city, languages) VALUES  ('Mr', 'Eagle', '07546458745', 'Bristol', 'Dutch'),  ('Miss', 'Schofield', '0766984752', 'London', 'English')

UPDATE classes SET salutation  = 'Mr' WHERE name = 'Richards'

SELECT * FROM classes WHERE deleted_at IS NOT null

DELETE FROM classes WHERE surname = 'Rogers'