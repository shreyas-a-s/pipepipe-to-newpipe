## Convert PipePipe database to work with NewPipe

## Motivation to create this project
[PipePipe](https://github.com/InfinityLoop1308/PipePipe) is a fork of [NewPipe](https://github.com/TeamNewPipe/NewPipe) which is snappier and less buggy compared to the original one (in my opinion). But one thing that bothered me was that if we export the db from PipePipe and import it to NewPipe, the app would crash and won't launch.

- One might ask, is this really important?

It is. Suppose sometime in future PipePipe stops gettings any more updates (let's hope it won't happen) and I want to move back to NewPipe, I want to make sure that I can get all my data from PipePipe to NewPipe.

## How to use
- Export database from PipePipe (Settings > Content > Export database)
- Rename the .zip file you got to PipePipe.zip
- Place it and the script (either pipepipe-to-newpipe.py or pipepipe-to-newpipe.sh) in same folder
- Execute the script (either by `./pipepipe-to-newpipe.py` or `./pipepipe-to-newpipe.sh`)
- Copy NewPipe.zip back to phone
- Import database to NewPipe (Settings > Backup and restore > Import database)
- Good to go

## What this script does
- Rename the column display_index in 'playlists' table to is_thumbnail_permanent
- Update all values in the renamed column to 0
- Delete the column display_index in 'remote_playlists' table

