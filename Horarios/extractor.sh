#!/bin/bash

# extract professors
python extractors/professor_extractor.py ./career_schedules/dicisHORARIOS.csv ./professors/p.csv

#extract subjects
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLAD.csv ./subjects/s_slad.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLGE.csv ./subjects/s_slge.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLICE.csv ./subjects/s_slice.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLIEL.csv ./subjects/s_sliel.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLIME.csv ./subjects/s_slime.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIO_2018_2sem_SLISC.csv ./subjects/s_slisc.csv
python extractors/subject_extractor.py ./career_schedules/dicisHORARIOS.csv ./subjects/s.csv
