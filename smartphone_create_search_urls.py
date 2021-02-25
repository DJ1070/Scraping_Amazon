f = open('smartphone_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=android+phone&rh=n%3A7072561011&ref=nb_sb_noss'
f.write(url)
f.write('\n')


for i in range(2,88):
    url = 'https://www.amazon.com/s?k=android+phone&i=mobile&rh=n%3A7072561011&page=' + str(i) + '&qid=1613497053&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()