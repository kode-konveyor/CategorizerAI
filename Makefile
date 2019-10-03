export MODEL_BASENAME=categorizerai
export REPO_NAME=CategorizerAI
export GITHUB_ORGANIZATION=kode-konveyor
export SONAR_ORG=$(GITHUB_ORGANIZATION)

all: compile categorizerai.compiled

buildreports: compile

shippable/xml:
	mkdir -p shippable/xml

include /usr/local/toolchain/rules.python

#inputs/$(MODEL_BASENAME).issues.xml: shippable/$(MODEL_BASENAME)-testcases.xml
#	mkdir -p inputs
#	$(TOOLCHAINDIR)/tools/getGithubIssues >inputs/$(MODEL_BASENAME).issues.xml

codedocs: shippable/$(MODEL_BASENAME)-testcases.xml shippable/$(MODEL_BASENAME)-implementedBehaviours.xml shippable/$(MODEL_BASENAME)-implementedBehaviours.html shippable/bugpriorities.xml

shippable/$(MODEL_BASENAME)-testcases.xml: $(MODEL_BASENAME).richescape shippable
	zenta-xslt-runner -xsl:xslt/generate_test_cases.xslt -s $(MODEL_BASENAME).richescape outputbase=shippable/$(MODEL_BASENAME)-

shippable/$(MODEL_BASENAME)-implementedBehaviours.xml: buildreports shippable $(MODEL_BASENAME).rich
	zenta-xslt-runner -xsl:xslt/generate-behaviours.xslt -s target/test/javadoc.xml outputbase=shippable/$(MODEL_BASENAME)-

upload: compile
	python3 -m twine upload dist/*

