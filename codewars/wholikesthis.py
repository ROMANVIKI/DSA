def likes(names):
    name_count = len(names)
    # print(name_count)
    if len(names) > 4 or len(names) == 4:
        print(f"'{names[0]}, {names[1]} and {name_count - 2} others like this'")
    elif len(names) == 3:
        print(f"'{names[0]}, {names[1]} and {names[2]} like this'")
    elif len(names) == 2:
        print(f"'{names[0]} and {names[1]} like this'")
    elif len(names) == 1:
        print(f"'{names[0]} likes this'")
    else:
        print("'no one likes this'")

name_list = []
result = likes(names=name_list)

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.