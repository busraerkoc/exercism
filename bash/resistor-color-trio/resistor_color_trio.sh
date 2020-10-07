#!/usr/bin/env bash

main() {
	declare -A COLORS=(["black"]=0 ["brown"]=1 ["red"]=2 ["orange"]=3 ["yellow"]=4 ["green"]=5 ["blue"]=6 ["violet"]=7 ["grey"]=8 ["white"]=9)
	RESULT=""
	for i in $1 $2
	do
		[[ -v "COLORS[$i]" ]] && RESULT+=${COLORS[$i]} || { echo "[[ -n $RESULT ]]" ; exit 1 ; }
	done
	if [[ -v "COLORS[$3]" ]] 
	then
		for ((i=0; i<${COLORS[$3]}; i++))
		do
			RESULT+=0
		done
		RESULT=$(echo $RESULT | sed 's/^0//')
		case 1 in
			$(( $(( RESULT/1000)) <= 1 )) )
			      	RESULT+=" ohms"
				;;
			$(( $(( RESULT/1000000 )) <= 1 )) )
				RESULT=$(( RESULT/1000 ))
				RESULT+=" kiloohms"
				;;
			$(( $(( RESULT/10000000000 )) <= 1 )) )
				RESULT=$(( RESULT/1000000 ))
				RESULT+=" megaohms"
				;;
			*)
				RESULT=$(( RESULT/1000000000 ))
				RESULT+=" gigaohms"
				;;
		esac
	else
		echo "[[ -n $RESULT ]]" && exit 1
	fi
	echo "$RESULT"
}

main "$@"
