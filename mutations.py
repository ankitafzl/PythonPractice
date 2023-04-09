def mutate_string(string, position, character):
    list1=list(string)
    list1[position]=character;
    string=''.join(list1);
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)