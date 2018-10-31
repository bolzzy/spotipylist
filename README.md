# spotipylist
Python Script to automate copy of rotating release radar list to a self-managed list

## Setup:

 * Setup a spotify developer nonprofit app
 * Add clientid and clientsecret to config file in the same directory as script
 * Create a new playlist that songs will get added to
 * Update the config file with the uri for the release radar playlist and the new playlist and your spotify username

## Usage:

To use this script, you need to authenticate. When the script launches, you will get propted by your browser to accept the spotify app permissions.
Click accept and copy the following redirect url into the script. The next time the script should run without need to authenticate.
