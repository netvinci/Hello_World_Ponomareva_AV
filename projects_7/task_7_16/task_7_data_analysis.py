import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch

conn = psycopg2.connect(
 host="localhost",

 port="5432",

 user="postgres",

 password="example",

 database="testdb"
)

query = """
SELECT 
    s.enrollment_year,
    e.grade
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.grade IS NOT NULL
"""

df = pd.read_sql(query, conn)

mean_grade = df['grade'].mean()
median_grade = df['grade'].median()

fig = plt.figure(figsize=(15, 5))
gs = gridspec.GridSpec(1, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

ax1.hist(df['grade'], bins=20, color='skyblue', edgecolor='black', alpha=0.7, density=True)
ax1.axvline(mean_grade, color='red', linestyle='--', linewidth=2, label=f'Среднее: {mean_grade:.1f}')
ax1.axvline(median_grade, color='green', linestyle='-', linewidth=2, label=f'Медиана: {median_grade:.1f}')
ax1.set_title('Распределение оценок')
ax1.set_xlabel('Оценка')
ax1.set_ylabel('Плотность')
ax1.legend()

ax2.boxplot(df['grade'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
ax2.set_title('Boxplot оценок')
ax2.set_xlabel('Оценка')

yearly_avg = df.groupby('enrollment_year')['grade'].mean().reset_index()
ax3.plot(yearly_avg['enrollment_year'], yearly_avg['grade'], marker='o', color='purple', linewidth=2)
ax3.set_title('Средняя оценка по году поступления')
ax3.set_xlabel('Год поступления')
ax3.set_ylabel('Средняя оценка')
ax3.grid(True, linestyle='--', alpha=0.3)
ax3.xaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))

plt.tight_layout()
plt.show()

Q1 = df['grade'].quantile(0.25)
Q3 = df['grade'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies = df[(df['grade'] < lower_bound) | (df['grade'] > upper_bound)]

if anomalies.empty:
    print("Аномалии не обнаружены")
else:
    print(f"Найдено аномалий: {len(anomalies)}")

conn.close()