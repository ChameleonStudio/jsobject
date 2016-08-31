upload_test:
	python3 setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

upload:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
