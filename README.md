# Usage of jq.py
Note: there are only one argument in jq.py

- -r: reverse, unbeautify the JSON data; no matter where it is

## Examples
Note: **jq** is the alias of `python3 jq.py`

Beautify/Unbeautify the JSON file:
```shell
jq example.json
jq -r example.json
jq example.json -r
```

Beautify/Unbeautify the JSON data from pipeline:
```shell
cat example.json | jq
cat example.json | jq -r
```