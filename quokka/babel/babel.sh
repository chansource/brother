#!/bin/sh
pybabel extract -F babel.ini -k _l -k _gettext -k _ngettext -k lazy_gettext -o quokka.pot --project quokka ..
