#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

# ---------------- 配置参数 ----------------
# DB_PATH = "/var/lib/docker/volumes/hometown_db_data/_data/sqlite.db"    # SQLite 数据库文件路径
DB_PATH = "D:/WorkSpace/4NOTE/hometown/data/db/sqlite.db"    # SQLite 数据库文件路径
# ------------------------------------------

def batch_add_data_resources(*params,group_id=1):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    (start,end) = params
    # Step 1：生成占位数据（seq、name、时间）
    rows = []
    for i in range(start, end + 1):
        seq =  i
        name = i
        lrc_url = f"/resource/{group_id}_{i}.lrc"
        audio_url = f"/resource/audio/{group_id}_{i}/playlist.m3u8"
        desc = f"{group_id}_{i}"
        rows.append((group_id, seq, name, lrc_url, audio_url, now, now, desc))
    cur.executemany("""
        INSERT INTO resources (group_id, seq, name, lrcUrl, audioUrl, created_at, updated_at, desc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)
    conn.commit()
    conn.close()

    print(f"成功生成 {end - start + 1} 条资源数据，group_id={group_id}。")

