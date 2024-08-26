#!/bin/bash

MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE=""

if [[ $1 == "new" ]]; then
    python3 "${MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE}/.csv_sheets/main.py" $1 $2;

elif [[ $1 == "sheet" ]]; then
    python3 "${MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE}/.csv_sheets/main.py" $1 $2;

else
    echo 'I said "new" or "sheet"!!, bye'
fi
