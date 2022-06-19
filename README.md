# sshmanager

sshmanager is a Python application to manage SSH bookmarks. The list of ssh hosts is deserialized into a json file using the JsonPickle library.

## Requirements

* Python 3
* ssh client application

## Running the application

Execute `python sshmanager/main.py`

### Example application run

``` text
$ python sshmanager/main.py 
                SSH Hosts                
┏━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Id ┃ Host   ┃ Group ┃ Full Host Name  ┃
┡━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│  1 │ python │ dev   │ python.acme.com │
│  2 │ java   │ dev   │ java.acme.com   │
└────┴────────┴───────┴─────────────────┘
Select a host id [1/2]:
```

## Libraries used

* Rich
* JsonPickle

## TODO

* Add ability to save / edit hosts via UI
* Full tests
* Ability to specify ssh username
* Full documentation
* Setup scripts so can install via pip
* Bash script to run application
* Save hosts file into ~/.config directory structure
* 