#!/usr/bin/env bash

main() {
	if [ ${#} -gt 0 ]
	then
		for (( i=1; i<${#}; i++))
		do
			next=$((i+1))
			echo "For want of a ${!i} the ${!next} was lost."
		done
		echo "And all for the want of a ${1}."
	fi
}

main "$@"
