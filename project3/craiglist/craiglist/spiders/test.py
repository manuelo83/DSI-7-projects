import pandas as pd

urls = pd.read_csv('/Users/manuel/Desktop/dsi-sf-7-materials_manuel/projects/project-3/lista_us_cities.csv')
# print urls['0'].values
urls = urls['0'].tolist()
# print urls
# break
# where the spider will go
city_urls = []
for url in urls:
    # print url
    # print "http://{}.craigslist.org/search/sss?query=rv".format(url)

    if ' ' not in url:

    	# continue
        # print url
        city_urls.append("http://{}.craigslist.org/search/sss?query=rv".format(url))

print city_urls
