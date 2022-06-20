# start , end ---> multiplication-table[start:end]



start = int(input('Enter Start: '))  # cast
end = int(input('Enter End: '))

for x in range(start, end+1):

    for y in range(1,13):

        print(f"{x} X {y} = {x*y}")

    print('--------------')

