f = open('headphone_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=headphones&i=electronics-intl-ship&ref=nb_sb_noss'
f.write(url)
f.write('\n')


for i in range(2,401):
    url = 'https://www.amazon.com/s?k=headphones&i=electronics-intl-ship&page=' + str(i) + '&qid=1613483962&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()
