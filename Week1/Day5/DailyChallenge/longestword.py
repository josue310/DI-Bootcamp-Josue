def longest_word(phrase):
    p = phrase
    t_p = p.split()
    l_mot = t_p[0]
    for mot in t_p:
        if len(mot) > len(l_mot):
            l_mot = mot
    return f"longest_word({p}) ➞ {l_mot}"

longest_word("Forgetfulness is by all means powerless!")