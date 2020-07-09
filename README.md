# X10D (_extend_) your CMD! ![For any OS where command shell exists](https://img.shields.io/badge/Windows-unX10Ded-brightgreen.svg)

Well, just a set of some commands to extend the functionality of your command shell.

## Installing

Download this repository and run the `setup.exe`. Then you can delete all files except `xtd.exe`.

## Usage

```
$ xtd [OPTIONS] COMMAND [ARGS]...

  ===== X10D (extend) your CMD! =====

Options:
  --help  Show this message and exit.

Commands:
  binv  Invert FILE(S) bitwisely.
  hfm   Compress or decompress FILE(S) using Huffman compression.
  now   What's time?
```

### Commands

- `binv <file [file [...]]>` inverts bitwisely a single file or several ones given separated with spaces. For example, `00ff 775a` becomes `ff00 88a5`.
- `hfm [-c / -d] <file [file [...]]>` compresses (if -c) or decompresses (if -d) a single file or several ones given separated with spaces using the [Huffman compression](https://en.wikipedia.org/wiki/Huffman_coding "Read about it on Wikipedia").
- `now` outputs the full datetime at the moment, _e.g._ `2020-07-06 23:08:26`.