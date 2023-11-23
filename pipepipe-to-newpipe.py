#!/usr/bin/env python

import os
import sqlite3
import zipfile

# Specify the path to your zip file
zip_file_path = 'PipePipe.zip'

# Open the zip file and extract contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
  zip_ref.extractall(os.path.dirname(zip_file_path))

# Connect to the SQLite database
connection = sqlite3.connect('newpipe.db')
cursor = connection.cursor()

# Rename the column display_index TO is_thumbnail_permanent
cursor.execute('ALTER TABLE playlists RENAME COLUMN display_index TO is_thumbnail_permanent')

# Update all values in the renamed column to 0
cursor.execute('UPDATE playlists SET is_thumbnail_permanent = 0')

# Delete the column display_index
cursor.execute('ALTER TABLE remote_playlists DROP COLUMN display_index')

# Commit the changes
connection.commit()

# Close the connection
connection.close()

# Create a ZipFile object in write mode
with zipfile.ZipFile('NewPipe.zip', 'w') as zip_ref:
  zip_ref.write('newpipe.db', arcname=os.path.basename('newpipe.db'))
  zip_ref.write('newpipe.settings', arcname=os.path.basename('newpipe.settings'))

# Remove extracted files
os.remove('newpipe.db')
os.remove('newpipe.settings')

