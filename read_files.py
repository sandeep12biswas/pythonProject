


def count_occurences(file_name, word):
    word_count = 0
    f=None
    try:
        f = open(file_name)
        file_lst = f.readlines()
        print(f"file {file_lst}")
        for element in file_lst:
            srl_lst =  element.split()
            for words in srl_lst:
                #print(f"Words in each sentense {words} and {word} is not same", words.__eq__(word))
                words = words.replace(',', '').replace('.', '')
                if words.__eq__(word) :
                    word_count = word_count+1
        print(f"The word {word} comes {word_count} times in the file {file_name}")
    except Exception as e:
        print(f"There is a error while processing the file, exception is {e}")
    finally:
        f.close()


count_occurences('resources/first_file.txt','bit')

