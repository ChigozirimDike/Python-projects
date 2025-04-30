import os
#os.chdir("Photos")
#organized = os.listdir()
#print(organized)

def organized_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
    make_place_directories(places) 
    print(os.listdir()) 
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


def extract_place(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    second = partial.find("_")
    return partial[:second]

def make_place_directories(places):
    for place in places:
        os.mkdir(place)

#organized_photos("Photos")
print("I run all the time!")

if __name__ == '__main__':
    print("I've been run directly!")

if __name__ == 'organized_photos':
    print("I've been imported!")