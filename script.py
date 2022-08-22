def get_libs(answer):
    code = answer.split('<code>')[1:]
    code = [part.split('</code>')[0] for part in code]
    code = '. '.join(code)
    
    libs = set()
    
    code = ['', ''] + code.replace('\n', ' ').split(' ')
    for i in range(len(code)):
        if code[i] == 'import':
            if code[i - 2] == 'from':
                libs.add(code[i - 1].split('.')[0])
            else:
                libs.add(code[i + 1].split('.')[0])
                
    return ' '.join(libs)
        