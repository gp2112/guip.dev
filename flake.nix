{
  description = "Personal website guip.dev";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.05";
    utils.url = "github:numtide/flake-utils";
  };


  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
  let pkgs = nixpkgs.legacyPackages.${system};
  in rec {
    packages = rec {
      guip-dev = pkgs.callPackage ./default.nix { };
      guip-dev-serve = pkgs.writeShellScriptBin "serve" ''
        echo "Serving on http://localhost:8000"
        ${pkgs.webfs}/bin/webfsd -F -f index.html -r ${guip-dev}/public
      '';
      default = guip-dev;
    };

    apps = rec {
      site = {
        type = "app";
        program = "${packages.guip-dev-serve}/bin/serve";
      };
      default = site;
    };
  }) // {
  };
}
