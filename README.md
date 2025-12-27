# hold
simple cli tool that can temporarily 'hold' text. think of it as a clipboard for your terminal.
```
usage: hold [-k [KEY]] [-d [DATA]] [-r] [-h] [-n] [-l] [-c] [-?]

a cli tool for "holding" text or output temporarily. effectively a clipboard made only for terminals

options:
  -k, --key [KEY]    target key to take or store from [default = global]
  -d, --data [DATA]  data to hold
  -r, --retrieve     set mode to retrieve
  -h, --hold         set mode to hold
  -n, --newline      text returned would include a newline appended to the end of the output
  -l, --list         list all saved elements
  -c, --clear        clears set key
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

saving to a specific key is more like
```
hold -hk key_goes_here -d "really important stuff i refuse to copy to the clipboard"
hold -nrk key_goes_here
really important stuff i refuse to copy to the clipboard
```

this data will save between sessions on a file in your computer. this is not encrypted! please be careful with the data you save!

if you wish to delete some data that is saved, you can use the `-c` argument
```
hold -ck key_goes_here
```

listing all data in the hold can be done with just a simple command as well
```
hold -l
```
output:
```
bar = foo
baz = foo
```

### dependencies
this program requires __loguru__, __python 3.13__ and __pyinstaller__, which can be installed by the following
#### arch:
```
pacman -S python python-loguru python-pyinstaller
```
#### eos:
```
yay -S python python-loguru python-pyinstaller
```
#### other distros / windows (with full pip support)
```
pip install -r requirements.txt
```
or 
```
pip install loguru pyinstaller
```
for other systems that __do not__ have pip support, please consult the community for installing python packages

### compiling
#### linux:
```
pyinstaller --noconfirm --onefile --console --name "hold" --add-data "hold:hold"  "./main.py" 
```
#### windows:
```
pyinstaller --noconfirm --onefile --console --name "hold" --add-data "core;core"  "./main.py" 
```