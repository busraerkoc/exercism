#!/usr/bin/env bash

second_part(){
	local NUM=("a Partridge in a Pear Tree." "two Turtle Doves" "three French Hens" "four Calling Birds" "five Gold Rings" "six Geese-a-Laying" "seven Swans-a-Swimming" "eight Maids-a-Milking" "nine Ladies Dancing" "ten Lords-a-Leaping" "eleven Pipers Piping" "twelve Drummers Drumming")
	local SECOND=""
	for ((i=$1; i > 1; i--))
	do
		SECOND+=${NUM[((i-1))]}", "
	done
	[[ $1 -gt 1 ]] && echo "${SECOND}"and "${NUM[0]}" || echo "${SECOND}${NUM[0]}"
}
first_part(){
	local NUMS=("first" "second" "third" "fourth" "fifth" "sixth" "seventh" "eighth" "ninth" "tenth" "eleventh" "twelfth")
	local ON="On the "
	local CH=" day of Christmas my true love gave to me: "
	echo "${ON}${NUMS[(($1-1))]}${CH}"
}

main() {
	for ((i=$1; i <=$2; i++))
	do
		FIRST=$( first_part $i )
		SECOND=$( second_part $i )
		echo "${FIRST}${SECOND}"
	done	
}

main "$@"
