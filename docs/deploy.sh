#!/bin/bash
set -e

/opt/homebrew/opt/ruby@3.3/bin/bundle exec jekyll build -d docs

git add -A
git commit -m "${1:-update site}"
git push origin deploy:master
