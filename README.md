# English-Dictionary

My First Python App - Working with Structure Controls, Functions, Databases, JSON,  Libraries,  Data Structures, etc

This is a simple command line application at the moment which I intend to contruct an interface and expand on later on. However, upon running the app, you will be promted to enter a word. This could be any english word which you want to know the definiton for. For example:

                                                    Word: rainnnn

                                                    Below are the defenition(s) found for 'rain':
                                                            - Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.      
                                                            - To fall from the clouds in drops of water.
 
Moreover, if you wanted to look up rain, but inputed rainnnn by accident, the program is intelligent. This is because it will find the closest word in the database and prompt the user if the correctly typed word is what they meant, followed by the definition of that word.
        
                                                    Word: rainnnn
                                                    Did you mean rain? (Y/N) Y

                                                    Below are the defenition(s) found for 'rain':
                                                            - Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
                                                            - To fall from the clouds in drops of water.
                                                            
Lasty, if the word is completely gibrish that is when this message will be displayed: 

                                                    Word: hjgvcghgj

                                                    Hmmm, no defenition found for 'hjgvcghgj'
                                                    
Instructions for use:
- Download repository
- open the terminal and install mySQL: pip install mysql-connector-python
