complex_table=[
 (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), 
 (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), 
 (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), 
 (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), 
 (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), 
 (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), 
 (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), 
 (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), 
 (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), 
 (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), 
 (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), 
 (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), 
 (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), 
 (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), 
 (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), 
 (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j)]
def convert(d):
    e=[]
    for i in range(int(len(d)/2)):
        num1 = int(d[i*2])
        if (num1 ==0): num1=-1
        num2 = int(d[i*2+1])
        if (num2 ==0): num2=-1
        e.append(complex(num1,num2))
    return e


signal_table16=['0011111000100101',
              '0100111110001001',
              '0101001111100010',
              '1001010011111000',
              '0010010100111110',
              '1000100101001111',
              '1110001001010011',
              '1111100010010100',
              '0110101101110000',
              '0001101011011100',
              '0000011010110111',
              '1100000110101101',
              '0111000001101011',
              '1101110000011010',
              '1011011100000110',
              '1010110111000001',]
signal_table8=['00010101',
                '00010110',
                '00011001',
                '00011010',
                '00100101',
                '00100110',
                '00101001',
                '00101010',
                '11010101',
                '11010110',
                '11011001',
                '11011010',
                '11100101',
                '11100110',
                '11101001',
                '11101010']
signal_table64=[
                '1101100111000011010100100010111011011001110000110101001000101110',
                '1110110110011100001101010010001011101101100111000011010100100010',
                '0010111011011001110000110101001000101110110110011100001101010010',
                '0010001011101101100111000011010100100010111011011001110000110101',
                '0101001000101110110110011100001101010010001011101101100111000011',
                '0011010100100010111011011001110000110101001000101110110110011100',
                '1100001101010010001011101101100111000011010100100010111011011001',
                '1001110000110101001000101110110110011100001101010010001011101101',
                '1000110010010110000001110111101110001100100101100000011101111011',
                '1011100011001001011000000111011110111000110010010110000001110111',
                '0111101110001100100101100000011101111011100011001001011000000111',
                '0111011110111000110010010110000001110111101110001100100101100000',
                '0000011101111011100011001001011000000111011110111000110010010110',
                '0110000001110111101110001100100101100000011101111011100011001001',
                '1001011000000111011110111000110010010110000001110111101110001100',
                '1100100101100000011101111011100011001001011000000111011110111000'
                ]
complex_table16=[]
complex_table8= []
complex_table64=[]
for i in range(16):
    #print(bin(i)[2:])
    f = str(bin(i)[2:])
    if (len(f)<4) :
        f = '0'*(4-len(f)) +f
    #print(f)
    f = f[::-1]
    f = int(f,2)
    complex_table16 += convert(signal_table16[f])
    complex_table8 += convert(signal_table8[f])
    complex_table64 += convert(signal_table64[f])
print("16",complex_table16)
print("8",complex_table8)
print("64",complex_table64)

