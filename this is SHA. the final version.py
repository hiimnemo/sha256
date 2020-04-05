#sha v 3.0

#sha256 with addition modulo:
print("My 4rd program, fuck addition modulo... from the bottom of my heart")
test_str = input("enter the message to be hashed here: ")
if len(test_str) > 2**64/8:
    print("value to be hashed too long... FUCK YOU.")
    test_str=""
else:
    test_str=test_str
res = "".join(format(ord(i), 'b').rjust(8, "0") for i in test_str)
unpad_msg=str(res)
#print(unpad_msg)
len_of_unpad_msg=len(unpad_msg)
z=1
k=512*z - len_of_unpad_msg -65
if k < 0:
    for k in range(-512,0):
        z=z+1
        k=512*z - len_of_unpad_msg -65
        if k>0:
            break
    else:
        z=z
#ADD THE VALUE OF UNPADDED zeroes based on modules function.
bin_len_of_unpad_msg="{:b}".format(len_of_unpad_msg).rjust(64, "0")
pad_msg=unpad_msg+"1"+"".rjust(int(k), "0")+bin_len_of_unpad_msg
#print(pad_msg)
print(len(pad_msg))

i=0
part_of_512s=[pad_msg[0:512]]
if len(pad_msg)==512:
    part_of_512s=part_of_512s
else:
    while i < len(pad_msg):
        i=i+512
        part_of_512s=part_of_512s+[pad_msg[i:i+512]]
        if i > len(pad_msg)-512*2:
            break
# print(part_of_512s)

# 16 32 bit parts
def m(i,t):
    a=part_of_512s[i-1][32*t:32*t+32]
    return(a)

# FUNCTIONS:
def con_deci(a):
#a=input("the fuckin test string here, IN FUCKIN binary: ")
    len_digs=len(a)-1
    i=0
    x=0
    #print(a[0:1])
    #b=int(a[0:1])

    for i in range(0,len_digs+1):
        b=int(a[i:i+1])
        x=int(x)+((2**(len_digs-i))*b)
        i=i+1
    return(x)

#1. Ch(x,y,z): x, y, z IS IN STRING and OUTPUT IS IN INTEGER. im taking out the integer behind con_deci
def ch(x,y,z, total_len_of_the_message):
    z=(con_deci(x)&con_deci(y))^(~(con_deci(x))&(con_deci(z)))
    #y="{:b}".format(z).rjust(total_len_of_the_message, "0")
    return(z)

#a="{:b}".format(ch("1011","1000", "1110"))
#print(a)
#2. Maj(x,y,z):
def maj(x,y,z, total_len_of_the_message):
    z=(((con_deci(x)&con_deci(y)))^(con_deci(x)&con_deci(z))^(con_deci(y)&con_deci(z)))
    #y="{:b}".format(z).rjust(total_len_of_the_message, "0")
    return(z)


#3. >> function:output string
def right_shift(n, x, total_len_of_the_message):
    z=x[0:len(x)-n].rjust(total_len_of_the_message, "0")
    return(z)

#4. << function: output str
def left_shift(n, x, total_len_of_the_message):
    z=x[n:len(x)].ljust(total_len_of_the_message, "0")
    return(z)


#5.LOTRn(x) output = str input is in n=int, x= str, total_len_of_the_message= int
def rotl(n, x, total_len_of_the_message):
    dec_after_leftshift=con_deci(str(left_shift(n, x, total_len_of_the_message)))
    dec_after_rightshift=con_deci(str(right_shift(len(x)-n, x, total_len_of_the_message)))
    z=dec_after_leftshift|dec_after_rightshift
    y="{:b}".format(z).rjust(total_len_of_the_message, "0")
    return(y)


