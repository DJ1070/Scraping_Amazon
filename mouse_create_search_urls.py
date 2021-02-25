f = open('mouse_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=mouse&i=computers-intl-ship&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,401):
    url = 'https://www.amazon.com/s?k=mouse&i=computers-intl-ship&page=' + str(i) + '&qid=1613495076&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()