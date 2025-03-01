with (import <nixpkgs> {  });
mkShell {
  packages = [
    (python3.withPackages (python-pkgs: [
      python-pkgs.evdev
    ]))
    (vscode-with-extensions.override {
        vscodeExtensions = with vscode-extensions; [
            ms-vscode.hexeditor
            tal7aouy.icons
            jnoortheen.nix-ide
            wmaurer.change-case
            ms-python.python
      ];
    })
  ];
}
