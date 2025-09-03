def count_occurrences(list1) :
    new_dict = {}

    for ele in list1 :
        list1.count(ele)
        new_dict[ele] = new_dict.get(ele, 0) + 1

    for key, value in new_dict.items() :
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)