def get_gender(sex ='unknow'):
    if sex is 'm':
        sex = 'Male'
    if sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()