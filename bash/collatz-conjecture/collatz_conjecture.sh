#!/usr/bin/env bash

main() {
	N=$1
	[[ $N -le 0 ]] 	&& { echo "Error: Only positive numbers are allowed" ; exit 1 ; }
	COUNT=0
	while [ $N -gt 1 ]
	do	
		if (( N % 2 == 0 ))
		then
			N=$(($N / 2 ))
		else
			N=$((3*$N+1))
		fi
		((COUNT++))
	done
	echo "$COUNT"
}

main "$@"
