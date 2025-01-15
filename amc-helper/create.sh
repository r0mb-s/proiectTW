#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <path> <question_file>"
  exit 1
fi

TARGET_PATH=$(realpath "$1")
if [ -e "$TARGET_PATH" ]; then
  echo "Error: The path '$TARGET_PATH' already exists."
  exit 2
fi

if [ ! -f "$2" ]; then
    echo "Error: The parameter '$2' is not a file."
    exit 3
fi

mkdir -p "$TARGET_PATH" 2>/dev/null

QUESTIONS_FILE=$(realpath "$2")

if [ $? -eq 0 ]; then
  echo "Folder created successfully at '$TARGET_PATH'."
else
  echo "Error: Could not create the folder at '$TARGET_PATH'."
  exit 4
fi

mkdir "$TARGET_PATH"/cr
mkdir "$TARGET_PATH"/cr/corrections
mkdir "$TARGET_PATH"/cr/corrections/jpg
mkdir "$TARGET_PATH"/cr/corrections/pdf
mkdir "$TARGET_PATH"/cr/diagnostic
mkdir "$TARGET_PATH"/cr/zooms
mkdir "$TARGET_PATH"/data
mkdir "$TARGET_PATH"/exports
mkdir "$TARGET_PATH"/scans
mkdir "$TARGET_PATH"/copies

COMMAND="auto-multiple-choice prepare \
    --mode s \
    --prefix "$TARGET_PATH" \
    $QUESTIONS_FILE \
    --out-sujet "$TARGET_PATH"/DOC-subject.pdf \
    --out-corrige "$TARGET_PATH"/DOC-correction.pdf \
    --data "$TARGET_PATH"/data \
    --out-calage "$TARGET_PATH"/DOC-calage.xy \
    --filter plain"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice prepare(s) successful."
else
    echo "Command auto-multiple-choice prepare(s) unsuccessful."
    echo "$OUTPUT"
    rm -rf "$TARGET_PATH"
    exit 6
fi

COMMAND="auto-multiple-choice prepare \
    --mode b \
    --prefix "$TARGET_PATH" \
    $QUESTIONS_FILE \
    --data "$TARGET_PATH"/data \
    --filter plain"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice prepare(b) successful."
else
    echo "Command auto-multiple-choice prepare(b) unsuccessful."
    echo "$OUTPUT"
    rm -rf "$TARGET_PATH"
    exit 6
fi

COMMAND="auto-multiple-choice meptex \
    --src "$TARGET_PATH"/DOC-calage.xy \
    --data "$TARGET_PATH"/data"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice meptex successful."
else
    echo "Command auto-multiple-choice meptex unsuccessful."
    echo "$OUTPUT"
    rm -rf "$TARGET_PATH"
    exit 6
fi
