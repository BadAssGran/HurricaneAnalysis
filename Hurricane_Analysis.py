
# All debugging print statements are left on purpose, if you wish to check quickly that every function runs as expected.
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


list_of_lists = [names, months, years, max_sustained_winds, areas_affected, damages, deaths]

# write your update damages function here:
def updated_damages(lst):
    updated_lst = []
    for item in lst:
        if item[-1] == "B":
            item = float(item[:-1])
            item *= 1000000000.00

        elif item[-1] == "M":
            item = float(item[:-1])
            item *= 1000000.00
        updated_lst.append(item)
    return updated_lst

#damages_lst = updated_damages(damages)
#print(damages_lst)

#The following function was not required by the project but I found I would be reusing this code in a few of the functions below, so I decided to throw this together.
def hurricane_values_dict_constructor(*list_of_lists):
    hurricane_values_list = []
    for n, m, y, w, a, d, dt in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
        hurricane_values_list.append(
            {"Name": n, "Month": m, "Year": y, "Max Sustained Wind": w, "Areas Affected": a, "Damages": d,
             "Deaths": dt})
    return hurricane_values_list
#hurricane_dict = hurricane_values_dict_constructor(*list_of_lists)
#print(hurricane_dict)

# write your construct hurricane dictionary function here:

def hurricane_dict_constructor(*list_of_lists):
    hurricane_info_dict = {}
    values = hurricane_values_dict_constructor(*list_of_lists)

    for k, v in zip(names, values):
        hurricane_info_dict[k] = v
    return hurricane_info_dict

#hurricane_dict_of_dicts = hurricane_dict_constructor(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_dict_of_dicts)


# write your construct hurricane by year dictionary function here:

def hurricane_by_year_constructor(*list_of_lists):
    vals = hurricane_values_dict_constructor(*list_of_lists)
    hurricane_by_year_dict = {}
    for k, v in zip(years, vals):
        if k not in hurricane_by_year_dict:
            hurricane_by_year_dict[k] = [v]
        else:
            hurricane_by_year_dict[k].append(v)
    return hurricane_by_year_dict
#h_by_year = hurricane_by_year_constructor(*list_of_lists)
#print(h_by_year)

# write your count affected areas function here:
def affected_areas_dict_constructor(areas_affected):
    area_names = {}
    for item in areas_affected:
        for area in item:
            if area not in area_names:
                area_names[area] = 1
            else:
                area_names[area] += 1
    return area_names

#areas_dict = affected_areas_dict_constructor(areas_affected)
#print(areas_dict)


# write your find most affected area function here:

def most_affected_area(areas_affected):
    areas_dict = affected_areas_dict_constructor(areas_affected)
    max_val = max(areas_dict.values())
    for k in areas_dict.keys():
        if areas_dict[k] == max_val:
            most_affected = k
    return (most_affected, max_val)

#most_battered = most_affected_area(areas_affected)
#print(most_battered)

# write your greatest number of deaths function here:

def deadliest_hurricane(names, deaths):
    max_val = max(deaths)
    for n, d in zip(names, deaths):
        if d == max_val:
            deadliest = n
    return (deadliest, max_val)

#deadliest_storm = deadliest_hurricane(names, deaths)
#print(deadliest_storm)


# write your categorize by mortality function here:
def categorize_by_mortality(names, deaths):
    mortality_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for n, d in zip(names, deaths):
        if d == 0:
            mortality_rating[0].append({n:d})
        elif d > 0 and d <= 100:
            mortality_rating[1].append({n:d})
        elif d > 100 and d <= 500:
            mortality_rating[2].append({n:d})
        elif d > 500 and d <= 1000:
            mortality_rating[3].append({n:d})
        elif d > 1000 and d <= 10000:
            mortality_rating[4].append({n:d})
        else:
            mortality_rating[5].append({n:d})
    return mortality_rating

#mortality = categorize_by_mortality(names, deaths)
#print(mortality)


# write your greatest damage function here:
damages_in_numbers = updated_damages(damages)

def greatest_damage(names, damages_in_numbers):
    max_damage = 0.0
    for name, damage in zip(names, damages_in_numbers):
        if type(damage) == type(max_damage):
            if damage > max_damage:
                max_damage = damage
                most_damaging = name
    return (most_damaging, max_damage)

#expensive_hurricane = greatest_damage(names, damages_in_numbers)
#print(expensive_hurricane)


# write your categorize by damage function here:
def categorize_by_damages(lst_names, lst_damages):
    categorized_by_damages_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for name1, damage1 in zip(lst_names, lst_damages):
        if type(damage1) != type(name1):
            if damage1 == 0:
                categorized_by_damages_dict[0].append({name1: damage1})
            elif damage1 > 0 and damage1 <= 100000000:
                categorized_by_damages_dict[1].append({name1: damage1})
            elif damage1 > 100000000 and damage1 <= 1000000000:
                categorized_by_damages_dict[2].append({name1: damage1})
            elif damage1 > 1000000000 and damage1 <= 10000000000:
                categorized_by_damages_dict[3].append({name1: damage1})
            elif damage1 > 10000000000 and damage1 <= 50000000000:
                categorized_by_damages_dict[4].append({name1: damage1})
            elif damage1 > 50000000000:
                categorized_by_damages_dict[5].append({name1: damage1})
    return (categorized_by_damages_dict)

#damages_categorized = categorize_by_damages(names, damages_in_numbers)
#print(damages_categorized)
