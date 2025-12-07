def word_count(text):
  wc_list = text.split()
  return len(wc_list)

def character_count(text):
  charact_dict = {}
  for c in text.lower():
    if not c in charact_dict:
      charact_dict[c] = 1
    else:
      charact_dict[c] = charact_dict[c] + 1
  return charact_dict

def sort_on(items):
    return items["num"]

def sort_count(dictionnary):
  sorted = []
  for k,v in dictionnary.items():
    tmp_dict={ 'char': k, 'num': v }
    sorted.append(tmp_dict)
  sorted.sort(reverse=True, key=sort_on)
  return sorted