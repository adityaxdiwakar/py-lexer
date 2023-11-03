#!/bin/bash
for file in tests/*; do
    if [[ $file == *.c ]]; then
        echo "Testing $file against lexer"
        base=$(basename "$file")
        name="${base%.*}"
        cat $file | python3 lex.py > output

        diff output "tests/expected/$name.out" > output_diff
        status=$?
        if [ "$status" -eq 0 ]; then
            echo "OK."
        else
            echo "Failed. See diff below."
            cat output_diff
            rm output || true
            rm output_diff || true
            exit 1
        fi
    fi
done
rm output || true
rm output_diff || true
