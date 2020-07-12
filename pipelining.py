################################# IMPERATIVE CODE #############################

# bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
#          {'name': 'women', 'country': 'Germany', 'active': False},
#          {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

# def format_bands(bands):
#     for band in bands:
#         band['country'] = 'Canada'
#         band['name'] = band['name'].replace('.', '')
#         band['name'] = band['name'].title()

# format_bands(bands)

# print bands
# # => [{'name': 'Sunset Rubdown', 'active': False, 'country': 'Canada'},
# #     {'name': 'Women', 'active': False, 'country': 'Canada' },
# #     {'name': 'A Silver Mt Zion', 'active': True, 'country': 'Canada'}]

###############################################################################

def pipeline_each(bands,operations):
    if len(operations) >= 1:
        pipeline_each(map(operations[0],bands),operations[1:])
    else:
        return bands

def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band,'country','Canada')

def strip_punctuation_from_name(band):
    # strings are immutable in python, no problem with .replace()
    return assoc(band,'name', band['name'].replace('.','')) 

def capitalize_names(band):
    # strings are immutable in python, no problem with .title()
    return assoc(band,'name',band['name'].title())

def test_function(operation):
    band = {'name': 'a silver mt. zion', 'country': 'Spain'}
    result = operation(band)
    print(band, ' -> ', operation.__name__,' -> ', result)


bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

# test_function(set_canada_as_country)
# test_function(strip_punctuation_from_name)
# test_function(capitalize_names)

print(pipeline_each(bands, [set_canada_as_country,strip_punctuation_from_name,capitalize_names]))