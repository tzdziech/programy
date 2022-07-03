def count_substring(string, sub_string):
    count = 0
    print("Szukamy:", sub_string)
    for i in range(0, len(string)-len(sub_string)+1):
        print("Szukam w", string[i:i+len(sub_string)])
        if sub_string in string[i:i+len(sub_string)]:
            print("znalazlem")
            count += 1
    return count


string = "ABCDCDC"
sub_string = "CDC"

count = count_substring(string, sub_string)
print(count)