#!/bin/bash

# 定义一个函数，用来切片单个音频文件
slice_audio() {
    local input_file="$1"       # 输入文件
    local base_output_dir="$2"  # 输出根目录
    local hls_time="${3:-10}"   # 切片时长，默认10秒

    local filename=$(basename "$input_file")
    local name="${filename%.*}"  # 去掉扩展名

    # 为每个文件创建独立输出目录
    local output_dir="$base_output_dir/$name"
    mkdir -p "$output_dir"

    # 执行 FFmpeg 切片
    # ffmpeg -i "$input_file" -hls_time "$hls_time" -hls_playlist_type vod "$output_dir/playlist.m3u8"
    ffmpeg -y -i "$input_file" \
    -map 0:a:0 \
    -c:a copy \
    -f hls \
    -hls_time "$hls_time" \
    -hls_playlist_type vod \
    "$output_dir/playlist.m3u8"
}

# 主流程
base_output_dir="./resource"
mkdir -p "$base_output_dir"

slice_audio ./resource/1_1.mp3 base_output_dir 10

# for file in ${base_output_dir}/*.mp3; do
#   echo "Processing file: $file"
#     # slice_audio "$file" "$base_output_dir" 10
# done
