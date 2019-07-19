class rotor():
    def __init__(self, scambling):
        self.o_unscambled = []
        for letter in scambling:
            letter_ascii = ord(letter.lower()) #convert to ascii
            self.o_unscambled.append(letter_ascii)


        unscarmbled = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ordinary = []
        for letter in unscarmbled:
            letter_ascii = ord(letter.lower()) #convert to ascii
            self.ordinary.append(letter_ascii)

        
    def input_fwd(self,i_num):
        i_num = self.ordinary[(i_num - 97)%26]
        output =  self.o_unscambled[ i_num - ord('a') ]

        return output

    def input_bwd(self, i_num):
        i_num = self.ordinary[(i_num - 97)%26]
        j = 0
        for i in self.o_unscambled:
            if i == i_num:
                break
            j+=1
        return j + 97


class EngimaMachine():
    #note rotations are in the anticlockwise direction
    def rotor1_Wiring(self, rotor1_Settings, change,i_pos = 0):
        self.c = i_pos;
        self.rotor1 = rotor(rotor1_Settings)

        self.change1 = ord( change[1].lower() )

    def rotor2_Wiring(self, rotor2_Settings , change, i_pos = 0):
        self.b = i_pos;
        self.rotor2 = rotor(rotor2_Settings)

        self.change2 = ord( change[1].lower() )

    def rotor3_Wiring(self, rotor3_Settings, change, i_pos = 0):
        self.a = i_pos;
        self.rotor3 = rotor(rotor3_Settings)

        self.change3 = ord( change[1].lower() )

    def plugBoard_Wiring(self, plugBoard_Settings):
        self.plugBoard = rotor(plugBoard_Settings)

    def reflector_Wiring(self, reflector_Settings):
        self.reflector = rotor(reflector_Settings)


    def input(self, i_num):
        #plugboard
        o_num = self.plugBoard.input_fwd(i_num)

        self.a+=1   #rotor3 always increments
        #rotor 3
        o_num = self.rotor3.input_fwd(o_num + self.a)
    
        if self.change3 == self.a+97:   #rotor 2 incrementation
            self.b+=1

        #rotor 2
        o_num = self.rotor2.input_fwd(o_num-self.a +self.b)
        
        if self.change2 == self.b+97:   #rotor 1 incrementation
            self.c+=1
        
        #rotor 1
        o_num = self.rotor1.input_fwd(o_num - self.b + self.c)

        #reflector
        o_num = self.reflector.input_fwd(o_num - self.c)

        #rotor 1
        o_num = self.rotor1.input_bwd(o_num + self.c)

        #rotor 2
        o_num = self.rotor2.input_bwd(o_num - self.c + self.b)

        #rotor 3
        o_num = self.rotor3.input_bwd(o_num - self.b + self.a)

        #plugboard
        o_num = self.plugBoard.input_fwd(o_num-self.a)  # fwd or bwd, doesn't matter

        
        return o_num
    

enigma = EngimaMachine()

# rotors, reflector and plugboard settings
enigma.rotor1_Wiring("EKMFLGDQVZNTOWYHXUSPAIBRCJ","QR",0)  #rotor I
enigma.rotor2_Wiring("AJDKSIRUXBLHWTMCQGZNPYFVOE","EF",0)  #rotor II
enigma.rotor3_Wiring("BDFHJLCPRTXVZNYEIWGAKMUSQO","VW",0)  #rotor III
enigma.plugBoard_Wiring("ABCDEFGHIJKLMNOPQRSTUVWXYZ")   #UNTOUCHED plugboard
enigma.reflector_Wiring("YRUHQSLDPXNGOKMIEBFZCWVJAT")   #Reflector B
#   ABCDEFGHIJKLMNOPQRSTUVWXYZ

message = "KPZFLUOETSTXLNBVHLSPEDJ"

for i in message:
    if i == ' ':
        continue
    i = i.lower()
    print( str(chr(enigma.input( ord(i) ))).upper() ,  end ="")



