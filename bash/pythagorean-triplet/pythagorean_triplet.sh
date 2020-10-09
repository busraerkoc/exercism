#!/usr/bin/env bash

main() {
	for ((a=1; a<$(($1/2)); a++))
	do
		for (( b=$a+1; b<$(($1/2)); b++ ))
		do
			(( c = $1-$a-$b ))
			(( $a*$a + $b*$b == $c*$c )) && echo "$a,$b,$c"
		done
	done
}

main "$@"
