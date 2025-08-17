import os

def rename_files_sequentially():
    # 获取当前目录下的所有文件（不包含目录）
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 排除脚本自身，避免重命名脚本文件
    script_name = os.path.basename(__file__)
    files = [f for f in files if f != script_name]
    
    # 按读取顺序重命名文件
    for i, filename in enumerate(files, start=1):
        # 获取文件扩展名
        file_ext = os.path.splitext(filename)[1]
        
        # 新文件名：数字 + 原扩展名
        new_filename = f"{i}{file_ext}"
        
        # 避免文件名冲突
        counter = 1
        while os.path.exists(new_filename):
            new_filename = f"{i}_{counter}{file_ext}"
            counter += 1
        
        # 重命名文件
        os.rename(filename, new_filename)
        print(f"已将 '{filename}' 重命名为 '{new_filename}'")

if __name__ == "__main__":
    rename_files_sequentially()
    print("文件重命名完成！")
