import os, random, string
from pathlib import Path


def rename_videos_to_gibberish(folder):
    video_exts = {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.ts'}

    # 收集所有视频文件
    videos = []
    for root, _, files in os.walk(folder):
        for f in files:
            if Path(f).suffix.lower() in video_exts:
                videos.append(Path(root) / f)

    if not videos:
        print("未找到视频文件")
        return

    print(f"找到 {len(videos)} 个视频文件")

    # 重命名
    renamed = 0
    for vid in videos:
        # 生成10位随机乱码
        gibberish = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        new_name = f"{gibberish}{vid.suffix}"
        new_path = vid.parent / new_name

        try:
            vid.rename(new_path)
            renamed += 1
            if renamed % 50 == 0:
                print(f"已重命名 {renamed}/{len(videos)} 个文件")
        except Exception as e:
            print(f"重命名失败 {vid.name}: {e}")

    print(f"完成！重命名 {renamed} 个视频文件")


# 运行
rename_videos_to_gibberish(r"I:\Adult\videos_mp4")