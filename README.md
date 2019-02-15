# FeedToCSV

Python 3 scripts to consume some feed of items and prepare them for ingest into a DSpace repository via bulk ingest. This code generates output which can be directly passed to the [DSpace CSV Archive](https://github.com/lib-uoguelph-ca/dspace-csv-archive) tool for conversion to the [DSpace Simple Archive Format](https://wiki.duraspace.org/display/DSDOC5x/Importing+and+Exporting+Items+via+Simple+Archive+Format).

Not exactly fit for public consumption, though you might find some value.

These script establish a modular framework which can be extended in order to consume other sources of content. Current implementations include:
* Internet Archive harvester
* InMagic harvester

These scripts generate two primary forms of output:
* A CSV file containing all of the metadata
* All of the associated files.

Reusable components included here which might interest others:
* A simple CSV file writer
* A threaded downloader, which will pull URLs as they are added to a queue, and downloads the files concurrently
* A transformer base class, which provides a pattern for defining crosswalks between metadata formats.

## Installation
1. Clone this repository
2. Install dependencies with `pip install -r requirements.txt`

## Internet Archive harvester
In order to use this, you'll need to:
* Sign up for an account
* Generate the ia.ini file by running `ia --config-file './ia.ini' configure`.
  Make sure the ia.ini file lives in the root of your repository.
