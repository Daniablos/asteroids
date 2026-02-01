#запуск игры
run:
	python main.py

#Pylint
lint:
	pylint --recursive=y . --ignore=venv,env,.venv,dist,build