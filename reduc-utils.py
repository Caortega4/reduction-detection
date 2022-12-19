import csv
import glob 
import pympi # Import pympi to work with elan files
import sox

corpus_root = 'C:\Research\\recordings-reduction'
tier_names = ['reductionLeft', 'reductionRight']
print(corpus_root)
audio_id = 0

tfm = sox.Transformer()

with open('metadata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'label'])

    for file_path in glob.glob('{}/*reduction.eaf'.format(corpus_root)):
        wav_path = file_path.split('-reduction.eaf')[0] + ".wav"
        print(wav_path)
        file_id = file_path.split('\\')[-1][:-4]
        
        eafob = pympi.Elan.Eaf(file_path)
        for tier in tier_names:
        # If the tier is not present in the elan file spew an error and
        # continue. This is done to avoid possible KeyErrors
            if tier not in eafob.get_tier_names():
                print ('WARNING!!!')
                print ('One of the tiers is not present in the elan file')
                print ('namely: {}. skipping this one...'.format(tier))
        # If the tier is present we can loop through the annotation data
            else:
                for annotation in eafob.get_annotation_data_for_tier(tier):
                # For each annotation do:
                    # print(annotation[0], annotation[1], annotation[2])
                    start_seconds = annotation[0] / 1000
                    end_seconds = annotation[1] / 1000
                    tfm.trim(start_seconds, end_seconds)
                    # create an output file.
                    tfm.build_file(wav_path, "C:\Research\\recordings-reduction\\trimmed-recordings\\" + str(file_id) + "-" + str(audio_id) + ".wav")
                    writer.writerow([audio_id, annotation[2]])
                    audio_id += 1