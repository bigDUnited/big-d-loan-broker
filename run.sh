#!/bin/bash
#Run the entire project.
p=$(ps aux | grep rulebase | head -n 1 | cut -f 4 -d' ')
kill -9 $p
proc=()
python broker/rulebase.py &
ps aux | grep rulebase | head -n 1
proc+=("$!")
python broker/creditscore_enricher.py &
proc+=("$!")
python broker/bank_enricher.py &
proc+=("$!")
python broker/recipient.py &
proc+=("$!")
python broker/danskebank_translator.py &
proc+=("$!")
python broker/nordea_translator.py &
proc+=("$!")
python broker/nytkredit_translator.py &
proc+=("$!")
python broker/bdo_translator.py &
proc+=("$!")
python dummylisten.py &
proc+=("$!")


python client.py

sleep 2
echo "${proc[@]}"
p=$(ps aux | grep rulebase | head -n 1 | cut -f 4 -d' ')
kill -9 $p ${proc[@]}
