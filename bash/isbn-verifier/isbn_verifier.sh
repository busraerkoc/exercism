#!/usr/bin/env bash

main() {
	NUMBER=${1//[![:digit:]X]/} X=10
	[[ ${#NUMBER} -ne 10 ]] && echo "false" && exit 0
	RESULT=0
	for ((NUM=0; NUM<${#NUMBER}; NUM++))
	do
		[[ ${NUMBER:NUM:1} == 'X' ]] && [[ $NUM -ne 9 ]] && echo "false" && exit 0
		((RESULT+=${NUMBER:NUM:1} * ( 10 - NUM ) ))
	done
	[[ $(( RESULT % 11 )) -eq O ]] && echo "true" && exit 0
	echo "false" && exit 0
}

main "$@"
