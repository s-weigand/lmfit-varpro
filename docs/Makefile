# Minimal makefile for Sphinx documentation
#
# get the right python version in case someone is using system python
python2_sys_alias=python
python3_sys_alias=python3
IS_PROPER_PYTHON = $(shell $(python2_sys_alias) -c 'from __future__ import print_function;import sys; print(int(sys.version_info >= (3,6)))')
ifeq ("$(IS_PROPER_PYTHON)","1")
PYTHON_TO_USE=$(python2_sys_alias)
.PHONY: which_python
else
IS_PROPER_PYTHON = $(shell $(python3_sys_alias) -c 'from __future__ import print_function;import sys; print(int(sys.version_info >= (3,6)))')
ifeq ("$(IS_PROPER_PYTHON)","1")
PYTHON_TO_USE=$(python3_sys_alias)
.PHONY: which_python
else
$(error You need at least python 3.6 with lmfit-varpro installed to work on lmfit-varpro documentation)
endif
endif


# You can set these variables from the command line.
SPHINXOPTS    = -W
SPHINXBUILD   = $(PYTHON_TO_USE) -msphinx
SPHINXPROJ    = glotaran
SOURCEDIR     = .
BUILDDIR      = _build
API_TOCTREE_DIR	= api

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

clean_all:
	rm -rf $(BUILDDIR)/*
	rm -rf $(API_TOCTREE_DIR)/*

api_docs:
	$(PYTHON_TO_USE) generate_api_documentation.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
