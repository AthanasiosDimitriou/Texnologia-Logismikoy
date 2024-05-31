Δημιουργήστε ένα Container και βάλτε το link του repository: https://github.com/AthanasiosDimitriou/Texnologia-Logismikoy

Μέσω Docker ανοίξτε το VSCode.
Στην συυνέχεια ανοίξτε το terminal και εισάγεται τις παρακάτω εντολές μία προς μία:
1) docker build -t my_streamlit_app . (Είναι μαζί με την τελεία)
2) docker run -p 8501:8501 my_streamlit_app

Τέλος θα σας βγάλει το παρακάτω μήνυμα και με CTRL+Click στο URL θα σας ανοίξει την εφαρμογή στον browser σας.
