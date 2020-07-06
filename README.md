# X10D (_extend_) your CMD! ![For any OS where command shell exists](https://img.shields.io/badge/Windows-unX10Ded-brightgreen.svg)

Well, just a set of some commands to extend the functionality of your command shell.

## Installing

Just add the directory with the [`xtd.exe`](xtd.exe) to the PATH. In future I plan to make the `setup.exe` which will do this automatically.

## Usage

```
$ xtd [OPTIONS] COMMAND [ARGS]...

  ===== X10D (extend) your CMD! =====

Options:
  --help  Show this message and exit.

Commands:
  binv  Invert FILE(S) bitwisely.
  now   What's time?
```

### Commands

- `binv <file [file [...]]>` inverts bitwisely a single file or several ones separated with spaces. For example, `00ff 775a` becomes `ff00 88a5`.
- `now` outputs the full datetime at the moment, _e.g._ `Right now: 2020-07-06 16:45:22.588288`.