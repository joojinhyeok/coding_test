def solution(letter):
    answer = ''
    # 모스부호 매핑
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    # split 활용해서 letter를 쪼갬 
    morse_list = letter.split(' ')
    
    # morse_list 순회하면서 매핑된 문자로 바꾸기
    for i in morse_list:
        answer += morse[i]
    return answer