#!/usr/bin/env bash
square_of_sum() {
	echo "$(( ($1*($1 + 1) / 2)**2 ))"
}

sum_of_squares() {
	echo "$(( $1 * ($1 + 1) * (2 * $1 + 1) / 6 ))"
}

difference() {
	echo $(( $(square_of_sum "$1") - $(sum_of_squares "$1") ))
}

main() {
	$1 "$2"
}

main "$@"

