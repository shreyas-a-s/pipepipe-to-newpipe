#!/bin/sh

# Install dependencies
if which apt-get > /dev/null; then
  sudo apt-get install -y zip unzip sqlite3
fi

# Open the zip file and extract contents
unzip -o PipePipe.zip

# Connect to the SQLite database
sqlite3 newpipe.db <<EOF

-- Rename the column display_index TO is_thumbnail_permanent
ALTER TABLE playlists RENAME COLUMN display_index TO is_thumbnail_permanent;

-- Update all values in the renamed column to 0
UPDATE playlists SET is_thumbnail_permanent = 0;

-- Delete the column display_index
ALTER TABLE remote_playlists DROP COLUMN display_index;

EOF

# Create a zip file
zip -r NewPipe.zip newpipe.db newpipe.settings

# Remove extracted files
rm newpipe.db newpipe.settings
