


def lineup_students(string):
    if len(string) < 1:
        return []
    print(sorted(sorted(string.split(" "), reverse=True),reverse=True, key=len))
    # print(sorted(sorted(string.split(" "), reverse=True, key=len), reverse=True))
    return sorted(sorted(string.split(" "), reverse=True),reverse=True, key=len)


lineup_students('Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi')
lineup_students("xxa xxb xxc xxd xa xb xc xd")
lineup_students("")

