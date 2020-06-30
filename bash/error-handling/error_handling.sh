#!/usr/bin/env bash

if (( $# == 1 ));
then
	echo "Hello, ${1}"
	exit 0
else
	echo "Usage: error_handling.sh <person>"
	exit 1
fi
