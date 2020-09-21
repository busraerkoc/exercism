#!/usr/bin/env bash

main() {
	[[ $1 -le 0 ]] && { echo "Classification is only possible for natural numbers." ; exit 1 ; }
	N=$(($1/2))
	RESULT=0
	while [[ $N -gt 0 ]]
	do
		if [[ $(($1%N)) -eq 0 ]]	
		then
			((RESULT+=$N))
		fi
		((N--))
	done
	[[ $RESULT -eq $1 ]] && { echo "perfect" ; exit 0 ; }
	[[ $RESULT -gt $1 ]] && { echo "abundant" ; exit 0 ; }
	[[ $RESULT -lt $1 ]] && { echo "deficient" ; exit 0 ; }
}

main "$@"
