#!/usr/bin/env bash

main() {
	RESULT=0
	for (( i=0; i<${#1}; i++ ))
	do
		(( RESULT+=$(( ${1:i:1} ** ${#1} )) ))
	done
	[[ $RESULT == $1 ]]  && echo "true" || echo "false"
}

main "$@"
