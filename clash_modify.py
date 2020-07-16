def main():
    clash_lines = ''
    with open('EasyPrivacy.yaml', 'r+') as clash_rule_origine:
        for clash_line in clash_rule_origine:
            if ',' in clash_line:
                clash_lines += '  - ' + clash_line
            elif '#' in clash_line:
                clash_lines += clash_line
        clash_lines = "payload:\n" + clash_lines
        # print(clash_lines)
    with open('EasyPrivacy.yaml', 'w') as clash_rule:
        clash_rule.write(clash_lines)





if __name__ == '__main__':
    main()
