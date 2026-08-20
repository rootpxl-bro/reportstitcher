# ReportStitcher

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Build](https://img.shields.io/badge/build-passing-brightgreen.svg) ![PRs](https://img.shields.io/badge/PRs-welcome-orange.svg) ![Maintained](https://img.shields.io/badge/maintained-yes-cyan.svg) ![Platform](https://img.shields.io/badge/platform-cross-platform-purple.svg)

Combines daily report fragments from many folders into one dated document.

## About

Combines daily report fragments from many folders into one dated document.

## Features

- Reader / processor / writer pipeline
- Supports JSON, CSV and plain text input
- Streaming-friendly, memory-safe for large files
- Easy to add custom transforms

## Install

```bash
git clone https://github.com/rootpxl-bro/reportstitcher.git
cd reportstitcher
```

## Usage

```bash
python main.py sample.json out.json

python main.py sample.json out.csv
```

## License

MIT. See [LICENSE](LICENSE) for details.

## Support

Found a bug or have an idea? Open an issue. Pull requests are always welcome.