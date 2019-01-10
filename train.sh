#!/bin/bash
python src/prepare-data.py input_data.txt prepared_data
python src/train-autoencoder.py -i 1 -e 1 -b 50 saved_model prepared_data/vocabulary.txt prepared_data/train-data.npz prepared_data/valid-data.npz

