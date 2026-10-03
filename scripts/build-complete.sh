#!/bin/sh
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
set -eu
cd "$(dirname "$0")/../tex"
mkdir -p ../tmp/build ../output/pdf
if command -v lualatex >/dev/null 2>&1; then
 e65_latex_engine=lualatex
elif test -x /Library/TeX/texbin/lualatex; then
 e65_latex_engine=/Library/TeX/texbin/lualatex
else
 printf '%s\n' 'LuaLaTeX was not found. Install a compatible TeX Live distribution and add lualatex to PATH.' >&2
 exit 1
fi
for pass in 1 2 3; do
 "$e65_latex_engine" -interaction=nonstopmode -halt-on-error -output-directory=../tmp/build e65-complete.tex
done
cp ../tmp/build/e65-complete.pdf "../output/pdf/Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes.pdf"
