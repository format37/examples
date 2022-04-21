from datetime import datetime

# Дано число 100 в двоичной системе, у калькулятора есть две программы :
# прибавить 1 и слева добавить 1 , надо получить 110001,тоже в двоичной

# pypy:
# wget https://downloads.python.org/pypy/pypy3.9-v7.3.8-linux64.tar.bz2
#  sudo tar xf pypy3.9-v7.3.8-linux64.tar.bz2 -C /opt
# /opt/pypy3.9-v7.3.8-linux64/bin/pypy ege01.py

def to_bin(i,lead_zero_count = 0):
    clear_bin = bin(i)[2:]
    if lead_zero_count:
        lead_zeros = ''.join(['0' for z in range(lead_zero_count-len(clear_bin))])
    else:
        lead_zeros = ''
    return lead_zeros+clear_bin
    
def to_dec(value):
    return int(value,2)

def win_counter(start, end, debug = False):    
    
    dec_start = to_dec(start)    
    dec_end = to_dec(end)
    
    # get combinations count
    a = to_dec(start)
    combinations_count = ''
    while a<dec_end:
        a+=1
        combinations_count+='1'    
    
    # walk over all combinations
    comb_len = dec_end-dec_start
    combinations_count_dec = to_dec(combinations_count)+1
    print('comb_len', comb_len)
    print('combinations_count_dec', combinations_count_dec)    
    win_combs = set()
    last_combs_len = len(win_combs)
    for i in range(combinations_count_dec):
        val = dec_start
        comb = to_bin(i,comb_len)
        len_counter = 0
        for c in reversed(comb):
            len_counter += 1
            if c=='1':
                val+=1
            else:
                val_bin = to_bin(val)
                val_bin = '1'+val_bin
                val = to_dec(val_bin)
            
            if val>=dec_end:
                break
        if val==dec_end:
            win_combs.add(comb[-len_counter:])
            
            if debug and not len(win_combs)==last_combs_len:
                print(i, len(win_combs), val, to_bin(val), len_counter, comb[-len_counter:])
            last_combs_len = len(win_combs)

    return win_combs

start = '100'
end = '110001'

print(start,end)
print(to_dec(start),to_dec(end))
start_time = datetime.now()
print(start_time)
w = win_counter(start, end, True)
end_time = datetime.now()
print(end_time)
print(end_time-start_time)
print(len(w))
