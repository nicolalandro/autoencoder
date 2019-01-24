# Text Autoencoder

This project refers to [erickrf/autoencoder](https://github.com/erickrf/autoencoder)

# Sample Usage

## GPU

    $ docker-compose run gpu-train
    $ docker-compose run gpu-interact

To have a bash shell

    $ docker-compose run gpu
    $ ./train.sh
    $ ./transform.sh


## CPU

    $ docker-compose run cpu-train
    $ docker-compose run cpu-interact

To have a bash shell

    $ docker-compose run cpu

# Webscaper data
Using [webscreper.io](https://addons.mozilla.org/en-US/firefox/addon/web-scraper/?src=search) on firefox it is possible to scrape web for data.
In that folder there are a sitemap exported, and the csv result.
With script scraped_title_to_list_file.py it is possible to write title column of csv into input_data.txt