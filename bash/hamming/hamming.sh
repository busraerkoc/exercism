#!/usr/bin/env bash

main() {
	HAMMING=0
	(( $# != 2 )) && { echo "Usage: hamming.sh <string1> <string2>" ; exit 1 ; }
	
	if (( ${#1} != ${#2} ))
	then
		echo "left and right strands must be of equal length"
		exit 1
	fi

	for (( i=0; i<${#1}; i++ ))
	do
		if [[ "${1:$i:1}" != "${2:i:1}" ]]
		then
			((HAMMING++))
		fi
	done
	echo "$HAMMING"
}

main "$@"
