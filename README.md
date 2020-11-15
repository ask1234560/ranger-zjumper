# Ranger & z
This plugin integrates [Z](https://github.com/rupa/z) with [ranger](https://github.com/ranger/ranger). The plugin uses `.z` file to jump around, watch [screencast](https://youtu.be/ciHHbFtz4N8).

## Installation
```
* git clone https://github.com/ask1234560/ranger-zjumper.git
* cd ranger-zjumper
* cp zjumper_ranger.py "${XDG_CONFIG_HOME:-$HOME/.config}"/ranger/plugins
* echo "map cz console z%space" >> "${XDG_CONFIG_HOME:-$HOME/.config}"/ranger/rc.conf
```

## Usage
* type `:z dir` to go to `.*dir` or `:z dir1 dir2 ... dirn` to go to `.*dir1.*dir2....*dirn`
* press c followed by z, followed by `dir` or `dir1 dir2 ... dirn`
* dir is not case sensitive

## Configuration
This plugin uses `.z` file which is in `$HOME`, if .z is not in `$HOME` then change `z_loc = getenv("HOME")+"/.z"` in `zjumper_ranger.py`.