#5.ROTRn(x) output = str input is in n=int, x= str, total_len_of_the_message= int
def rotr(n, x, total_len_of_the_message):
    dec_after_rightshift=con_deci(str(right_shift(n, x, total_len_of_the_message)))
    dec_after_leftshift=con_deci(str(left_shift(len(x)-n, x, total_len_of_the_message)))
    z=dec_after_leftshift|dec_after_rightshift
    y="{:b}".format(z).rjust(total_len_of_the_message, "0")
    return(y)
#6. shr= basically it is x>>n
def shr(n, x, total_len_of_the_message):
    a=right_shift(n, x, total_len_of_the_message)
    return(a)
    
#7.cap sigma 0 to 256:
def cap_sigma_0_256(x, total_len_of_the_message):
    a=rotr(2, x, total_len_of_the_message)
    b=rotr(13, x, total_len_of_the_message)
    c=rotr(22, x, total_len_of_the_message)
    d=con_deci(a)^con_deci(b)^con_deci(c)
    #a=(con_deci(str(rotr(2, x, total_len_of_the_message)))^con_deci(str(rotr(13, x, total_len_of_the_message)))^con_deci(str(rotr(22, x, total_len_of_the_message))))
    #b="{:b}".format(a).rjust(total_len_of_the_message, "0")
    return(d)

#8. cap sig
def cap_sigma_1_256(x, total_len_of_the_message):
    a=rotr(6, x, total_len_of_the_message)
    b=rotr(11, x, total_len_of_the_message)
    c=rotr(25, x, total_len_of_the_message)
    d=con_deci(a)^con_deci(b)^con_deci(c)
    #a=(con_deci(str(rotr(6, x, total_len_of_the_message)))^con_deci(str(rotr(11, x, total_len_of_the_message)))^con_deci(str(rotr(25, x, total_len_of_the_message))))
    #b="{:b}".format(a).rjust(total_len_of_the_message, "0")
    return(d)
#9.
def small_sigma_0_256(x, total_len_of_the_message):
    a=rotr(7, x, total_len_of_the_message)
    b=rotr(18, x, total_len_of_the_message)
    c=shr(3, x, total_len_of_the_message)
    d=con_deci(a)^con_deci(b)^con_deci(c)
    #a=(con_deci(str(rotr(7, x, total_len_of_the_message)))^con_deci(str(rotr(18, x, total_len_of_the_message)))^con_deci(str(shr(3, x, total_len_of_the_message))))
    #b="{:b}".format(a).rjust(total_len_of_the_message, "0")
    return(d)
#10.
def small_sigma_1_256(x, total_len_of_the_message):
    a=rotr(17, x, total_len_of_the_message)
    b=rotr(19, x, total_len_of_the_message)
    c=shr(10, x, total_len_of_the_message)
    d=con_deci(a)^con_deci(b)^con_deci(c)
    #a=(con_deci(str(rotr(17, x, total_len_of_the_message)))^con_deci(str(rotr(19, x, total_len_of_the_message)))^con_deci(str(shr(10, x, total_len_of_the_message))))
    #b="{:b}".format(a).rjust(total_len_of_the_message, "0")
    return(d)
#11.
def con_hex_to_deci(a):
#a=input("the fuckin test string here, IN FUCKIN binary: ")
    len_digs=len(a)-1
    i=0
    x=0
    #print(a[0:1])
    #b=(a[0:1])

    for i in range(0,len_digs+1):
        b=a[i:i+1]
        if b=="a":
            b=10
        elif b=="b":
            b=11
        elif b=="c":
            b=12
        elif b=="d":
            b=13
        elif b=="e":
            b=14
        elif b=="f":
            b=15
        x=int(x)+((16**(len_digs-i))*int(b))
        i=i+1
    
   
    return(x)

