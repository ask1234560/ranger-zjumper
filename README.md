# Ranger & z

This plugin integrates [Z](https://github.com/rupa/z/) with ranger. The plugin uses .z file to jump around, watch [screencast](https://youtu.be/ciHHbFtz4N8).

## Installation

* Copy zjumper_ranger.py to ${XDG_CONFIG_HOME}/ranger/plugins aka ~/.config/ranger/plugins.
* Add  __`map cz console z%space`__ in .config/ranger/rc.conf


## Usage

* type `:z dirname` to go to dirname or `:z dirname1 dirname2` to go to dirname1/*/dirname2.
* press c followed by z, followed by `dirname` or `dirname1 dirname2`.
* dirname should be lowercase only.

## Configuration

This plugin uses .z file in home directory, if .z in different location change  `cmd = """awk -F "|" -v q=\""""+" ".join(self.args[1:])+"""\" 'BEGIN{gsub(/ /, ".*", q)}  { if(tolower($1) ~ q){ print $1} }'  ~/.z"""` accordingly. 

