import wikipedia

def get_page_sumarries(page_name):
    try:
        return [[page_name, wikipedia.page(page_name, auto_suggest=False).summary]]
    except wikipedia.exceptions.DisambiguationError as err:
        page_name = wikipedia.random(1)
        return get_page_sumarries(page_name)

def get_random_pages_summary(pages=0):
    ret = []
    page_names = [wikipedia.random(1) for i in range(pages)]
    for p in page_names:
        for page_summary in get_page_sumarries(p):
            ret.append(page_summary)
        return ret

text = []
number_of_pages = 10000
for x in range (number_of_pages):
    text.append(get_random_pages_summary(1)) 

word = []
data_5_letters_words = []
file = open(r#insert path to textfile here,"w+", encoding="utf-8")

for i in range (len(text)):
    j = 0
    text_var = text[i]
    text_var = text_var[0]
    text_var = list(text_var)
    text_var = list(text_var[1])
    while (j < len(text_var)):
        if (text_var[j].isalpha()):
            word.append(text_var[j])
            j += 1
        else:
            data_var = "".join(word)
            j += 1
            if (len(data_var) == 5 and data_var[0].islower() and (not(data_var in data_5_letters_words))):
                data_5_letters_words.append(data_var)
                file.write(data_var)
                file.write("\n")
                data_var = ""
                word = []
            else:
                data_var = ""
                word = []           
file.close()                        