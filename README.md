# usergen
This receives as input two dictionaries (name, last name) and writes into an output file the generated usernames.

usage: usergen.py [-h] [-mN MIN_CHARS_N] [-xN MAX_CHARS_N] [-mS MIN_CHARS_S]
                  [-xS MAX_CHARS_S] [-u UNION [UNION ...]] [-o OUTPUT]
                  [-m {a,w}]
                  Names Surnames

Generate usernames with A LOT of different of options.

positional arguments:
  Names                 The path to the file containing the dictionary with
                        names.
  Surnames              The path to the file containing the dictionary with
                        names.


optional arguments:
  -h, --help            show this help message and exit
  
  -mN MIN_CHARS_N, --min-chars-N MIN_CHARS_N
  
                        The minimum number of chars from the Name. Default is
                        1.
                        
  -xN MAX_CHARS_N, --max-chars-N MAX_CHARS_N
  
                        The maximum number of chars from the Name. Default is
                        1.
                        
  -mS MIN_CHARS_S, --min-chars-S MIN_CHARS_S
  
                        The minimum number of chars from the Surname. Default
                        is 7.
                        
  -xS MAX_CHARS_S, --max-chars-S MAX_CHARS_S
  
                        The maximum number of chars from the Surname. Default
                        is 7.
                        
  -u UNION [UNION ...], --union UNION [UNION ...]
  
                        Select if you want a binding character [_ . - ] etc.
                        Default is None.
                        
  -o OUTPUT, --output OUTPUT
  
                        If you want to specify the name of the output file.
                        Default is... usernames! Yay!
  -m {a,w}, --mode {a,w}
  
                        If you want the results to be appended to the file or
                        to overwrite. Default is overWrite.

