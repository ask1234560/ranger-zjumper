# Ranger & z

This plugin integrates [Z](https://github.com/rupa/z/) with [ranger](https://github.com/ranger/ranger). The plugin uses `.z` file to jump around, watch [screencast](https://youtu.be/ciHHbFtz4N8).

## Installation

* Copy `zjumper_ranger.py` to `${XDG_CONFIG_HOME}/ranger/plugins` aka `~/.config/ranger/plugins`.
* Add  __`map cz console z%space`__ in .config/ranger/rc.conf


## Usage

* type `:z dirname` to go to `.*dirname` or `:z dirname1/dirname2` to go to `.*dirname1/dirname2`
* press c followed by z, followed by `dirname` or `dirname1/dirname2`
* dirname is case sensitive

## Configuration

This plugin uses `.z` file, if `.z` in different location other than `~/.config/.z` change `z_loc = getenv("HOME")+"/.config/.z"` in zjumper_ranger.py. 

