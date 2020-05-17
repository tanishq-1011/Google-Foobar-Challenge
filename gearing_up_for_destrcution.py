from fractions import Fraction  

def solution(pegs):
    lgt = len(pegs)
    if ((not pegs) or lgt == 1):
        return [-1,-1]

    evt = True if (lgt % 2 == 0) else False
    s = (- pegs[0] + pegs[lgt - 1]) if evt else (- pegs[0] - pegs[lgt -1])

    if (lgt > 2):
        for i in xrange(1, lgt-1):
            s += 2 * (-1)**(i+1) * pegs[i]

    fgr = Fraction(2 * (float(s)/3 if evt else s)).limit_denominator()


    crs = fgr
    for i in xrange(0, lgt-2):
        cd = pegs[i+1] - pegs[i]
        nes = cd - crs
        if (crs < 1 or nes < 1):
            return [-1,-1]
        else:
            crs = nes

    return [fgr.numerator, fgr.denominator]
