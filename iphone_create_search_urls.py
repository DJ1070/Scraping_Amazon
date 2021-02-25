f = open('iphone_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=iphone&i=mobile&ref=nb_sb_noss'
f.write(url)
f.write('\n')


for i in range(2,77):
    url = 'https://www.amazon.com/s?k=iphone&i=mobile&page=' + str(i) + '&qid=1613575472&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()