#!/usr/bin/env bash

main() {
	for i in "$@"
	do 
		echo "$i" | rev
	done
}

main "$@"
