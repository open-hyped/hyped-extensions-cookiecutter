sphinx-apidoc -f -e -o source/api ../src/hyped/extensions/ --maxdepth 3
make clean
make html
