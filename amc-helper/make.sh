#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <image path> <amc project dir>"
  exit 1
fi

TARGET_PATH=$(realpath "$1")
PROJECT_PATH=$(realpath "$2")

if [ ! -f "$TARGET_PATH" ]; then
    echo "Error: The parameter '$TARGET_PATH' is not a file."
    exit 2
fi
if [ ! -d "$PROJECT_PATH" ]; then
    echo "Error: The parameter '$PROJECT_PATH' is not a directory."
    exit 3
fi

COMMAND="auto-multiple-choice analyse \
    --projet $PROJECT_PATH \
    $TARGET_PATH"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice analyse successful."
else
    echo "Command auto-multiple-choice analyse unsuccessful."
    echo "$OUTPUT"
    exit 4
fi

COMMAND="auto-multiple-choice note \
    --data $PROJECT_PATH/data \
    --seuil 0.15 \
    --note-max 10"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice note successful."
else
    echo "Command auto-multiple-choice note unsuccessful."
    echo "$OUTPUT"
    exit 5
fi

COMMAND="auto-multiple-choice export \
    --data $PROJECT_PATH/data \
    --o $PROJECT_PATH/grades.csv"

OUTPUT=$(eval "$COMMAND" 2>&1)

if [ $? -eq 0 ]; then
    echo "Command auto-multiple-choice export successful ($PROJECT_PATH/grades.csv)."
else
    echo "Command auto-multiple-choice export unsuccessful."
    echo "$OUTPUT"
    exit 6
fi
