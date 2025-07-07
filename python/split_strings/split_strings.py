#!/usr/bin/python3

def solution(s: str) -> list[str]:
    result = []

    if len(s) % 2:
        s += "_"

    for i in range(0, len(s), 2):
        result.append(s[i:i+2])

    return result

if __name__ == "__main__":
    print(solution("abced"))
