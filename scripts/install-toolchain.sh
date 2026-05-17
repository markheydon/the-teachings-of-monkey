#!/usr/bin/env bash
set -euo pipefail

HUGO_VERSION="${HUGO_VERSION:-0.152.2}"
DART_SASS_VERSION="${DART_SASS_VERSION:-1.93.3}"
INSTALL_ROOT="${INSTALL_ROOT:-${HOME}/.local}"

mkdir -p "${INSTALL_ROOT}"

install_dart_sass() {
  local archive="dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
  local url="https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/${archive}"

  echo "Installing Dart Sass ${DART_SASS_VERSION} from ${url}"
  curl -sLJO "${url}"
  rm -rf "${INSTALL_ROOT}/dart-sass"
  tar -C "${INSTALL_ROOT}" -xf "${archive}"
  rm -f "${archive}"
}

install_hugo() {
  local archive="hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
  local url="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${archive}"

  echo "Installing Hugo ${HUGO_VERSION} from ${url}"
  curl -sLJO "${url}"
  rm -rf "${INSTALL_ROOT}/hugo"
  mkdir -p "${INSTALL_ROOT}/hugo"
  tar -C "${INSTALL_ROOT}/hugo" -xf "${archive}"
  rm -f "${archive}"
}

install_dart_sass
install_hugo

if [[ -n "${GITHUB_PATH:-}" ]]; then
  echo "${INSTALL_ROOT}/dart-sass" >> "${GITHUB_PATH}"
  echo "${INSTALL_ROOT}/hugo" >> "${GITHUB_PATH}"
else
  export PATH="${INSTALL_ROOT}/dart-sass:${INSTALL_ROOT}/hugo:${PATH}"
fi

echo "Dart Sass: $("${INSTALL_ROOT}/dart-sass/sass" --version)"
echo "Hugo: $("${INSTALL_ROOT}/hugo/hugo" version)"
