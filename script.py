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
        'genre' : 'si-fi'
    }
    about_me['movies'].append(new_movie)

    print_student_name_and_id(about_me)
    
    print_pizza_toppings(about_me)

    add_pizza_toppings(about_me, ('pineapple','tomato'))

    print_pizza_toppings(about_me)

    print_movie_genres(about_me)

    print_movie_titles(about_me)


    return

    
#Function that prints student name and ID	
def print_student_name_and_id(about_me):

    full_name = about_me['full_name']
    first_name = about_me['full_name'].split(' ')[0]
    student_id = about_me['student_id']
    print(f'My name is {full_name}, but you can call me Lord {first_name}.')
    print(f'My student ID is {student_id}.')

    return

#Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    for i, nt in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = nt.lower()
    about_me['pizza_toppings'].sort()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f'My favourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'- {p} ')
    return

#Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print("I like to watch ", end="")
    movie_list = [g['genre'] for g in about_me['movies']]
    print(", ".join(movie_list), end=".\n")
    


    return

#Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    print("Some of my favourite movies are  ", end="")
    movie_title = [t['title'] for t in about_me['movies']]
    print(", ".join(movie_title), end="!\n")
    return
    
if __name__== '__main__':
    main()