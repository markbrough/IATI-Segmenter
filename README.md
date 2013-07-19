# IATI Segmenter
Takes apart large IATI XML files and outputs one file per country or region. A "NULL" file will be created for activities that don't have a country or region (this shouldn't happen, but it's possible).

## License

Copyright 2013 Mark Brough.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License v3.0 as 
published by the Free Software Foundation, either version 3 of the License, 
or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## How to run the scripts

1. Install the dependencies. It's recommended that you use a `virtualenv`. From
within the relevant folder, run the following commands (all commands assume a Linux
installation):

        virtualenv ./pyenv
        source ./pyenv/bin/activate
        pip install -r requirements.txt

3. Run the script:

        ./iati_segmenter.py [FILENAME]

4. The data should be output to `data/`

5. You can also provide multiple files:

        ./iati_segmenter.py [FILENAME1] [FILENAME2] etc...
