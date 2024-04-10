import pandas as pd
import datetime
import random

# データポイント数
num_data_points = 10000

# データ生成
start_time = datetime.datetime.now()
time_stamps = [start_time + datetime.timedelta(seconds=i*600) for i in range(num_data_points)]

temperatures = [ random.randint(-20,40) for _ in range(num_data_points)]

# DataFrameの作成
data = {"Time": time_stamps, "status": temperatures}
df = pd.DataFrame(data)

# CSVファイルに書き込み
df.to_csv("time_temp.csv", index=False)
