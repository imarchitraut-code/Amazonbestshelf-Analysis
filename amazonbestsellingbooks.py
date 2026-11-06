import pandas as pd
import streamlit
import matplotlib.pyplot as plt

streamlit.title("Amazon Bestsellers Analysis")

df = pd.read_csv('bestsellers with categories - bestsellers with categories.csv')

streamlit.header("Full Dataset")
streamlit.dataframe(df)

streamlit.header("Search by Author")
search_author = streamlit.text_input("Enter author name")
if search_author:
    results = df[df['Author'].str.contains(search_author, case=False, na=False)]
    streamlit.dataframe(results)
streamlit.header("Search by Name")
search_book = streamlit.text_input("Enter book name")
if search_book:
    results = df[df['Name'].str.contains(search_book, case=False, na=False)]
    streamlit.dataframe(results)

streamlit.header("Most Frequently Best-Selling Authors")
num_authors = streamlit.slider("How many authors to show?", 1, 50, 10)
streamlit.bar_chart(df['Author'].value_counts().head(num_authors))

streamlit.header("10 Least Frequently Best-Selling Authors")
streamlit.dataframe(df['Author'].value_counts().tail(10))

streamlit.header("Top Most Frequent Genres")
streamlit.bar_chart(df['Genre'].value_counts().head(10))

streamlit.header("Average User Rating and Price by Genre")
streamlit.dataframe(
    df.groupby('Genre')[['User Rating', 'Price']].mean(),
    column_config={
        "Price": streamlit.column_config.NumberColumn("Price", format="$%.2f")
    }
)

streamlit.header("search books according to price and user rating")
min_price=float(df['Price'].min())
max_price=float(df['Price'].max())
max_rating=float(df['User Rating'].max())
min_rating=float(df['User Rating'].min())
price_range=streamlit.slider("select the range of price",min_price,max_price,(min_price,max_price))
userrating_range=streamlit.slider("select the range of rating",min_rating,max_rating,(min_rating,max_rating))
price_low, price_high = price_range
rating_low, rating_high = userrating_range
filtered_df=df[(df['Price']>=price_low) & (df['Price']<=price_high) & (df['User Rating']>=rating_low) & (df['User Rating']<=rating_high)]
streamlit.write(f"Showing{len(filtered_df)} books from {len(df)}")
streamlit.dataframe(
    filtered_df,
    column_config={
        "Price": streamlit.column_config.NumberColumn("Price", format="$%.2f")
    }
)
streamlit.metric("Average Book Price", f"${df['Price'].mean():.2f}")

streamlit.header("Most Appeared Book in the List")
streamlit.write(df['Name'].value_counts().head(1))

streamlit.header("Does Price Correlate with User Rating?")
correlation = df['Price'].corr(df['User Rating'])
streamlit.metric("Correlation", round(correlation, 3))

streamlit.header("Number of Books by Genre")
fig, ax = plt.subplots()
df['Genre'].value_counts().plot(kind='bar', ax=ax, title='Number of Books by Genre')
ax.set_xlabel('Genre')
ax.set_ylabel('Number of Books')
plt.xticks(rotation=45)
streamlit.pyplot(fig)