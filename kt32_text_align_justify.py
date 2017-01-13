def line_justified(line, width):
    n_of_words = len(line)
    n_of_spaces = n_of_words and n_of_words - 1 or 0
    total_space = width - len(''.join(line))
    add_space = total_space - n_of_spaces
    
    spaces = [' '] * n_of_spaces
    if add_space and n_of_spaces:
    	for i in range(add_space):
            el = i % n_of_spaces
            spaces[el] += ' '
    ret = ''
    for i, word in enumerate(line):
        ret += word
        if i < len(spaces):
            ret += spaces[i]
    return ret
    

def justify(text, width):
    if not text:
        return 
    ret = []
    cur_line = []
    for word in text.split():
        cur_line_len = len(' '.join(cur_line))
        if cur_line_len + 1 + len(word) <= width:
            cur_line.append(word)
        else:
            ret.append(line_justified(cur_line, width))
            cur_line = [word, ]
    if line_justified(cur_line, width) != ret[-1]:
        ret.append(' '.join(cur_line))
    
    return '\n'.join(ret)