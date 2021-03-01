f = open('laptop_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=laptop&i=computers&language=en_US&ref=nb_sb_noss_1'
f.write(url)
f.write('\n')

for i in range(2,401):
    url = 'https://www.amazon.com/s?k=laptop&i=computers&page=' + str(i) + '&language=en_US&qid=1614601629&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()
