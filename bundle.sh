#!/bin/bash

name="themer.zip"
main_file="themer.py"

mkdir themer
cp $main_file ./themer/__main__.py
cp $(ls *.py | grep -v $main_file) ./themer/
cd ./themer
zip ../$name $(ls *.py)
cd ..
chmod 777 $name

if [ ! -d "output" ]
then
	mkdir output
fi

mv themer.zip output
rm -r themer
