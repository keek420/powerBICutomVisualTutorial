import pandas as pd
import numpy as np
import random

# 期間の日数
days = 31

# 1分ごとのデータを生成
minutes_per_day = 24 * 60
total_minutes = days * minutes_per_day

# 生産個数と不具合個数をランダムに生成
production_counts = np.random.randint(20, 41, total_minutes)

defect_counts = np.zeros(total_minutes)

# 不具合個数の計算
for i in range(total_minutes):
    defect_counts[i] = int(production_counts[i]*random.randint(0,30)/100)

# ちょこ停のシミュレーション
for i in range(total_minutes):
    if np.random.rand() <= 0.01:
        # 1%の確率で10分間停止
        production_counts[i:i+10] = 0
        defect_counts[i:i+10] = 0

# データフレームを作成
df = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-04-01', periods=total_minutes, freq='min'),
    'ProductionCount': production_counts,
    'DefectCount': defect_counts
})

# CSV形式で出力
df.to_csv('dummy_data.csv', index=False)
