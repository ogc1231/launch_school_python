def invert_dict(dictionary) :
    list1 = list(dictionary.values())
    list2 = list(dictionary.keys())

    invert_dict = dict(zip(list1, list2))

    return invert_dict

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True