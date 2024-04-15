#!/bin/bash
rsync -av videos/* hello@192.168.24.10:/mnt/d4t/data/court/videos/
rsync -av images/* hello@192.168.24.10:/mnt/d4t/data/court/images/
rsync -av pt/* hello@192.168.24.10:/mnt/d4t/data/court/pt/