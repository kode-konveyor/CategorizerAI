
compile:
	./setup.py bdist_wheel

upload: compile
	python3 -m twine upload dist/*

clean:
	git clean -fdx
