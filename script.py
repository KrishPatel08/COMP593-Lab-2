def main():
    about_me = {
        'full_name' : 'Krish Umeshbhai Patel',
        'student_id' : '10291361',
        'pizza_toppings' : [
            'ONIONS',
            'BABY CORNS',
            'PANNER'
        ],
        'movies' : [
            {
                'title' : 'avengers',
                'genre' : 'action',
            },
            {
                'title' : 'jungle cruse',
                'genre' : 'advanture'
            }

        ]
    }

    #Add another movie to the data structure
    new_movie = {
        'title' : 'brahmastra',
        'genre' : 'sifi'
    }
    about_me['movies'].append(new_movie)
    

  

    
    




if __name__== '__main__':
    main()