#!/usr/bin/env python3
#
# A reporting tool for a News site
from datetime import datetime
from news_reporting_tool_db\
    import get_articles_all_time_top_three,\
    get_authors_most_popular,\
    get_dates_w_excessive_req_errors

# File names for reports
f1_name = '1_articles_all_time_top_three.txt'
f2_name = '2_authors_sorted_by_popularity.txt'
f3_name = '3_days_with_excessive_errors.txt'

# Write report of all time most popular 3 articles
f1 = open(f1_name, 'w')
for title, count in get_articles_all_time_top_three():
    f1.write('%s - %d\n' % (title, count))
f1.close()

# Write report of authors sorted by popularity
f2 = open(f2_name, 'w')
for name, count in get_authors_most_popular():
    f2.write('%s - %d\n' % (name, count))
f2.close()

# Write report of days with excessive req. errors
f3 = open(f3_name, 'w')
for date, perc in get_dates_w_excessive_req_errors():
    # Apply output formatting
    perc_ = "{:2.2f}".format(perc) + '% errors'
    date_ = datetime.strftime(date, '%b %d, %Y')

    f3.write('%s - %s\n' % (date_, perc_))
f3.close()
