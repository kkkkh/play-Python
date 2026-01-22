import subprocess
from pathlib import Path


def batch_sclice_audio(*params,dir_path: str = "./app/resource", group_id: int = 1):
  root = Path(dir_path)
  root.mkdir(exist_ok=True)
  (start,end) = params
  for id in range(start, end + 1):
    dir_path_each = root / f'{group_id}_{id}'
    dir_path_each.mkdir(exist_ok=True)

    m3u8_path = dir_path_each / "playlist.m3u8"
    segment_pattern = dir_path_each / "%03d.ts"

    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(dir_path_each.with_suffix('.mp3')),
        "-map", "0:a:0",
        "-c:a", "aac",
        "-f", "hls",
        "-hls_time", "10",
        "-hls_playlist_type", "vod",
        "-hls_segment_filename", str(segment_pattern),
        str(m3u8_path)
    ], check=True)


def sclice_audio(dir_path: str = "./app/resource"):
  root = Path(dir_path)
  root.mkdir(exist_ok=True)
  for mp3 in root.glob("*.mp3"):
      name = mp3.stem
      print(name)
      out_dir = root / name
      out_dir.mkdir(exist_ok=True)

      m3u8_path = out_dir / "playlist.m3u8"
      segment_pattern = out_dir / "%03d.ts"

      subprocess.run([
          "ffmpeg", "-y",
          "-i", str(mp3),
          "-map", "0:a:0",
          "-c:a", "aac",
          "-f", "hls",
          "-hls_time", "10",
          "-hls_playlist_type", "vod",
          "-hls_segment_filename", str(segment_pattern),
          str(m3u8_path)
      ], check=True)
