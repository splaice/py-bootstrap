.PHONY: all pep8 pyflakes clean

GITIGNORES=$(shell cat .gitignore |tr "\\n" ",")

all: pep8

pep8: .gitignore
	pep8 . --exclude=$(GITIGNORES)

#TODO: setup pyflakes to run @splaice
pyflakes:
	@pyflakes .

clean:
	@rm -rf build dist
