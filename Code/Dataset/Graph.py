
import os 
import matplotlib.pyplot as plt

train_path ='K://DATASET//DATSET_BIG'
labels=os.listdir(train_path)

print(labels,len(labels))

IMAGES=[]   

for i in labels:

    class_folder = os.path.join(train_path, i) 
    
    image_name = os.listdir(class_folder)
    nn=0
    for ii in range(len(image_name)):
        nn+=1
    #print(f'Folder: {i} {nn}')
    IMAGES.append(nn)

plt.figure(figsize=(15, 5)) 
plt.bar(labels, IMAGES)
plt.ylabel('Number of Images Train', fontsize=14)
plt.xlabel('Folder', fontsize=14)
plt.title('Image Count in Folder Train', fontsize=16, fontweight='bold')
plt.show()


