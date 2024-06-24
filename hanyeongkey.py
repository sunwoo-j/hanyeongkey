# Hangul choseong(초성), jungseong(중성), jongseong(종성) lists
CHOSEONG_LIST = [char for char in "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"]
JUNGSEONG_LIST = [char for char in "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]
JONGSEONG_LIST = [char for char in " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"]

# Key mapping dictionary
ALPHABET_HANGUL_MAPPING = {
    'q': 'ㅂ', 'Q': 'ㅃ', 'w': 'ㅈ', 'W': 'ㅉ', 
    'e': 'ㄷ', 'E': 'ㄸ', 'r': 'ㄱ', 'R': 'ㄲ',
    't': 'ㅅ', 'T': 'ㅆ', 'y': 'ㅛ', 'Y': 'ㅛ',
    'u': 'ㅕ', 'U': 'ㅕ', 'i': 'ㅑ', 'I': 'ㅑ', 
    'o': 'ㅐ', 'O': 'ㅒ', 'p': 'ㅔ', 'P': 'ㅖ',
    'a': 'ㅁ', 'A': 'ㅁ', 's': 'ㄴ', 'S': 'ㄴ', 
    'd': 'ㅇ', 'D': 'ㅇ', 'f': 'ㄹ', 'F': 'ㄹ', 
    'g': 'ㅎ', 'G': 'ㅎ', 'h': 'ㅗ', 'H': 'ㅗ', 
    'j': 'ㅓ', 'J': 'ㅓ', 'k': 'ㅏ', 'K': 'ㅏ', 
    'l': 'ㅣ', 'L': 'ㅣ', 'z': 'ㅋ', 'Z': 'ㅋ',
    'x': 'ㅌ', 'X': 'ㅌ', 'c': 'ㅊ', 'C': 'ㅊ', 
    'v': 'ㅍ', 'V': 'ㅍ', 'b': 'ㅠ', 'B': 'ㅠ', 
    'n': 'ㅜ', 'N': 'ㅜ', 'm': 'ㅡ', 'M': 'ㅡ'
}
HANGUL_ALPHABET_MAPPING = {
    'ㄱ':'r', 'ㄲ':'R', 'ㄳ':'rt', 'ㄴ':'s',
    'ㄵ':'sw', 'ㄶ':'sg', 'ㄷ':'e', 'ㄸ':'E',
    'ㄹ':'f', 'ㄺ':'fr', 'ㄻ':'fa', 'ㄼ':'fq',
    'ㄽ':'ft', 'ㄾ':'fx', 'ㄿ':'fv', 'ㅀ':'fg',
    'ㅁ':'a', 'ㅂ':'q', 'ㅃ':'Q', 'ㅄ':'qt',
    'ㅅ':'t', 'ㅆ':'T', 'ㅇ':'d', 'ㅈ':'w',
    'ㅉ':'W', 'ㅊ':'c', 'ㅋ':'z', 'ㅌ':'x',
    'ㅍ':'v', 'ㅎ':'g', 'ㅏ':'k', 'ㅐ':'o',
    'ㅑ':'i', 'ㅒ':'O', 'ㅓ':'j', 'ㅔ':'p',
    'ㅕ':'u', 'ㅖ':'P', 'ㅗ':'h', 'ㅘ':'hk',
    'ㅙ':'ho', 'ㅚ':'hl', 'ㅛ':'y', 'ㅜ':'n',
    'ㅝ':'nj', 'ㅞ':'np', 'ㅟ':'nl', 'ㅠ':'b',
    'ㅡ':'m', 'ㅢ':'ml', 'ㅣ':'l'
}

# Convert consecutive jungseongs to compound jungseong
def check_compound_jungseong(char_list):
    jungseong_combinations = {
        ('ㅗ', 'ㅏ'): 'ㅘ', ('ㅗ', 'ㅐ'): 'ㅙ', ('ㅗ', 'ㅣ'): 'ㅚ',
        ('ㅜ', 'ㅓ'): 'ㅝ', ('ㅜ', 'ㅔ'): 'ㅞ', ('ㅜ', 'ㅣ'): 'ㅟ',
        ('ㅡ', 'ㅣ'): 'ㅢ'
    }
    return jungseong_combinations.get(tuple(char_list[:2]), char_list[0])

# Convert consecutive jongseongs to compound jongseong
def check_compound_jongseong(char_list):
    jongseong_combinations = {
        ('ㄱ', 'ㄱ'): 'ㄲ', ('ㄱ', 'ㅅ'): 'ㄳ',
        ('ㄴ', 'ㅈ'): 'ㄵ', ('ㄴ', 'ㅎ'): 'ㄶ',
        ('ㄹ', 'ㄱ'): 'ㄺ', ('ㄹ', 'ㅁ'): 'ㄻ',
        ('ㄹ', 'ㅂ'): 'ㄼ', ('ㄹ', 'ㅅ'): 'ㄽ',
        ('ㄹ', 'ㅌ'): 'ㄾ', ('ㄹ', 'ㅍ'): 'ㄿ',
        ('ㄹ', 'ㅎ'): 'ㅀ', ('ㅂ', 'ㅅ'): 'ㅄ'
    }
    return jongseong_combinations.get(tuple(char_list[:2]), char_list[0])

# Convert QWERTY to Dubeolsik
def alphabet2hangul(alphabet_input):
    # Map hangul from alphabet
    hangul_conversion = [ALPHABET_HANGUL_MAPPING.get(char, char) for char in alphabet_input]

    # Group by hangul characters
    hangul_len = len(hangul_conversion)
    hangul_char = []
    pos = 0
    for i in range(1, hangul_len):
        if i == hangul_len - 1:
            hangul_char.append(hangul_conversion[pos:])
        elif (hangul_conversion[i] in CHOSEONG_LIST and hangul_conversion[i+1] in JUNGSEONG_LIST) or \
             (hangul_conversion[i] not in CHOSEONG_LIST + JUNGSEONG_LIST):
            hangul_char.append(hangul_conversion[pos:i])
            pos = i

    # Convert compound vowels and consonants
    for char in hangul_char:
        if len(char) > 2 and char[0] in CHOSEONG_LIST and char[1] in JUNGSEONG_LIST:
            # Check for compound jungseong
            if char[1] in JUNGSEONG_LIST and char[2] in JUNGSEONG_LIST:
                temp_letter = char[1]
                char[1] = check_compound_jungseong(char[1:3])
                if temp_letter != char[1]:
                    char.pop(2)
            # Check for compound jongseong
            if len(char) >= 4 and char[2] in JONGSEONG_LIST and char[3] in JONGSEONG_LIST:
                temp_letter = char[2]
                char[2] = check_compound_jongseong(char[2:4])
                if temp_letter != char[2]:
                    char.pop(3)
    
    # Combine each character
    hangul_output = []
    for char in hangul_char:
        jongseong_index = 0
        if len(char) > 1 and char[0] in CHOSEONG_LIST and char[1] in JUNGSEONG_LIST:
            choseong_index = CHOSEONG_LIST.index(char.pop(0))
            jungseong_index = JUNGSEONG_LIST.index(char.pop(0))
            if len(char) > 0 and char[0] in JONGSEONG_LIST:
                jongseong_index = JONGSEONG_LIST.index(char.pop(0))
            character_code = 0xAC00 + (choseong_index * 21 * 28) + (jungseong_index * 28) + jongseong_index
            hangul_output.append(chr(character_code))
        while char:
            hangul_output.append(char.pop(0))

    return ''.join(hangul_output)

# Convert Dubeolsik to QWERTY
def hangul2alphabet(hangul_input):
    result = []
    for char in hangul_input:
        if '가' <= char <= '힣':
            char_code = ord(char) - 0xAC00
            choseong_index = char_code // (21 * 28)
            jungseong_index = (char_code % (21 * 28)) // 28
            jongseong_index = (char_code % (21 * 28)) % 28
            
            result.append(HANGUL_ALPHABET_MAPPING[CHOSEONG_LIST[choseong_index]])
            result.append(HANGUL_ALPHABET_MAPPING[JUNGSEONG_LIST[jungseong_index]])
            if jongseong_index != 0:
                result.append(HANGUL_ALPHABET_MAPPING[JONGSEONG_LIST[jongseong_index]])

        elif char in HANGUL_ALPHABET_MAPPING:
            result.append(HANGUL_ALPHABET_MAPPING[char])
        else:
            result.append(char)
    
    return ''.join(result)

# Check if input is in hangul or alphabet
def hangul_or_alphabet(input_str):
    def is_alphabet(char):
        return ('A' <= char <= 'Z') or ('a' <= char <= 'z')
    
    def is_hangul(char):
        unicode_value = ord(char)
        return (0xAC00 <= unicode_value <= 0xD7A3) or (0x1100 <= unicode_value <= 0x11FF) or (0x3130 <= unicode_value <= 0x318F)
    
    for char in input_str:
        if is_alphabet(char):
            return 'alphabet'
        elif is_hangul(char):
            return 'hangul'
    
    return 'not found'

# Main function
def hanyeongkey(input_str):
    if hangul_or_alphabet(input_str) == 'hangul':
        return hangul2alphabet(input_str)
    elif hangul_or_alphabet(input_str) == 'alphabet':
        return alphabet2hangul(input_str)
    else:
        return "This message cannot be converted. No hangul or alphabet found."

# Execute
repeat = True
while repeat:
    input_string = input("Enter the string to be converted: ")
    print(hanyeongkey(input_string))