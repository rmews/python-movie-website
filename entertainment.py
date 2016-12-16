import fresh_tomatoes
import media

# Create instances of favorite movies
# Each movie variable consist of 4 arguments
casino_royale = media.Movie("Casino Royale",
                            "Armed with a licence to kill, Secret Agent James"
                            " Bond sets out on his first mission as 007 and"
                            " must defeat a weapons dealer in a high stakes"
                            " game of poker at Casino Royale, but things are"
                            " not what they seem.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMDI5ZWJhOWItYTlhOC00YWNhLTlkNzctNDU5YTI1M2E1MWZhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_CR0,0,672,1000_AL_.jpg  # NOQA",
                            "https://www.youtube.com/watch?v=xK7PbujRUOk")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246  # NOQA",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
star_wars = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                        "During the near end of the clone wars, Darth Sidious"
                        " has revealed himself and is ready to execute the"
                        " last part of his plan to rule the Galaxy.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_SY1000_SX750_AL_.jpg  # NOQA",
                        "https://www.youtube.com/watch?v=5UnjrG_N8hU")
inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of"
                        " dream-sharing technology, is given the inverse task"
                        " of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg  # NOQA",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels"
                         " about the true nature of his reality and his role"
                         " in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg  # NOQA",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")
office_space = media.Movie("Office Space",
                           "Three company workers who hate their jobs decide"
                           " to rebel against their greedy boss.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BOTA5MzQ3MzI1NV5BMl5BanBnXkFtZTgwNTcxNTYxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg  # NOQA",
                           "https://www.youtube.com/watch?v=dMIrlP61Z9s")

# construct movies object
movies = [casino_royale, avatar, star_wars, inception, the_matrix,
          office_space]

# Call fresh tomatoes file by passing movies object as argument
fresh_tomatoes.open_movies_page(movies)
