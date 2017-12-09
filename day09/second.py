import sys



def main():
    s = input()
    i = 0
    score = 0
    nest_level = 0
    garbage_count = 0
    in_garbage = False
    while i < len(s):
        if in_garbage and s[i] != '!' and s[i] != '>':
            garbage_count += 1

        if s[i] == '{' and not in_garbage:
            nest_level += 1
            score += nest_level
        elif s[i] == '}' and not in_garbage:
            nest_level -= 1
        elif s[i] == '<' and not in_garbage:
            in_garbage = True
        elif s[i] == '>':
            in_garbage = False
        elif s[i] == '!':
            i += 1
        i += 1
    # print(score)
    print(garbage_count)

if __name__ == '__main__':
    main()
