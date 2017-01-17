#!/bin/bash
#Run the entire project.
p=$(ps aux | grep rulebase | head -n 1 | cut -f 4 -d' ')
kill -9 $p

proc=()

java -jar rulebase.jar &

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
python broker/normalizer.py &
proc+=("$!")
python broker/aggregator.py &
proc+=("$!")



python client.py &

sleep 5
echo "${proc[@]}"
p=$(ps aux | grep rulebase | head -n 1 | cut -f 4 -d' ')
kill -9 $p ${proc[@]}
