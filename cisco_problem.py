import re
import string

input_string = "(ab(c){2}d){2}(ab){2}"
expected_output = "abccdabccdabab"

begin_str_char = "("
end_str_char = ")"
begin_num_char = "{"
end_num_char = "}"

def _solve_phrase(phrase):
    phrase = phrase[1:-1]
    l_end_str_char_ind = phrase.rindex(end_str_char)
    l_begin_num_char_ind = phrase.rindex(begin_num_char)
    times = int(phrase[l_begin_num_char_ind+1:])
    phrase = phrase[:l_end_str_char_ind]
    beg_ind = phrase.find(begin_str_char)
    end_ind = phrase.find(end_num_char)
    return phrase * times

def _valid(match):
    if match.count(begin_str_char) == \
       match.count(end_str_char) == \
       match.count(begin_num_char) == \
       match.count(end_num_char):
        return True
    return False

def reduceString(input_string):
    """Combination based solution"""
    all_combinations = []
    for start_index in range(len(input_string)):
        for end_index in range(len(input_string),-1,-1):
            all_combinations.append(input_string[start_index:end_index])
    components = set()
    for match in all_combinations:
        if _valid(match):
            potential_matches = re.findall(r"\(\S*\)\{\d\}",match)
            for eachValidMatch in potential_matches:
                if len(eachValidMatch) != 0 and _valid(eachValidMatch):
                    components.add(eachValidMatch)
    all_my_pieces = sorted(list(components),key=len)
    for i in range(len(all_my_pieces)-1):
        result = _solve_phrase(all_my_pieces[i])
        for j in range(len(all_my_pieces)):
            if all_my_pieces[i] in all_my_pieces[j] and i != j:
                all_my_pieces[j] = all_my_pieces[j].replace(all_my_pieces[i],result)
    return all_my_pieces[-1]

def decodeString(input_string):
    """Text Decoding Solution"""
    character_strings = []
    numbers = []
    fullstring = ""
    tempstring = ""
    tempnum = ""
    index = 0
    while index < len(input_string):
        curr_char = input_string[index]
        if curr_char == "(":
            resolve = False
            if len(tempstring) > 0:
                character_strings.append(tempstring)
                tempstring = ""
            index += 1
        elif curr_char in string.ascii_letters:
            if resolve:
                character_strings[-1] += curr_char
            else:
                tempstring = tempstring + curr_char
            index += 1
        elif curr_char == ")":
            if len(tempstring) > 0:
                character_strings.append(tempstring)
                tempstring = ""
            index += 1
        elif curr_char == "{":
            index += 1
        elif curr_char in string.digits:
            tempnum = tempnum + curr_char
            index += 1
        elif curr_char == "}":
            resolve = True
            numbers.append(int(tempnum))
            tempnum = ""
            print(character_strings, numbers)
            while len(numbers) > 0:
                character_string = character_strings.pop()
                number = numbers.pop()
                print(character_string,number)
                result = character_string * number
                if len(character_strings) > 0:
                    character_strings[-1] = character_strings[-1] + result
                elif len(numbers) == len(character_strings) == 0:
                    fullstring += result
            index += 1
    return fullstring