#12. conversion of hex to bin:
def con_hex_to_bin(a, total_len_of_the_message):
#a=input("the fuckin test string here, IN FUCKIN binary: ")
    len_digs=len(a)-1
    i=0
    x=0
    #print(a[0:1])
    #b=(a[0:1])

    for i in range(0,len_digs+1):
        b=a[i:i+1]
        if b=="a":
            b=10
        elif b=="b":
            b=11
        elif b=="c":
            b=12
        elif b=="d":
            b=13
        elif b=="e":
            b=14
        elif b=="f":
            b=15
        x=int(x)+((16**(len_digs-i))*int(b))
        i=i+1
    
    y= "{:b}".format(x).rjust(total_len_of_the_message, "0")
   
    return(y)

#13.
def addition_modulo_2_32(x, y):
    a=x+y
    i=1
    if a < 2**32:
        a=x+y
        return(a)
    
    elif a == 2**32:
        a=0
        return(a)
    
    elif a > 2**32 :
        while a > 2**32:
            a=(x+y)-((2**32)*i)
            i=i+1
            if a%(2**32) == 0:
                a=0
                return(a)
        return(a)
#14. 
def addition_modulo_2_32_4(a, b, c, d):
    x=addition_modulo_2_32(addition_modulo_2_32(addition_modulo_2_32(a, b), c), d)
    return(x)

#15. AND FUCK YOU FOR DOING THIS TO ME. U MADE ME CHANGE how to con hex to bin.. WORDS IT SEEMS.. FUCK YOU.
def con_8hex_to_32bitwords(a):
    x=str(con_hex_to_bin(a[0:1], 4))+str(con_hex_to_bin(a[1:2], 4))+str(con_hex_to_bin(a[2:3], 4))+str(con_hex_to_bin(a[3:4], 4))+str(con_hex_to_bin(a[4:5], 4))+str(con_hex_to_bin(a[5:6], 4))+str(con_hex_to_bin(a[6:7], 4))+str(con_hex_to_bin(a[7:8], 4))
    return(x)

#16.
#. how to convert 8 hex digits to 32 bit word LISTS. FML
def con_list_8hex_to_32bit(a):
    i=0
    x=[]
    while i in range(0, len(a)):
        x=x+[con_8hex_to_32bitwords(a[i])]
        i=i+1
    return(x)

#initialize 8 hash variables.
h_0="6a09e667"
h_1="bb67ae85"
h_2="3c6ef372"
h_3="a54ff53a"
h_4="510e527f"
h_5="9b05688c"
h_6="1f83d9ab"
h_7="5be0cd19"
initial_hash=[h_0, h_1, h_2, h_3, h_4, h_5, h_6, h_7]
#initial_hash_32bin=[con_8hex_to_32bitwords(h_0), con_8hex_to_32bitwords(h_1)]  i m gonna define it





#initialize k(t) constants:
k_t=["428a2f98", "71374491", "b5c0fbcf", "e9b5dba5", "3956c25b", "59f111f1", "923f82a4", "ab1c5ed5", "d807aa98", "12835b01", "243185be", "550c7dc3", "72be5d74", "80deb1fe", "9bdc06a7", "c19bf174", "e49b69c1", "efbe4786", "0fc19dc6", "240ca1cc", "2de92c6f", "4a7484aa", "5cb0a9dc", "76f988da", "983e5152", "a831c66d", "b00327c8", "bf597fc7", "c6e00bf3", "d5a79147", "06ca6351", "14292967", "27b70a85", "2e1b2138", "4d2c6dfc", "53380d13", "650a7354", "766a0abb", "81c2c92e", "92722c85", "a2bfe8a1", "a81a664b", "c24b8b70", "c76c51a3", "d192e819", "d6990624", "f40e3585", "106aa070", "19a4c116", "1e376c08", "2748774c", "34b0bcb5", "391c0cb3", "4ed8aa4a", "5b9cca4f", "682e6ff3", "748f82ee", "78a5636f", "84c87814", "8cc70208", "90befffa", "a4506ceb", "bef9a3f7", "c67178f2"]
def k(t):
    x=k_t[t]
    return(x)

