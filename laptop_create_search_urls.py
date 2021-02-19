f = open('laptop_search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=laptop&i=computers&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1'
f.write(url)
f.write('\n')


for i in range(2,401):
    url = 'https://www.amazon.com/-/de/s?k=laptop&i=computers&page=' + str(i) + '&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1613478173&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()
