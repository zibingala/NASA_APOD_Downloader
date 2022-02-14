# NASA_APOD_Downloader
NASA - Astro Picture of the Day Downloader

Based on Ajinkya Sonawane's code on medium.com   
https://medium.com/daily-python/consuming-nasa-api-using-python-part-1-daily-python-17-4ce104fa47ab

# INSTALL
pip install requests

CREATE your API-key at https://api.nasa.gov/
COPY it to line 16

FOLDER for your downloads automatically created
NAME IT in line 19

# USAGE

Two modes (Single date || Iterate through Years/Months) :  
- Change booleans in line 22 or line 28 to choose between modes
- set dates for single download or iteration in line {23,25} && line {29,32}

- Automatically tries to use 'hdurl' (you can uncomment line 61 for simple url)
- Currently works only with images (no videos, or other 'media_type')

# ENJOY THE UNIVERSE!
