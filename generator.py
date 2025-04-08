from PIL import Image
import os
import random
personlist = os.listdir('people')
backlist = ['people_backgrounds/1.png','people_backgrounds/2.png','people_backgrounds/3.png','people_backgrounds/4.png','people_backgrounds/5.png']
output_directory = "thumbnail_img"
def revamp(ist, b):
    for i in range(5):
        for person in ist:
            if not 'people' in person:
                if b == 0:
                    ist.append('people/'+person)
                    ist.remove(person)
                if b == 1:
                    ist.append('people_backgrounds/'+person)
                    ist.remove(person)
                else:
                    continue
    print(ist)
"""personlist,0
        OR
    backlist, 1
    """

revamp(personlist, 0)
revamp(backlist, 1)
os.makedirs(output_directory, exist_ok=True)



def ImgCreation(num):
        for i in range(num+1):
            image1_path = random.choice(backlist)
            image2_path = random.choice(personlist) 
            image1 = Image.open(image1_path).convert("RGBA")
            image2 = Image.open(image2_path).convert("RGBA")
            image2 = image2.resize(image1.size)
            combined = Image.alpha_composite(image1, image2)
            output_path = os.path.join(output_directory, f"thumbnail{i}.png")
            combined.save(output_path)
f = input("How many files would you like to create?" )
ImgCreation(int(f))
#The files will be stored in a new directory called (thumbnail_img)