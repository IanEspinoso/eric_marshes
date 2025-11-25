from operator import itemgetter
import requests
import plotly.express as px

# Creates an API call and verifies the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Processes the information about each article contribution
sub_ids = r.json()
sub_dicts = []
for sub_id in sub_ids[:25]:
    try:
        # Creates a new API call for each article contribution
        url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"
        r = requests.get(url)
        print(f"id: {sub_id}\tstatus: {r.status_code}")
        response_dict = r.json()
        # Creates a dictionary for each article
        sub_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={sub_id}",
            'comments': response_dict['descendants'],
        }
        sub_dicts.append(sub_dict)
    except KeyError:
        print(f"{sub_id} had its comments deactivated.")

sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)

# Processes the information on the repositories
sub_links, comments, sub_titles = [], [], []
for sub_dict in sub_dicts:
    sub_titles.append(sub_dict['title'])
    comments.append(sub_dict['comments'])
    sub_links.append(f"<a href='{sub_dict['hn_link']}'>{sub_dict['title']}</a>")

# Creates a visual representation
title = "Most-Commented Hacker News Articles"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=sub_links, y=comments, title=title, labels=labels, 
             hover_name=sub_titles)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='darkorange', marker_opacity=0.6)

fig.show()