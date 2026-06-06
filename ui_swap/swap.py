import xbmc
import xbmcvfs

# Check if the "Icons Only" setting is toggled ON
is_icons = xbmc.getCondVisibility('Skin.HasSetting(SkynetIconsOnly)')

# Define our holding pen files
if is_icons:
    home_src = 'special://skin/ui_swap/Home_Icons.xml'
    inc_src = 'special://skin/ui_swap/Includes_Home_Icons.xml'
else:
    home_src = 'special://skin/ui_swap/Home_Wide.xml'
    inc_src = 'special://skin/ui_swap/Includes_Home_Wide.xml'

# Define the live Kodi destination files
home_dest = 'special://skin/xml/Home.xml'
inc_dest = 'special://skin/xml/Includes_Home.xml'

# Delete the old files to ensure a clean slate
xbmcvfs.delete(home_dest)
xbmcvfs.delete(inc_dest)

# Copy the requested files into the live XML folder
xbmcvfs.copy(home_src, home_dest)
xbmcvfs.copy(inc_src, inc_dest)

# Force Kodi to instantly reload the UI
xbmc.executebuiltin('ReloadSkin()')