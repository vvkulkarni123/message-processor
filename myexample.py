wish = 'One day I will make Onions cry'
#print (wish.split(' '))
languages = 'Java, Python, C++, JavaScript'
#print (languages.split(', '))
countries = 'USA,Canada,Mexico,Brazil,United Kingdom,Uganda,South Africa'
countryNames=   countries.split(',')
countriesWithNameStartU = []

#print(countryNames)
for country in countryNames:
    if country.startswith('U'):
        countriesWithNameStartU.append(country)
print(countriesWithNameStartU)
mixed_string = 'There are 2 apples and 5 oranges and 45 bananas in the basket'
numbers = [int(s) for s in mixed_string.split() if s.isdigit()]
#print(numbers)
sum_of_numbers = sum(numbers)
print(sum_of_numbers)