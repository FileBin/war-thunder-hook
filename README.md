## War thunder mouse hook

### Motivation

War thunder has an open issue for linux client with porblem that mouse can randomly flip 90 degree and you will crash, and be knock out for 7 minutes. Annoying? Yeah, so thats why this python script exist.

### Installation

#### NixOs

just do 

```bash
nix-shell
chmod 777 hook.py
./hook.py
```

#### Steam additional steps (Currently only for Nix, needs improvement)

copy files from `./steam` directory into war thunder folder

replace `cd /home/filebin/projects/war-thunder-hook/` in start-hook.sh and stop-hook.sh with your __hook__ folder

replace launch parameters with contents of `./command.txt` directory into war thunder folder

#### Other distros

will require `evdev` library installed in system and python bindings for it, or just install it from Pipfile

```bash
pipenv install
pipenv shell
python3 hook.py
```



## Usage

After script is started you need to launch game and rebind controls to virtual gamepad. Also is better to plug out any additional gamepads and disable steam input because war thunder can't save input config because of index overlap.

Controls:

* `\` enable/disable mouse button wrap into virtual gamepad

* `ctrl` slow down mouse wheel axis scroll speed
