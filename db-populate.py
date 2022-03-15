import sqlite3

db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute(""" 
INSERT INTO contact_details (firstname, surname, street_adress, suburb) VALUES
('Adeeb', 'Khan', 'chak', 'lucknow'),
('Saad', 'Ahmad', 'indra', 'delhi'),
('Ayaaz', 'Haq', 'Ali ganj', 'muarda')
""")

connie.commit()
connie.close()