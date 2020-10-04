#!/usr/bin/env bash

main() {
	[[ $1 -le 0 ]] && echo "invalid input" && exit 1
	PRIMES=("2" "3" "5" "7" "11" "13")
	[[ $1 -le 6 ]] && echo "${PRIMES[$1-1]}" && exit 0
	NUM=13
	INC=2
	LST_CNT=6
	while [[ $LST_CNT -lt $1 ]]
	do
		CNT=0
		NUM=$(($NUM+$INC))
		for (( NUMBER=2; NUMBER<NUM; NUMBER++))
		do
			[[ $((NUM%NUMBER)) -eq 0 ]] && ((CNT++))
		done
		[[ $CNT ==  0 ]] && ((LST_CNT++))
	done
	echo "$NUM"
}

main "$@"
