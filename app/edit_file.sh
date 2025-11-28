#!/bin/bash
i=1
group_id=1
file_path="./resource/*.mp3"

ls ${file_path} | sort -V | while read f; do
  ext="${f##*.}"
  path="${f%/*}"
  # echo mv "$f" "$path${group_id}_$i.$ext"
  mv "$f" "${path}/${group_id}_${i}.${ext}"
  ((i++))
done
