# Next Stop

Backend for [@civic-data-design-lab](http://github.com/civic-data-design-lab)'s work for the Cooper Hewitt's _Reimagining Mobility_ exhibition. 

Currently, this installation supports macOS and linux, although Windows usage is possibe if you compile your own SANE back end. This can run on a raspberry pi or similar ARM system, but some library requirements (like numpy and scipy) may take a while to install -- take a look at piwheels for pre-compiled ARM libraries.

## Install SANE

1. See if homebrew is installed on your Mac (type `brew --version` into a terminal window).
2. If not, run this command in a terminal window: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
3. In a terminal window, `run brew install sane-backends`

## Install PIP (Python Package Manager)

1. Check if PIP is installed by typing `pip -V` into a terminal window.
2. In a terminal window, type `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
3. In a terminal window, type `python3 get-pip.py`

## [Download and Extract My Repository](https://github.com/ericmhuntley/nextstop/archive/master.zip)

## Install Project Dependencies

1. In a terminal window, change directory into the repository root (for example, `cd ~/Downloads/nextstop`).
2. Install my project dependencies by typing `pip install -r requirements.txt`

## Run our Scheduler

Assuming you have the scanner hooked up to a USB port, you should now be able to run `python3 scheduler.py` from a terminal window. This will get the scanner running - drop a card in and within a few sections it will scan.

Your new scans will save as front and back PNGs in the folder 'scans' nested within your working directory.

## Processing Scans 

Every night, the scheduler should upload the cards to the CDDL web server, which has the processing script. Additionally, the server *should* automatically process scans every night. Follow the below steps if the new scans are not appearing online and to manually process scans.

1. Use SSH to connect to ehuntley.media.mit.edu.
2. Run `python3 /home/ehuntley/nextstop/process.py` to read and output the card json. `Read.json` will be output under `/home/ehuntley/scans/`. Note that this command will only process cards scanned within the past 24 hours, unless you have modified the timedelta variable, located under `nextstop/cardscanner/process.py`. 
3. Ingest the JSON to SQL by running: cat `/home/ehuntley/scans/read.json | psql -d nextstop -U ehuntley -h localhost -c 'COPY pushjson (data) FROM STDIN;'`
4. Then, to parse the SQL run `psql -d nextstop -U ehuntley -h localhost -f '/home/ehuntley/scans/parse_json.sql'`
5. If you encounter a duplicate error, that means that two (or more) entries in the pushjson table have the same id (UUID). In order to fix this, either wait 24 hours (parse_json.sql will only handle entries ingested in the past 24 hours) or access the postgres database via PGadmin (or other client) and delete the entries from your timestamp. For example, `DELETE FROM pushjson WHERE ingested_at > ‘2019-01-06 10:09:32’`
