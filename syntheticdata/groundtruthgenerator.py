import glob, os, re
from tqdm import tqdm
os.chdir("nums/generated")
for file in tqdm(glob.glob("*.png")):
    # print(re.search("[.0-9]*", file)[0])
    f = open(file.replace(".png", ".gt.txt"), "w")
    f.write(re.search("[.0-9]*", file)[0])
    f.close()