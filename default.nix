{ stdenv, bundlerEnv, ruby, lib, pkgs, ... }:


let
  baseurl = "guip.dev";
  gems = bundlerEnv {
    name = "guip-dev-env";
    inherit ruby;
    gemdir = ./.;
  };
in
stdenv.mkDerivation {
  name = "guip.dev";
  src = ./.;

  buildInputs = [
    ruby
    gems
  ];


  buildPhase = ''
    ${gems}/bin/bundle exec jekyll build ${lib.optionalString (baseurl != null) "--baseurl ${baseurl}"}
  '';

  installPhase = ''
    mkdir -p $out
    cp -Tr _site $out/public
  '';

}
