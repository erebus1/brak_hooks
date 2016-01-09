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

Due to the way isort discovers third party packages, this hook will (and
isort) will behave differently in and outisde env which defeats the purpose
of this hook in tools like thg or your IDE.

# config
Put 'no-isort` anywhere in the commit message to skip the hook.

# Credits
- the base code was basically ripped off from https://bitbucket.org/lgs/hghooks
