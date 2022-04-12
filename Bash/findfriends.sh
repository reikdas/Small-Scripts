#!/bin/bash

declare -A map
while read -ra line; do
    count=0
    key=0
    arr=()
    for word in "${line[@]}"; do
        if [ $count -eq 0 ]; then
            key=$word
        else
            arr+=($word)
        fi
        ((count=count+1))
    done
    map[$key]="${arr[*]}"
done

for key1 in "${!map[@]}"
do
    for key2 in "${!map[@]}"
    do
        if [[ "$key1" < "$key2" ]]; then
            echo -n "$key1, $key2 = "
            read -ra words1 <<< "${map[$key1]}"
            read -ra words2 <<< "${map[$key2]}"
            for i in "${words1[@]}"
            do
                for j in "${words2[@]}"
                do
                    if [[ "$i" == "$j" ]]; then
                        echo -n "$i "
                    fi
                done
            done
            echo " "
        fi
    done
done

