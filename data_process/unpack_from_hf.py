"""
解压从HuggingFace下载的数据集

使用方法:
    # 假设从HF下载数据到 /path/to/download/
    # 目录结构应该是:
    #   /path/to/download/Generation/image/train/rh20t/contact_box.zip
    #   /path/to/download/Generation/meta/train/rh20t/smart_resize_format/*.json

    python unpack_from_hf.py --data_root /path/to/download --data_type all

解压后:
    /path/to/download/Generation/image/train/rh20t/contact_box/xxx.jpg

    JSON中的路径 "Generation/image/train/rh20t/contact_box/xxx.jpg"
    相对于 data_root 可以正确访问图片
"""

import os
import subprocess
import argparse
from glob import glob
from tqdm import tqdm
from multiprocessing import Pool


def unpack_single_zip(args):
    """解压单个zip文件"""
    zip_path, extract_dir = args

    try:
        # 解压到指定目录
        # -o 覆盖已存在文件, -q 安静模式
        cmd = f'unzip -oq "{zip_path}" -d "{extract_dir}"'
        subprocess.run(cmd, shell=True, check=True)

        return (zip_path, True, None)
    except Exception as e:
        return (zip_path, False, str(e))


def get_all_zip_files(data_type="Generation"):
    """获取所有zip文件"""
    image_root = os.path.join(DATA_ROOT, data_type, "image")
    zip_files = glob(os.path.join(image_root, "**/*.zip"), recursive=True)
    return zip_files


def main():
    parser = argparse.ArgumentParser(description="Unpack zip files from HuggingFace download")
    parser.add_argument("--data_type", type=str, default="Generation",
                        choices=["Generation", "Understanding", "all"],
                        help="Which data type to unpack")
    parser.add_argument("--num_workers", type=int, default=8, help="Number of parallel workers")
    parser.add_argument("--dry_run", action="store_true", help="Only show what would be done")
    parser.add_argument("--data_root", type=str, default=DATA_ROOT,
                        help="Root directory of the data")
    args = parser.parse_args()

    global DATA_ROOT
    DATA_ROOT = args.data_root

    data_types = ["Generation", "Understanding"] if args.data_type == "all" else [args.data_type]

    for data_type in data_types:
        print(f"\n{'=' * 60}")
        print(f"Processing {data_type}...")
        print(f"{'=' * 60}")

        # 获取所有zip文件
        zip_files = get_all_zip_files(data_type)

        if not zip_files:
            print(f"No zip files found for {data_type}")
            continue

        print(f"Found {len(zip_files)} zip files:")
        for z in zip_files:
            print(f"  - {z}")

        if args.dry_run:
            print("\n[Dry run] Would unpack the above files")
            continue

        # 准备解压任务
        # zip文件解压到其所在目录
        unpack_tasks = []
        for zip_path in zip_files:
            extract_dir = os.path.dirname(zip_path)
            unpack_tasks.append((zip_path, extract_dir))

        # 多进程解压
        print(f"\nUnpacking {len(unpack_tasks)} zip files...")
        results = []
        with Pool(processes=args.num_workers) as pool:
            for result in tqdm(pool.imap_unordered(unpack_single_zip, unpack_tasks),
                               total=len(unpack_tasks), desc="Unpacking"):
                results.append(result)

        # 打印结果
        print(f"\n{'=' * 60}")
        print("Unpack results:")
        print(f"{'=' * 60}")
        success_count = 0
        for zip_path, success, error in sorted(results):
            status = "OK" if success else f"FAILED: {error}"
            print(f"  [{status}] {os.path.basename(zip_path)}")
            if success:
                success_count += 1

        print(f"\nSuccessfully unpacked: {success_count}/{len(results)}")

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
