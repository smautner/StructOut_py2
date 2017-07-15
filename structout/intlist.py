
import math



#############
# NUMBER DECORATOR
#############

colorscheme={
        0:0,
        1:0,
        2:4,
        3:4,
        4:1,
        5:1,
        6:3,
        7:3,
        '.':0
        }

def compress_int(i):
    '''
    :param i:  INTEGER
    :return:
        0 -> .
        1-9 -> 1-9
        10+  -> A+
    '''
    if i < 1:
        return '.'
    else:
        z= int(math.log(i,2))
        return z if z <=9 else chr(z+55)


def colorize_symbol(symbol, col):
    '''http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python'''
    return '\x1b[1;3%d;48m%s\x1b[0m' % (col, symbol)



def decorate_number(num):
    '''
    :param num:  integer
    :return:
        string, that integer in COMPRESSED and colored
    '''
    num =compress_int(num)
    return colorize_symbol (str(num), colorscheme.get(num, 8))




def resize(values, desired_length):
    length=len(values)
    size= float(length)/desired_length
    values = [  max(values[ int(i*size): int(math.ceil((i+1)*size))   ] )  for i in xrange(desired_length)]
    return values


def positiondict_to_list(positiondict):
    maxx =max(positiondict)
    minn =min(positiondict)
    return [ positiondict.get(a,0) for a in range(minn,maxx+1)]



def positiondict_to_printable(pdict,dlength):
    ret = map(decorate_number, resize( positiondict_to_list(pdict),desired_length=dlength ))
    return ''.join(ret)



def display(region, disp_length=200):
    info ="| %d \t %s" % (region.end-region.start,str(region) )

    if region.piles:
        print positiondict_to_printable(region.piles,disp_length)

    if region.pvalues:
        print positiondict_to_printable(region.pvalues,disp_length)
    print info



