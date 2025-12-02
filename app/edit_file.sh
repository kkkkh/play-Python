!/bin/bash

# 重命名 lrc 文件
i=1
group_id=1
file_path="./test/*.mp3"

ls ${file_path} | sort -V | while read f; do
  ext="${f##*.}"
  path="${f%/*}"
  echo mv "$f" "$path/${group_id}_$i.$ext"
  # mv ./sources/englishpod_0001pb.lrc ./sources/1_1.lrc
  # mv "$f" "${path}/${group_id}_${i}.${ext}"
  ((i++))
done



