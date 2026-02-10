import os
import pandas as pd
import numpy as np
from datetime import datetime

# 配置目录
DATA_FOLDER = "my_source_files"

def generate_random_csv():
    # 确保目录存在
    os.makedirs(DATA_FOLDER, exist_ok=True)

    # 生成基于时间的文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.csv"
    file_path = os.path.join(DATA_FOLDER, filename)
    
    # 生成随机数据 (15行 8列)
    df = pd.DataFrame(
        np.random.randn(15, 8), 
        columns=[f'指标_{i+1}' for i in range(8)]
    )
    
    # 保存文件
    df.to_csv(file_path, index=False)
    print(f"成功生成数据文件: {file_path}")

if __name__ == "__main__":
    generate_random_csv()