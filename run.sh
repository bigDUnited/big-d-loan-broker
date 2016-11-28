#!/bin/bash
proc=()
python rulebase.py &
proc+=("$!")
python creditscore_enricher.py &
proc+=("$!")
python bank_enricher.py &
proc+=("$!")
python recipient.py &
proc+=("$!")
python client.py

sleep 2
echo "${proc[@]}"
kill ${proc[@]}
