
# Spoolman-filament-extractor 🎉

Python script to extract your filaments and bring them into a [SpoolmanDB](https://github.com/Donkie/SpoolmanDB) format to participate in creating an comprehensive and centralized filament database. This database is used in [Spoolman](https://github.com/Donkie/Spoolman) by [Donkie](https://github.com/Donkie).

## Installation

Just clone the repo and install deps

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

Create an `.env` file according to the `.env.example` and add your spoolman url.

`API_URL`

## Usage/Examples

Just simply execute the script

```bash
py main.py
```

The script will create a `output_filaments` folder which contains JSON files. One JSON file per manufacturer according to the JSON schemas of SpoolmanDB.

