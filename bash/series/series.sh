#!/usr/bin/env bash

main() {
	[[ ${2} -eq 0 ]] && { echo "slice length cannot be zero" ; exit 1 ; }
	[[ ${2} -lt 0 ]] && { echo "slice length cannot be negative" ; exit 1 ; }
	[[ ${#1} -eq 0 ]] && { echo "series cannot be empty" ; exit 1 ; }
	[[ ${2} -gt ${#1} ]] && { echo "slice length cannot be greater than series length" ; exit 1 ; }
	RESULT=()
	for ((i=0; i<$(( ${#1} - $2 + 1 )); i++))
	do
		RESULT+=(${1:i:$2})
	done
	echo "${RESULT[@]}"
}

main "$@"
