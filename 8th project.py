'''favouriteseries=[]
s1=input("Enter your fav series:")
favouriteseries.append(s1)
s2=input("Enter your fav series:")
favouriteseries.append(s2)
s3=input("Enter your fav series:")
favouriteseries.append(s3)
s4=input("Enter your fav series:")
favouriteseries.append(s4)
'''
# for smart work we will use loop method

favouriteseries=[]
for i in range(4):
    series=input("Enter your fav series:")
    favouriteseries.append(series)
    print(favouriteseries)