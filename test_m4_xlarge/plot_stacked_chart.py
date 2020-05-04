import matplotlib.pyplot as plt


year = [2014, 2015, 2016, 2017, 2018, 2019]  
tutorial_public = [33, 117, 98, 54, 28, 15]  
tutorial_premium = [5, 5, 13, 56, 39, 11]

bar1 = plt.barh(year, tutorial_premium, color="g",label="boh2")  
# careful: notice "bottom" parameter became "left"
bar2 = plt.barh(year, tutorial_public, left=tutorial_premium, color="r",label="boh")
# bar1 = plt.bar(np.arange(len(errorRateListOfFast))+ bar_width, errorRateListOfFast, bar_width, align='center', alpha=opacity, color='b', label='Fast <= 6 sec.')
# bar2 = plt.bar(range(len(errorRateListOfSlow)), errorRateListOfSlow, bar_width, align='center', alpha=opacity, color='r', label='Slower > 6 sec.')

# Add counts above the two bar graphs
for rect in bar1 + bar2:
    height = rect.get_height()
    #plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    bl = rect.get_xy()
    x = 0.5*rect.get_width() + bl[0]
    y = 0.5*rect.get_height() + bl[1]
    plt.text(x, y,'%d' % int(height),ha='center',va='center', color='w')
# we also need to switch the labels
plt.xlabel('Number of futurestud.io Tutorials')  
plt.ylabel('Year')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

