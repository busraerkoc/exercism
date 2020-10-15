#!/usr/bin/env bash

main() {
	RESULT=()
	for (( i=0; i<${#1}; i++ ))
	do
		case "${1:i:1}" in
			"G")
				RESULT+="C"
				;;
			"C")
				RESULT+="G"
				;;
			"T")
				RESULT+="A"
				;;
			"A")
				RESULT+="U"
				;;
			*)
				echo "Invalid nucleotide detected."
				exit 1
		esac
	done
	echo "$RESULT"
}

main "$@"
