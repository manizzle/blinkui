
venv: requirements.txt
	python ./vendor/venv-update venv= venv -ppython3 install= -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv
