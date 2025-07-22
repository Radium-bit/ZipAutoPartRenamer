## Copyright (c) 2025 Radium-bit
## SPDX-License-Identifier: MIT
## See LICENSE file for full terms

import os
import re

def find_part_format_files():
    """
    查找是否存在 PartX 命名的文件
    """
    pattern = re.compile(r'^(.*?)-Part(\d+)\.(7z|rar|zip)$')
    for filename in os.listdir('.'):
        if pattern.match(filename):
            return True
    return False

def rename_to_split_format():
    """
    将 xxx-Part1.7z → xxx.7z.001 等格式
    """
    pattern = re.compile(r'^(.*?)-Part(\d+)\.(7z|rar|zip)$')
    for filename in os.listdir('.'):
        match = pattern.match(filename)
        if match:
            base_name, part_num, ext = match.groups()
            new_name = f"{base_name}.{ext}.{int(part_num):03d}"
            print(f"[还原] {filename} → {new_name}")
            os.rename(filename, new_name)

def rename_to_part_format():
    """
    将 xxx.7z.001 → xxx-Part1.7z 等格式
    """
    pattern = re.compile(r'^(.*?\.(7z|rar|zip))\.(\d{3,})$')
    for filename in os.listdir('.'):
        match = pattern.match(filename)
        if match:
            base_name, ext, part_num = match.groups()
            part_int = int(part_num)
            new_name = f"{base_name.replace(f'.{ext}', '')}-Part{part_int}.{ext}"
            print(f"[重命名] {filename} → {new_name}")
            os.rename(filename, new_name)

def main():
    if find_part_format_files():
        print("检测到 PartX 格式，正在还原为 .xxx.001 格式...")
        rename_to_split_format()
    else:
        print("检测到分卷文件，正在重命名为 PartX 格式...")
        rename_to_part_format()

    print("\n作者: Radiumbit\n项目地址:https://github.com/Radium-bit/ZipAutoPartRenamer\n")
    input("\n操作完成，按回车键退出...")

if __name__ == "__main__":
    main()
