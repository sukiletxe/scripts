# Scripts

These are small scripts that I used at least once and I thought would be nice sharing.

* Poner_quitar_letras (Python): Sorts a collection of folders (the parent of the folder where the script is), putting every folder that starts with one letter or number in its folder. For example `English` and `Engineering` would be moved into `E`. Removes this sorting if it is in place. Only works with folders, doesn't do anything with files. To repeat: this script sorts the parent folder of the script, so create a folder for it. (The rationale back in the day was that I turned this into an exe with the libraries and such in separate files, so I wanted to avoid clutter).
* Test_killing_pids (Python): Dirty test to see how a process can kill itself. Not useful on its own.
* Addtochannels (Python): Adds some Telegram users to some channels (or supergroups).
* Notifyadded (Python): Script which notifies you who added you to a telegram group (not retroactively), and the groups in common you have with the person who added you.
* dirlist (Powershell): Script which lists a folder recursively, outputting the result in `dirlist<foldername>.txt`. Here the level of a subfolder is indicated with indentation.
* Mono (AutoHotkey): Press Ctrl+Win+Alt+M to toggle systemwide mono audio. Works in Windows 10, no idea if it does in Windows 11.
* kill_atvplus_aria_labels (Tampermonkey): Removes useless aria labels from the Apple Tv+ website. This fixes the accessibility of some headings (which appear as just links to screen readers) and the website's language chooser (which doesn't show the actual languages you can choose). In Chrome (maybe in Edge too) with NVDA you need to press NVDA+F5 after opening or refreshing any Apple TV+ url to actually see that the labels are gone, in Firefox this is not necessary. I don't know why this happens.
