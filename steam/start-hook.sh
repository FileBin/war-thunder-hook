#!/usr/bin/env bash
LD_PRELOAD=""
rm background.pid
cd /home/filebin/projects/war-thunder-hook/
env -i NIX_PATH="$NIX_PATH" XAUTHORITY="$XAUTHORITY" PATH="$PATH" HOME="$HOME" USER="$USER" DISPLAY="$DISPLAY" bash -l -c './run-nix.sh' &
cd -
jobs -p | head -n 1 | tee background.pid
