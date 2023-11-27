from grammar import Grammar

if __name__ == '__main__':
    grammar = Grammar.from_file("g1.txt")
    print(grammar.print_syntax())

