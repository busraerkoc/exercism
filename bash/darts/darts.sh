#!/usr/bin/env bash

main() {
	[[ $# -lt 2 ]] || [[ ! $1 =~ ^-?[.0-9]+$ ]] || [[ ! $2 =~ ^-?[.0-9]+$ ]] && { echo "invalid input" ; exit 1 ; }
	VAR=$(bc <<< $1^2+$2^2)
	RADIUS=$(bc  <<< "sqrt($VAR)")
	if (($(bc -l <<< "$RADIUS > 10" )))
	then
		echo "0"
	elif (($(bc -l <<< "$RADIUS > 5" )))
	then
		echo "1"
	elif (($(bc -l <<< "$RADIUS > 1" )))
	then
		echo "5"
	elif (($(bc -l <<< "$RADIUS >= 0" )))
	then
		echo "10"
	else
		exit 1
	fi
}

main "$@"
