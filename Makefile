all: compile categorizerai.compiled

buildreports: compile

shippable:
	mkdir -p shippable

shippable/xml:
	mkdir -p shippable/xml

inputs/categorizerai.issues.xml:
	mkdir -p inputs
	tools/getGithubIssues kode-konveyor CategorizerAI f279765590d25bedfc9f08f7fc39a8c39c891711 >inputs/categorizerai.issues.xml

include /usr/share/zenta-tools/model.rules

compile:
	./setup.py bdist_wheel

upload: compile
	python3 -m twine upload dist/*

clean:
	git clean -fdx
