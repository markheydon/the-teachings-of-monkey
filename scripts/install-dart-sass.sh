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
sudo install -m 0755 "$TMP_DIR/dart-sass/sass" /usr/local/bin/sass

sass --version
