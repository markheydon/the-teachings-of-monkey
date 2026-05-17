#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-1.93.3}"

TMP_TGZ="$(mktemp -t dart_sass_XXXXXX.tar.gz)"
TMP_DIR="$(mktemp -d -t dart_sass_dir_XXXXXX)"
trap 'rm -f "$TMP_TGZ"; rm -rf "$TMP_DIR"' EXIT

URL="https://github.com/sass/dart-sass/releases/download/${VERSION}/dart-sass-${VERSION}-linux-x64.tar.gz"
echo "Installing Dart Sass ${VERSION} from ${URL}"

wget -q -O "$TMP_TGZ" "$URL"
tar -xzf "$TMP_TGZ" -C "$TMP_DIR"

# The `sass` launcher expects sibling files in `src/`, so install the whole
# extracted directory and link the launcher into PATH.
sudo rm -rf /usr/local/lib/dart-sass
sudo mkdir -p /usr/local/lib
sudo cp -R "$TMP_DIR/dart-sass" /usr/local/lib/dart-sass
sudo chmod -R a+rX /usr/local/lib/dart-sass
sudo ln -sf /usr/local/lib/dart-sass/sass /usr/local/bin/sass

sass --version
