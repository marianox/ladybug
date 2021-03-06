# Open DOE website
# By Mostapha Sadeghipour Roudsari
# Sadeghipour@gmail.com
# Ladybug started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

"""
Open DOE website to download .epw weather file.
-
Provided by Ladybug 0.0.54

    Args:
        _download: Set Boolean to True to open the website
    Returns:
        readMe! : 'Happy downloading...' in case of success
"""
ghenv.Component.Name = "Ladybug_download EPW Weather File"
ghenv.Component.NickName = 'DownloadEPW'
ghenv.Component.Message = 'VER 0.0.54\nFEB_16_2014'
ghenv.Component.Category = "Ladybug"
ghenv.Component.SubCategory = "0 | Ladybug"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

import webbrowser as wb
if _download:
    url = 'http://apps1.eere.energy.gov/buildings/energyplus/cfm/weather_data.cfm'
    wb.open(url,2,True)
    print 'Happy downloading!'
else:
    print 'Set download to true...'
