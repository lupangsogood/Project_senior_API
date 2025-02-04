from Lips_Eyeliner_Makeup.apply_makeup import ApplyMakeup
from Brush_Makeup.blush import BrushMakeup_class
from Lip_Makeup.lipstick import LipMakeup_class
from Eyebrown_Makeup.eyebrown import Eyebrown_Makeup_class
import cv2
import os
import base64


class simulate_makeup():

    def __init__(self):
        self.path = 0
        self.Rb = 0
        self.Gb = 0
        self.Bb = 0
        self.Rl = 0
        self.Gl = 0
        self.Bl = 0
        self.eyeBrowL = 0
        self.eyeBrowR = 0


    def brush_color(self,type_id,style_id):
       
        if type_id == "1":
            if style_id == "1":
                self.Rb = 131
                self.Gb = 86
                self.Bb = 101

                self.eyeBrowR = "1_1_R.jpg"
                self.eyeBrowL = "1_1_L.jpg"
            elif style_id =="2":
                self.Rb = 223
                self.Gb = 169
                self.Bb = 144

                self.eyeBrowR = "1_2_R.jpg"
                self.eyeBrowL = "1_2_L.jpg"
            elif style_id =="3":
                self.Rb = 196
                self.Gb = 119
                self.Bb = 133

                self.eyeBrowR = "1_3_R.jpg"
                self.eyeBrowL = "1_3_L.jpg"
        elif type_id == "2":
                if style_id =="1":
                    self.Rb = 192
                    self.Gb = 131
                    self.Bb = 114

                    self.eyeBrowR = "2_1_R.jpg"
                    self.eyeBrowL = "2_1_L.jpg"
                elif style_id =="2":
                    self.Rb = 194
                    self.Gb = 133
                    self.Bb = 218

                    self.eyeBrowR = "2_2_R.jpg"
                    self.eyeBrowL = "2_2_L.jpg"
                elif style_id =="3":
                    self.Rb = 252
                    self.Gb = 177
                    self.Bb = 147

                    self.eyeBrowR = "2_3_R.jpg"
                    self.eyeBrowL = "2_3_L.jpg"
        elif type_id == "3":
                if style_id =="1":
                    self.Rb = 252
                    self.Gb = 187
                    self.Bb = 154

                    self.eyeBrowR = "3_1_R.jpg"
                    self.eyeBrowL = "3_1_L.jpg"
                elif style_id =="2":
                    self.Rb = 184
                    self.Gb = 117
                    self.Bb = 122

                    self.eyeBrowR = "3_2_R.jpg"
                    self.eyeBrowL = "3_2_L.jpg"
                elif style_id =="3":
                    self.Rb = 177
                    self.Gb = 105
                    self.Bb = 104

                    self.eyeBrowR = "3_3_R.jpg"
                    self.eyeBrowL = "3_3_L.jpg"
        elif type_id == "4":
                if style_id =="1":
                    self.Rb = 193
                    self.Gb = 121
                    self.Bb = 77

                    self.eyeBrowR = "4_1_R.jpg"
                    self.eyeBrowL = "4_1_L.jpg"
                elif style_id =="2":
                    self.Rb = 238
                    self.Gb = 180
                    self.Bb = 162

                    self.eyeBrowR = "4_2_R.jpg"
                    self.eyeBrowL = "4_2_L.jpg"
                elif style_id =="3":
                    self.Rb = 240
                    self.Gb = 157
                    self.Bb = 152

                    self.eyeBrowR = "4_3_R.jpg"
                    self.eyeBrowL = "4_3_L.jpg"
        else:
            self.Rb = 0
            self.Gb = 0
            self.Bb = 0

    def lipstick_color(self,type_id,style_id):

        if type_id == "1":
            if style_id == "1":
                self.Rl = 107
                self.Gl = 65
                self.Bl = 77
            elif style_id =="2":
                self.Rl = 215
                self.Gl = 140
                self.Bl = 151
            elif style_id =="3":
                self.Rl = 174
                self.Gl = 38
                self.Bl = 51
        elif type_id == "2":
                if style_id =="1":
                    self.Rl = 175
                    self.Gl = 65
                    self.Bl = 68
                elif style_id =="2":
                    self.Rl = 177
                    self.Gl = 109
                    self.Bl = 162
                elif style_id =="3":
                    self.Rl = 188
                    self.Gl = 82
                    self.Bl = 80
        elif type_id == "3":
                if style_id =="1":
                    self.Rl = 253
                    self.Gl = 163
                    self.Bl = 142
                elif style_id =="2":
                    self.Rl = 184
                    self.Gl = 117
                    self.Bl = 122
                elif style_id =="3":
                    self.Rl = 151
                    self.Gl = 84
                    self.Bl = 64
        elif type_id == "4":
                if style_id =="1":
                    self.Rl = 250
                    self.Gl = 135
                    self.Bl = 156
                elif style_id =="2":
                    self.Rl = 221
                    self.Gl = 135
                    self.Bl = 135
                elif style_id =="3":
                    self.Rl = 174
                    self.Gl = 46
                    self.Bl = 61
        else:
            self.Rl = 0
            self.Gl = 0
            self.Bl = 0

 
    def get_makeup(self,imagepath,type_id,style_id):

        self.brush_color(type_id,style_id)
        self.lipstick_color(type_id,style_id)
        path_eyebrown_L = os.path.join("C:\\Users\\comsc\\AppData\\Local\Programs\\Python\\Python36\\Project_senior\\drawable", self.eyeBrowL)
        path_eyebrown_R = os.path.join("C:\\Users\\comsc\\AppData\\Local\Programs\\Python\\Python36\\Project_senior\\drawable", self.eyeBrowR)
        Rb = self.Rb
        Gb = self.Gb
        Bb = self.Bb

        Rl = self.Rl
        Gl = self.Gl
        Bl = self.Bl
        #------------------------- CHECK PATH AFTER GIT PULL ----------------------------------#
        #-----------------------FOR NOTE_BOOK --------------------------------------------------#
        '''
        path_image = 'C:\\Users\\ANUSIT\\Anaconda3\\envs\\opencv-env\\Project_senior\\Project_senior\\images_input\\input14.jpg'
        print(path_image)
        path_eyebrown_R = 'C:\\Users\\ANUSIT\\Anaconda3\\envs\\opencv-env\\Project_senior\\Project_senior\\drawable\\testjangmakR1.jpg'
        path_eyebrown_L = 'C:\\Users\\ANUSIT\\Anaconda3\\envs\\opencv-env\\Project_senior\\Project_senior\\drawable\\testjangmakL1.jpg'
            '''
        #----------------------------------FOR COMPUTER_SERVER ----------------------------------------#
        #path_image = 'C:\\Users\\comsc\\AppData\\Local\\Programs\\Python\\Python36\\Project_senior\\images_intput\\input14.jpg'
        path_eyebrown_R = path_eyebrown_R
        path_eyebrown_L = path_eyebrown_L

        self.image_path = imagepath
        print(self.image_path)

        AM = ApplyMakeup()
        BM = BrushMakeup_class()
        LM = LipMakeup_class()
        EM = Eyebrown_Makeup_class()


        abs_path = 'C:\\Users\\comsc\\AppData\\Local\\Programs\\Python\\Python36\\Project_senior\\tmp_images\\'
        UPLOAD_FOLDER = 'C:\\Users\\comsc\\AppData\\Local\\Programs\\Python\\Python36\\Project_senior\\images_output'        
        output_file1 = AM.apply_liner(self.image_path)
        output_file2 = BM.apply_brush((abs_path+output_file1),Rb,Gb,Bb)
        output_file3 = LM.apply_lipstick_func((abs_path+output_file2),Rl,Gl,Bl)
        output_file4 = EM.apply_Eyebrown((abs_path+output_file3),path_eyebrown_R,path_eyebrown_L)
    
        img_result = cv2.imread(output_file4)
        type_id = type_id
        style_id = style_id
        file_name = type_id +'_'+ style_id +'_FILE_OUTPUT' + '__RESULT__' + '.jpg'
        path = os.path.join(UPLOAD_FOLDER,file_name)
        cv2.imwrite(path,img_result)
        with open(path, "rb") as image_file:
            encoded_string64 = base64.b64encode(image_file.read())
        return encoded_string64

    