initial_hash_32bin=con_list_8hex_to_32bit(initial_hash)
# print(initial_hash_32bin, "32 bin initial hash")
k_t_32bitbin=con_list_8hex_to_32bit(k_t)
# print(k_t_32bitbin, "k_t_32bitbin")
# print(con_deci(initial_hash_32bin[0]))

#for i in range(0, len(part_of_512s)):
#REMEMBER TO PUT " for i in range(0, len(part_of_512s)):" here. AND FROM HERE CAREFUL ON USING VARIBLES.
total_len_of_the_message=32
t=0
i=1
empty_set=[]
#i=1
def making_a_list(x, y):
    i=0
    a=[]
    while i < y:
        a=a+[x+i]
        i=i+1
        if i==(y-x):
            break
    return(a)
#Now the actual operations:
#1. defining w(t):
for t in making_a_list(0,16):
    i=1
    x=m(i, t)
            #t=t+1
    empty_set=empty_set+[con_deci(x)]
    t=t+1
# print(t, "value of t after 16 cycles")
# print("enpty set after 16 cycles: ", empty_set, len(empty_set))

#making list. I DONT BELIVE in range anymore.


while t in making_a_list(16, 64):
    empty_set=empty_set+[addition_modulo_2_32_4(small_sigma_1_256("{:b}".format(empty_set[t-2]).rjust(32, "0"), 32), empty_set[t-7], small_sigma_0_256("{:b}".format(empty_set[t-15]).rjust(32, "0"), 32), empty_set[t-16])]
    t=t+1
    #if t==18:
        #break
    

w=empty_set
# print(w, "W(t)", len(w))
n=[]
for l in range(0, 64):
    n=n+["{:b}".format(w[l]).rjust(32, "0"), l+1]
    l=l+1

# print(m)
# print('w(t) value is perfect.')

#print(empty_set, len(empty_set))
## purrfect.

#2. defining 8 working variables.
a=con_deci(initial_hash_32bin[0])
b=con_deci(initial_hash_32bin[1])
c=con_deci(initial_hash_32bin[2])
d=con_deci(initial_hash_32bin[3])
e=con_deci(initial_hash_32bin[4])
f=con_deci(initial_hash_32bin[5])
g=con_deci(initial_hash_32bin[6])
h=con_deci(initial_hash_32bin[7])
# print(a)

#3. bullshit additions..WAIT Modulo additions.. FUCK YOU AGAIN.
list_of_sub_hashes=[a, b, c, d, e, f, g, h]  #this is in decimals.
# print(list_of_sub_hashes, "initial hashes")
t=0
value_of_t1=[]
value_of_t2=[]
while t in making_a_list(0,64):
    t_1= addition_modulo_2_32(addition_modulo_2_32_4(list_of_sub_hashes[7], cap_sigma_1_256("{:b}".format(list_of_sub_hashes[4]).rjust(32, "0"), 32), ch("{:b}".format(list_of_sub_hashes[4]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[5]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[6]).rjust(32, "0"), 32), con_deci(k_t_32bitbin[t])), w[t])
    t_2=addition_modulo_2_32(cap_sigma_0_256("{:b}".format(list_of_sub_hashes[0]).rjust(32, "0"), 32), maj("{:b}".format(list_of_sub_hashes[0]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[1]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[2]).rjust(32, "0"), 32))
    h=list_of_sub_hashes[6]
    g=list_of_sub_hashes[5]
    f=list_of_sub_hashes[4]
    e=addition_modulo_2_32(list_of_sub_hashes[3], t_1)
    d=list_of_sub_hashes[2]
    c=list_of_sub_hashes[1]
    b=list_of_sub_hashes[0]
    a=addition_modulo_2_32(t_1, t_2)
    value_of_t1=value_of_t1+[t_1]
    value_of_t2=value_of_t2+[t_2]
    
    list_of_sub_hashes=[a, b, c, d, e, f, g, h]
    t=t+1
   
    #if t==1:
        #break
    
 
