def solution(s):
    answer = len(s)
    for length in range(1, len(s)//2+1):
        zipped_str = ''
        last = s[0:length]
        this = ''
        cnt = 1
        for idx in range(length, len(s)+length, length):
            this = s[idx:idx+length]
            if last == this:
                cnt += 1
            else:
                if cnt > 1:
                    zipped_str += str(cnt) + last
                    cnt = 1
                else:
                    zipped_str += last
                last = this

        answer = min(len(zipped_str), answer)
    return answer
