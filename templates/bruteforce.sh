#!/bin/bash

a=-1234567

while [ $a -lt 99999999 ]; do
	echo "$a" | ./keygenme
	a=$(expr $a + 1)
	echo $a
done
