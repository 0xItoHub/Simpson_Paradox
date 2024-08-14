import pandas as pd
import matplotlib.pyplot as plt

# データセットの作成
data = {
    'Group': ['A', 'A', 'B', 'B'],
    'Success': [20, 30, 40, 10],
    'Total': [50, 50, 100, 100]
}

df = pd.DataFrame(data)

# 成功率を計算
df['Success Rate'] = df['Success'] / df['Total']

# グラフの描画
plt.figure(figsize=(8, 5))
plt.bar(df['Group'], df['Success Rate'], color=['blue', 'blue', 'green', 'green'])

# 全体の成功率
overall_success = df['Success'].sum() / df['Total'].sum()
plt.axhline(overall_success, color='red', linestyle='--', label='Overall Success Rate')

plt.title("Simpson's Paradox Example")
plt.ylabel('Success Rate')
plt.legend()
plt.show()
