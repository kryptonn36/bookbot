def get_num_words(file_contents):
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")

def get_num_char(file_contents):
    dict_count = {}
    file_contents = file_contents.lower()
    words = file_contents.split()
    for word in words :
        # print(word)
        for character in word:
            if character in dict_count:
                dict_count[character] += 1
            else:
                dict_count[character] = 1
    
    return dict_count

def sorting(dict_count):
    dict_to_list = list(dict_count.items())
    sorted_list = sorted(dict_to_list ,key=lambda x:x[1], reverse=True)
    dict_count = dict(sorted_list)
    return dict_count