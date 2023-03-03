import csv
import glob 
import pympi # Import pympi to work with elan files

corpus_root = "C:\Research\\features\EN\\"

counts = [0,0,0,0]

for file_path in glob.glob('{}/*reduction.eaf'.format(corpus_root)):
    print("Getting label distribution for: ", file_path)
    file_id = file_path.split('\\')[-1][:-4]        
    eafob = pympi.Elan.Eaf(file_path)
    for tier in eafob.get_tier_names():
        for annotation in eafob.get_annotation_data_for_tier(tier):
        # For each annotation do:
            # print(annotation[1])
            # print(annotation[2])
            if annotation[2] == '' or int(annotation[2]) > 3 or int(annotation[2]) < 0:
                print("Mislabeled data end at: ", annotation[1])
            else:
                counts[int(annotation[2])] += 1
    print("Counts for ", file_path," :", counts)

print("Total counts: ", counts)

