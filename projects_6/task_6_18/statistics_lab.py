import pandas as pd
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5434",
        user="postgres",
        password="student",
        database="student_task"
    )

    query = """
    SELECT 
        pr.price, 
        p.name AS product_name, 
        p.category
    FROM 
        prices pr
    JOIN 
        products p ON pr.product_id = p.id
    """

    df = pd.read_sql_query(query, connection)

    print("СТАТИСТИКА ПО ЦЕНАМ:")
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()

    print(f"Среднее значение: {mean_price} руб.")
    print(f"Медиана: {median_price} руб.")
    print(f"Стандартное отклонение: {std_price} руб.")
    print(f"Минимальная цена: {min_price} руб.")
    print(f"Максимальная цена: {max_price} руб.")

    Q1 = df['price'].quantile(0.25)
    Q2 = df['price'].quantile(0.50)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1

    print("КВАРТИЛИ И МЕЖКВАРТИЛЬНЫЙ РАЗМАХ:")
    print(f"Первый квартиль (25%): {Q1:.2f} руб.")
    print(f"Второй квартиль (50%/медиана): {Q2:.2f} руб.")
    print(f"Третий квартиль (75%): {Q3:.2f} руб.")
    print(f"Межквартильный размах (IQR): {IQR:.2f} руб.")

    high_price_products = df[df['price'] > Q3][['product_name', 'category', 'price']]
    print(f"Товары с ценой выше Q3 (>{Q3:.2f} руб.):")
    print(high_price_products.to_string(index=False))

    print("СТАТИСТИКА ПО КАТЕГОРИЯМ:")
    category_stats = df.groupby('category').agg(
        count=('price', 'count'),
        mean_price=('price', 'mean'),
        median_price=('price', 'median'),
        std_price=('price', 'std')
    ).round(2).sort_values('mean_price', ascending=False)

    print(category_stats)

    print("ТОП-5 ТОВАРОВ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН:")
    price_spread = df.groupby('product_name').agg(
        min_price=('price', 'min'),
        max_price=('price', 'max')
    )
    price_spread['price_range'] = price_spread['max_price'] - price_spread['min_price']

    top_5_spread = price_spread.sort_values('price_range', ascending=False).head(5)

    top_5_with_categories = df[['product_name', 'category']].drop_duplicates().merge(
        top_5_spread, on='product_name'
    )

    print(top_5_with_categories[['product_name', 'category', 'min_price', 'max_price', 'price_range']].to_string(index=False))

except Exception as error:
    print(f"Ошибка при подключении: {error}")