# print(value_of_t1, "t_1s")
# print(value_of_t2, "t_2s") 
# print(list_of_sub_hashes[0], "value of a after round 64")  
list_of_sub_hashes=[a, b, c, d, e, f, g, h]
# print(list_of_sub_hashes) #THANK THE ONE TRUE GOD.. RNG GOD. xD

FINAL_HASH_1=(addition_modulo_2_32(list_of_sub_hashes[0], con_hex_to_deci(initial_hash[0])))
FINAL_HASH_2=(addition_modulo_2_32(list_of_sub_hashes[1], con_hex_to_deci(initial_hash[1])))
FINAL_HASH_3=(addition_modulo_2_32(list_of_sub_hashes[2], con_hex_to_deci(initial_hash[2])))
FINAL_HASH_4=(addition_modulo_2_32(list_of_sub_hashes[3], con_hex_to_deci(initial_hash[3])))
FINAL_HASH_5=(addition_modulo_2_32(list_of_sub_hashes[4], con_hex_to_deci(initial_hash[4])))
FINAL_HASH_6=(addition_modulo_2_32(list_of_sub_hashes[5], con_hex_to_deci(initial_hash[5])))
FINAL_HASH_7=(addition_modulo_2_32(list_of_sub_hashes[6], con_hex_to_deci(initial_hash[6])))
FINAL_HASH_8=(addition_modulo_2_32(list_of_sub_hashes[7], con_hex_to_deci(initial_hash[7])))

#("{:b}".format(FINAL_HASH_1st_part).rjust(32, "0"))
# print("{:x}".format(FINAL_HASH_1)+"{:x}".format(FINAL_HASH_2)+"{:x}".format(FINAL_HASH_3)+"{:x}".format(FINAL_HASH_4)+"{:x}".format(FINAL_HASH_5)+"{:x}".format(FINAL_HASH_6)+"{:x}".format(FINAL_HASH_7)+"{:x}".format(FINAL_HASH_8))
# print(len("{:x}".format(FINAL_HASH_1)+"{:x}".format(FINAL_HASH_2)+"{:x}".format(FINAL_HASH_3)+"{:x}".format(FINAL_HASH_4)+"{:x}".format(FINAL_HASH_5)+"{:x}".format(FINAL_HASH_6)+"{:x}".format(FINAL_HASH_7)+"{:x}".format(FINAL_HASH_8)))
# #print(FINAL_HASH_1, len(str(256_hash))
# #nope i m not getting the required hash. we shall call this RAM-256 hash
    

# DONE FOR 512 BITS of a message.
# next is sha256 v4.0. the final version
i=2
empty_set=[]
while i in range(2, len(part_of_512s)+1):
    # starting the algo from first
    #1. defining w(t):
    # x=""
    empty_set=[]
    for t in range(0,16):
        # x=m
        # i=1
        x=m(i, t)
            #t=t+1
        empty_set=empty_set+[con_deci(x)]
        t=t+1
    # print(t, "value of t after 16 cycles")
    # print("enpty set after 16 cycles: ", empty_set, len(empty_set))
        
