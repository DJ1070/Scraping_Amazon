f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=Processor&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,51):
    url = 'https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=' + str(i) + '&qid=1594555641&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()
