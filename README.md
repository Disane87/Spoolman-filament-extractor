
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


---

## 🔗 Related Spoolman Projects

Check out these other projects from the Spoolman ecosystem:

| Project | Description |
|---------|-------------|
| [🧵 Spoolman MCP](https://github.com/Disane87/spoolman-mcp) | MCP Server for Spoolman — manage your filament inventory through AI assistants like Claude. Available on [npm](https://www.npmjs.com/package/@disane-dev/spoolman-mcp). |
| [🏠 Spoolman Home Assistant](https://github.com/Disane87/spoolman-homeassistant) | Integrate Spoolman with Home Assistant — track spools, get notifications, automate your printing workflow |
| [🎨 Spoolman Filament Swatch](https://github.com/Disane87/spoolman-filament-swatch) | Beautiful, interactive filament color browser for Spoolman. [Live Demo](https://spoolswatch.disane.dev/) |
| [🗄️ SpoolmanDB](https://github.com/Donkie/SpoolmanDB) | Centralized community filament database used by Spoolman |
| [🖨️ Spoolman](https://github.com/Donkie/Spoolman/) | The awesome filament manager that powers everything |
