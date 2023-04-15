# Dorky
Google Dorking from the command line

![](https://github.com/arlidge/Dorky/blob/main/dork.png)

# Dorky

## Features

- Written in uncomplicated Go (Golang)
- No installation necessary - just use the [binary](https://github.com/karan/joe#installation).
- Stupidly [easy to use](https://github.com/karan/joe#usage)
- Supports all Github-supported [`.gitignore` files](https://github.com/karan/joe#list-all-available-files)
- Works on Mac, Linux and (maybe) Windows
- Supports other version control systems (`.hgignore`)

## Installation

After install, make sure to run `joe u`. This will download all `.gitignore` files in `~/joe-data/` folder.

### Option 1: Binary

`joe` is available for OSX (macOS), Linux and Windows.

Download the latest binary from the [Releases page](https://github.com/karan/joe/releases). It's the easiest way to get started with `joe`.

Make sure to add the location of the binary to your `$PATH`.

### Option 2: From source

```bash
$ git clone git@github.com:karan/joe.git
$ cd joe/
$ chmod +x tool.sh
$ ./tool.sh build
```
