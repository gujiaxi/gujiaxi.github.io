import os

def check_file_for_double_img(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:  # 兼容非 utf-8 文件
        try:
            with open(filepath, encoding='gbk') as f:
                lines = f.readlines()
        except:
            return False  # 不可读文件跳过

    for i in range(len(lines) - 1):
        if lines[i].lstrip().startswith('<img') and lines[i+1].lstrip().startswith('<img'):
            print(f"Found in {filepath}:")
            print("  " + lines[i].rstrip())
            print("  " + lines[i+1].rstrip())
            return True
    return False

# 扫描当前目录及子目录所有.md、.html、.txt
for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith(('.md', '.html', '.txt')):
            check_file_for_double_img(os.path.join(root, name))