#making list. I DONT BELIVE in range anymore.

    
    while t in range(16, 64):
        empty_set=empty_set+[addition_modulo_2_32_4(small_sigma_1_256("{:b}".format(empty_set[t-2]).rjust(32, "0"), 32), empty_set[t-7], small_sigma_0_256("{:b}".format(empty_set[t-15]).rjust(32, "0"), 32), empty_set[t-16])]
        t=t+1
    
    w=empty_set
    # print(w, i)
    # print(w, "W(t)", len(w))
    # n=[]
    # for l in range(0, 64):
    # #     n=n+["{:b}".format(w[l]).rjust(32, "0"), l+1]
    # #     # l=l+1
    #defining 8 working variables
    #2. defining 8 working variables.
    a=FINAL_HASH_1
    b=FINAL_HASH_2
    c=FINAL_HASH_3
    d=FINAL_HASH_4
    e=FINAL_HASH_5
    f=FINAL_HASH_6
    g=FINAL_HASH_7
    h=FINAL_HASH_8
    # print(a)
    list_of_sub_hashes=[a, b, c, d, e, f, g, h]
    # print(list_of_sub_hashes, i)
    
    t=0
    value_of_t1=[]
    value_of_t2=[]
    while t in making_a_list(0,64):
        t_1= addition_modulo_2_32(addition_modulo_2_32_4(list_of_sub_hashes[7], cap_sigma_1_256("{:b}".format(list_of_sub_hashes[4]).rjust(32, "0"), 32), ch("{:b}".format(list_of_sub_hashes[4]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[5]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[6]).rjust(32, "0"), 32), con_deci(k_t_32bitbin[t])), w[t])
        t_2=addition_modulo_2_32(cap_sigma_0_256("{:b}".format(list_of_sub_hashes[0]).rjust(32, "0"), 32), maj("{:b}".format(list_of_sub_hashes[0]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[1]).rjust(32, "0"), "{:b}".format(list_of_sub_hashes[2]).rjust(32, "0"), 32))
        h=list_of_sub_hashes[6]
        g=list_of_sub_hashes[5]
        f=list_of_sub_hashes[4]
        e=addition_modulo_2_32(list_of_sub_hashes[3], t_1)
        d=list_of_sub_hashes[2]
        c=list_of_sub_hashes[1]
        b=list_of_sub_hashes[0]
        a=addition_modulo_2_32(t_1, t_2)
        value_of_t1=value_of_t1+[t_1]
        value_of_t2=value_of_t2+[t_2]
    
        list_of_sub_hashes=[a, b, c, d, e, f, g, h]
        t=t+1
    
    FINAL_HASH_1=(addition_modulo_2_32(list_of_sub_hashes[0], FINAL_HASH_1))
    FINAL_HASH_2=(addition_modulo_2_32(list_of_sub_hashes[1], FINAL_HASH_2))
    FINAL_HASH_3=(addition_modulo_2_32(list_of_sub_hashes[2], FINAL_HASH_3))
    FINAL_HASH_4=(addition_modulo_2_32(list_of_sub_hashes[3], FINAL_HASH_4))
    FINAL_HASH_5=(addition_modulo_2_32(list_of_sub_hashes[4], FINAL_HASH_5))
    FINAL_HASH_6=(addition_modulo_2_32(list_of_sub_hashes[5], FINAL_HASH_6))
    FINAL_HASH_7=(addition_modulo_2_32(list_of_sub_hashes[6], FINAL_HASH_7))
    FINAL_HASH_8=(addition_modulo_2_32(list_of_sub_hashes[7], FINAL_HASH_8))
    
    # print(FINAL_HASH_1, FINAL_HASH_2, FINAL_HASH_3, FINAL_HASH_4, FINAL_HASH_5, FINAL_HASH_6, FINAL_HASH_7, FINAL_HASH_8, i)
    
    i=i+1
    # if i == (len(part_of_512s)+1):
    #     break
    
print("{:x}".format(FINAL_HASH_1).rjust(8, "0")+"{:x}".format(FINAL_HASH_2).rjust(8, "0")+"{:x}".format(FINAL_HASH_3).rjust(8, "0")+"{:x}".format(FINAL_HASH_4).rjust(8, "0")+"{:x}".format(FINAL_HASH_5).rjust(8, "0")+"{:x}".format(FINAL_HASH_6).rjust(8, "0")+"{:x}".format(FINAL_HASH_7).rjust(8, "0")+"{:x}".format(FINAL_HASH_8).rjust(8, "0"))
print("THIS COMPLETES SHA256. COMPLETELY. ONCE AND FOR ALL.")