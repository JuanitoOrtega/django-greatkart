# Exportar tabla
python manage.py dumpdata --indent 2 tests.UnitOfMeasurement > database.json

# Importar tabla
python manage.py loaddata database.json

# Exportar datos de varios modelos a la vez

python manage.py dumpdata --indent 2 glossaries.Country glossaries.State glossaries.Gender > database.json