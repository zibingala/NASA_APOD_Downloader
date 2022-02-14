###########################################################
## NASA -  Astronomy Picture of The Day Archive Download ##
###########################################################
#### Based on Ajinkya Sonawane's code on medium.com #######
## https://medium.com/daily-python/consuming-nasa-api-using-python-part-1-daily-python-17-4ce104fa47ab
###########################################################
######################## zibingala ########################
#########################  2022.  #########################
###########################################################

## pip install requests
import requests
import os

## create your API-key at https://api.nasa.gov/
apiKey = 'YOUR_API_KEY'

## Foldername for download - next to .py file
FolderName = 'apod'

## Single Picture Download
Single = True
y_single = 2022 # year
m_single = 2 # month 
d_single = 13 # day

## Iterate through and download
Iterate = False
y1 = 2010 # beginning year
y2 = 2011 # ending year (included)
m1 = 1 # beginning month
m2 = 12 # ending month (included)

# Create target Folder if doesn't exist
if not os.path.exists(FolderName):
    os.mkdir(FolderName)
    print("Directory " , FolderName ,  " Created ")
else:    
    print("Directory " , FolderName ,  " already exists")

# Downloading function
def fetchAPOD(y,m,d):

  ## fill 0s 
  if m < 10:
      m = '0' + str(m)
  if d < 10:
      d = '0' + str(d)

  URL_APOD = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key':apiKey,
      'date': str(y) + '-' + str(m) + '-' + str(d),
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  # print(response)
  ## url = response.get('url')
  if response.get('media_type') == 'image':
    try:
        url = response.get('hdurl')
    except:
        try:
            url = response.get('url')
        except:
            print (str(y) + str(m) + str(d) + ' <-- No URL recieved.')
            return
    print(url)
    r = requests.get(url, allow_redirects=True)
    open(FolderName +'/apod' + str(y) + str(m) + str(d) + '.jpg', 'wb').write(r.content)

## iterates through years - change year
def iteratethrough(y1, y2, m1, m2):
    for y in range (y1, y2+1):
        for m in range (m1, m2+1):
            # of course, some kind of switch function would be more elegant than nested if-else-if-else-if...
            if m in (1, 3, 5, 7, 8, 10, 12):
                for d in range (1,31+1):
                    fetchAPOD(y, m, d)
            else: 
                if m in (4,6,9,11):
                    for d in range (1,30+1):
                        fetchAPOD(y, m, d)
                else: 
                    for d in range (1,28+1):
                        fetchAPOD(y, m, d)

if Single:
    fetchAPOD(y_single, m_single, d_single)

if Iterate:
    iteratethrough(y1, y2, m1, m2)













# https://github.com/zibingala/ # 2022 #
