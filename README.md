# Brak hooks

A collection of repository hooks. Well, currently one - mercurial isort.

# How to install and use

```
# sudo or --user, anywhere where mercurial lives
pip install --user --upgrade git+git://github.com/bartekbrak/brak_hooks.git
```

```
#.hg/hgrc
[hooks]
pretxncommit.isort = python:brak_hooks.code.isort
```
