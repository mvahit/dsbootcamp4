################################
# GITHUB
################################

commit:
	git commit -am "commit from makefile"

push:
	git push origin master

pull:
	git pull origin master

fetch:
	git fetch origin master

reset:
	rm -f .git/index
	git reset

compush: commit push



################################
# PYPI
################################

sdist:
	python setup.py sdist

upload:
	twine upload dist/*