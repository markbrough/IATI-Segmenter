# IATI Segmenter
Takes apart large IATI XML files and outputs one file per country or region. A 
"NULL" file will be created for activities that don't have a country or region 
(this shouldn't happen, but it's possible).

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

## How to segment files

1. Install the module `iatisegmenter`:

        pip install iatisegmenter

2. Import the module and then segment a file:

        import iatisegmenter
        iatisegmenter.segment_file([PREFIX], [SOURCE FILENAME], [OUTPUT DIRECTORY])

   Where:

   `PREFIX` is a short word or acronym at the start of your files, e.g. `dfid`, `worldbank`, etc.

   `SOURCE FILENAME` is the path to your file

   `OUTPUT DIRECTORY` is the path to the directory where the files should be output
