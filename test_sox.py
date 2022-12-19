import sox
# create transformer
tfm = sox.Transformer()
# trim the audio between 5 and 10.5 seconds.
annotation_start_ms = 3346
annotation_end_ms = 4626
start_seconds = annotation_start_ms / 1000
end_seconds = annotation_end_ms / 1000

print('Start: ', start_seconds, ' End: ', end_seconds)

tfm.trim(start_seconds, end_seconds)
# create an output file.
tfm.build_file("C:\Research\corpus\EN_006.wav", "C:\Research\\recordings-reduction\\trimmed-recordings\EN_006_001.wav")