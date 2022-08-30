# Download Dataset script

* Create a virtual env: `python3 -m venv $HOME/venvs/notebooks`
* Activate it: `source $HOME/venvs/notebooks/bin/activate`
* Make sure you export the `MOONSENSE_SECRET_TOKEN` env variable: `export MOONSENSE_SECRET_TOKEN=<get this from the
  console>`
* Run: `python3 download.py --since 2022-08-03 --until 2022-08-06 --filter_by inputs/filtered_list.csv`

# Run modeling script

```
python3 prepare-data.py
```
