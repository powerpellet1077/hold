# hold
simple cli tool that can temporarily 'hold' text. think of it as a clipboard for your terminal.
```
usage: hold [-k [KEY]] [-d [DATA]] [-r] [-h] [-n] [-?]

a cli tool for "holding" text or output temporarily. effectively a clipboard made only for terminals

options:
  -k, --key [KEY]    target key to take or store from [default = global]
  -d, --data [DATA]  data to hold
  -r, --retrieve     set mode to retrieve
  -h, --hold         set mode to hold
  -n, --newline      text returned would output a newline in addition
  -?, --help         provides help

```


### usage
to save data to the global key, you could do
```
hold -hd "hellow world :D"
```

retrieving it is just as easy
```
hold -nr
hellow world :D
```

this could be useful for saving text/tokens without using the clipboard directly

### compiling
#### linux:
```
pyinstaller --noconfirm --onefile --console --name "hold" --add-data "hold:hold"  "./main.py" 
```
#### windows:
```
pyinstaller --noconfirm --onefile --console --name "hold" --add-data "core;core"  "./main.py" 
```