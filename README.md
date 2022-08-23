### Command-line arguments

```
    disconnect                                          : Disconnect us from the server.
    print                                               : Print the batteries, the temperature chambers and the diagnostic chambers registred to our database.
    register -<type> args                               : Register to our database a battery ("b"), a temperature chamber ("tc") or a diagnostic chamber ("dc").
    pop -<type> <id>                                    : Remove from our database the element of type with it's id. 
    save                                                : Save the current database into the databse.pickle file.
    load-s                                              : Load the database form the database.pickle file.
    load-b <id of dc> <id of battery> <channel>         : Load the batteries into the dc into the channel given in argument.
    check-diag                                          : Check and print all the batteries that needs to be diagnosticated.
    start <id of dc>                                    : Start the diagnostic of the diagnostic chamber given in parameter.
    status <id of dc>                                   : Give the number of days until the diagnostic finsih.
    generate-f <id of dc>                               : Generate the files for the batteries registred in the diagnostic chamber.
    abort <id of dc>                                    : Abort the diagnostic of the diagnostic chamber given in parameter.
    unload <id of dc>                                   : Unload the diagnostic chamber if the time of diagnostic is finished.

```