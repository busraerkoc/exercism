#!/usr/bin/env bash
RESULT=""
main() {
	(($1%3)) || RESULT+="Pling"
	(($1%5)) || RESULT+="Plang"
	(($1%7)) || RESULT+="Plong"
	[[ -z "$RESULT" ]] && echo "$1" || echo "$RESULT"
}
main "$@"
