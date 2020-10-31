import re
input = "(ab(c){2}d){2}(ab){2}"
expected_output = "abccdabccdabab"

begin_str_char = "("
end_str_char = ")"
begin_num_char = "{"
end_num_char = "}"

##def clean(phrase):
##    phrase = phrase[1:-1]
##    l_end_str_char_ind = phrase.rindex(end_str_char)
##    l_begin_num_char_ind = phrase.rindex(begin_num_char)
##    times = int(phrase[l_begin_num_char_ind+1:])
##    phrase = phrase[:l_end_str_char_ind]
##    beg_ind = phrase.find(begin_str_char)
##    end_ind = phrase.find(end_num_char)
##    if beg_ind == end_ind:
##        return phrase * times
##    print(phrase[:beg_ind],phrase[beg_ind:end_ind+1],phrase[end_ind+1:],times)
##    return (phrase[:beg_ind] + \
##            findPhrases(phrase[beg_ind:end_ind+1]) + \
##            phrase[end_ind+1:])*times
##
##def findPhrases(input):
##    phrases = []
##    index = 0
##    while (len(input) > 0):
##        curr_str = input[:index+1]
##        if curr_str.count(begin_str_char) == curr_str.count(end_str_char) ==\
##           curr_str.count(begin_num_char) == curr_str.count(end_num_char):
##            phrases.append(curr_str)
##            input = input[index+1:]
##            index = 0
##        else:
##            index += 1
##    return "".join([clean(phrase) for phrase in phrases])

def solve_phrase(phrase):
    phrase = phrase[1:-1]
    l_end_str_char_ind = phrase.rindex(end_str_char)
    l_begin_num_char_ind = phrase.rindex(begin_num_char)
    times = int(phrase[l_begin_num_char_ind+1:])
    phrase = phrase[:l_end_str_char_ind]
    beg_ind = phrase.find(begin_str_char)
    end_ind = phrase.find(end_num_char)
    return phrase * times

def valid(match):
    if match.count(begin_str_char) == \
       match.count(end_str_char) == \
       match.count(begin_num_char) == \
       match.count(end_num_char):
        return True
    return False

all_combinations = []
for start_index in range(len(input)):
    for end_index in range(len(input),-1,-1):
        all_combinations.append(input[start_index:end_index])
components = set()
for match in all_combinations:
    if valid(match):
        potential_matches = re.findall(r"\(\S*\)\{\d\}",match)
        for eachValidMatch in potential_matches:
            if len(eachValidMatch) != 0 and valid(eachValidMatch):
                components.add(eachValidMatch)
all_my_pieces = sorted(list(components),key=len)
for i in range(len(all_my_pieces)-1):
    result = solve_phrase(all_my_pieces[i])
    for j in range(len(all_my_pieces)):
        if all_my_pieces[i] in all_my_pieces[j] and i != j:
            all_my_pieces[j] = all_my_pieces[j].replace(all_my_pieces[i],result)
print(all_my_pieces[-1])
