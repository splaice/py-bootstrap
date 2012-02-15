.PHONY: all pep8 pyflakes

GITIGNORES=$(shell cat .gitignore |tr "\\n" ",")

all: pep8

pep8: .gitignore
	pep8 . --exclude=$(GITIGNORES)

#TODO: setup pyflakes to run @splaice
pyflakes:
	@pyflakes .
