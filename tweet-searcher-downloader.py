
#pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twintimport twint

# Configure search parameters
c = twint.Config()
c.Search = "your_search_query"
c.Lang = "en"
c.Limit = 100  # Number of tweets to download
c.Store_csv = True  # Store tweets in a CSV file
c.Output = "tweets.csv"  # Output file name

# Run search
twint.run.Search(c)
