# Data for books and songs
books_data = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "genre": "Fiction"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "1984": {"author": "George Orwell", "genre": "Science Fiction"},
    "Pride and Prejudice": {"author": "Jane Austen", "genre": "Romance"},
    "Harry Potter and the Sorcerer's Stone": {"author": "J.K. Rowling", "genre": "Fantasy"},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "genre": "Fiction"},
    "The Lord of the Rings": {"author": "J.R.R. Tolkien", "genre": "Fantasy"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "Animal Farm": {"author": "George Orwell", "genre": "Fiction"},
    "The Hobbit": {"author": "J.R.R. Tolkien", "genre": "Fantasy"},
    "Brave New World": {"author": "Aldous Huxley", "genre": "Science Fiction"},
    "The Hunger Games": {"author": "Suzanne Collins", "genre": "Science Fiction"},
    "The Diary of a Young Girl": {"author": "Anne Frank", "genre": "Autobiography"},
    "Frankenstein": {"author": "Mary Shelley", "genre": "Gothic Fiction"},
    "Moby-Dick": {"author": "Herman Melville", "genre": "Adventure"},
    "The Picture of Dorian Gray": {"author": "Oscar Wilde", "genre": "Gothic Fiction"},
    "The Hitchhiker's Guide to the Galaxy": {"author": "Douglas Adams", "genre": "Science Fiction"},
    "The Chronicles of Narnia": {"author": "C.S. Lewis", "genre": "Fantasy"},
    "Jane Eyre": {"author": "Charlotte Brontë", "genre": "Gothic Fiction"},
    "One Hundred Years of Solitude": {"author": "Gabriel García Márquez", "genre": "Magic Realism"},
    "The Count of Monte Cristo": {"author": "Alexandre Dumas", "genre": "Adventure"},
    "The Bell Jar": {"author": "Sylvia Plath", "genre": "Autobiography"},
    "The Odyssey": {"author": "Homer", "genre": "Epic Poetry"},
    "The Iliad": {"author": "Homer", "genre": "Epic Poetry"},
    "Anna Karenina": {"author": "Leo Tolstoy", "genre": "Fiction"},
    "Crime and Punishment": {"author": "Fyodor Dostoevsky", "genre": "Fiction"},
    "The Brothers Karamazov": {"author": "Fyodor Dostoevsky", "genre": "Fiction"},
    "Don Quixote": {"author": "Miguel de Cervantes", "genre": "Adventure"},
    "The Canterbury Tales": {"author": "Geoffrey Chaucer", "genre": "Poetry"},
    "Wuthering Heights": {"author": "Emily Brontë", "genre": "Gothic Fiction"},
    "Gone with the Wind": {"author": "Margaret Mitchell", "genre": "Historical Fiction"},
    "Les Misérables": {"author": "Victor Hugo", "genre": "Historical Fiction"},
    "The Alchemist": {"author": "Paulo Coelho", "genre": "Fiction"},
    "Little Women": {"author": "Louisa May Alcott", "genre": "Fiction"},
    "The Adventures of Sherlock Holmes": {"author": "Arthur Conan Doyle", "genre": "Mystery"},
    "The Divine Comedy": {"author": "Dante Alighieri", "genre": "Epic Poetry"},
    "The Grapes of Wrath": {"author": "John Steinbeck", "genre": "Fiction"},
    "A Tale of Two Cities": {"author": "Charles Dickens", "genre": "Historical Fiction"},
    "The Secret Garden": {"author": "Frances Hodgson Burnett", "genre": "Children's Fiction"},
    "The Phantom of the Opera": {"author": "Gaston Leroux", "genre": "Gothic Fiction"},
    "The Road": {"author": "Cormac McCarthy", "genre": "Post-Apocalyptic Fiction"},
    "Dracula": {"author": "Bram Stoker", "genre": "Gothic Fiction"},
    "The Adventures of Tom Sawyer": {"author": "Mark Twain", "genre": "Adventure"},
    "The Importance of Being Earnest": {"author": "Oscar Wilde", "genre": "Comedy"},
    "The Shining": {"author": "Stephen King", "genre": "Horror"},
    "Great Expectations": {"author": "Charles Dickens", "genre": "Fiction"},
    "The Color Purple": {"author": "Alice Walker", "genre": "Fiction"},
    "The Old Man and the Sea": {"author": "Ernest Hemingway", "genre": "Fiction"},
    "The Road Less Traveled": {"author": "M. Scott Peck", "genre": "Self-Help"},
    "The Joy Luck Club": {"author": "Amy Tan", "genre": "Fiction"},
    "The Kite Runner": {"author": "Khaled Hosseini", "genre": "Fiction"},
    "Life of Pi": {"author": "Yann Martel", "genre": "Adventure"},
    "The Girl with the Dragon Tattoo": {"author": "Stieg Larsson", "genre": "Mystery"},
    "The Outsiders": {"author": "S.E. Hinton", "genre": "Young Adult"},
    "The Da Vinci Code": {"author": "Dan Brown", "genre": "Thriller"},
    "The Fault in Our Stars": {"author": "John Green", "genre": "Young Adult"},
    "The Help": {"author": "Kathryn Stockett", "genre": "Historical Fiction"},
    "The Handmaid's Tale": {"author": "Margaret Atwood", "genre": "Science Fiction"},
    "The Martian": {"author": "Andy Weir", "genre": "Science Fiction"},
    "Jurassic Park": {"author": "Michael Crichton", "genre": "Science Fiction"},
    "The Road to Wigan Pier": {"author": "George Orwell", "genre": "Non-Fiction"},
    "Fear and Loathing in Las Vegas": {"author": "Hunter S. Thompson", "genre": "Autobiography"},
    "Lord of the Flies": {"author": "William Golding", "genre": "Fiction"},
    "The Sun Also Rises": {"author": "Ernest Hemingway", "genre": "Fiction"}
}

songs_data = {
    "Shape of You": {"artist": "Ed Sheeran", "genre": "Pop"},
    "Bohemian Rhapsody": {"artist": "Queen", "genre": "Rock"},
    "Someone Like You": {"artist": "Adele", "genre": "Pop"},
    "Despacito": {"artist": "Luis Fonsi", "genre": "Latin"},
    "Uptown Funk": {"artist": "Mark Ronson ft. Bruno Mars", "genre": "Funk"},
    "Don't Stop Believin'": {"artist": "Journey", "genre": "Rock"},
    "Billie Jean": {"artist": "Michael Jackson", "genre": "Pop"},
    "Sweet Child o' Mine": {"artist": "Guns N' Roses", "genre": "Rock"},
    "Rolling in the Deep": {"artist": "Adele", "genre": "Pop"},
    "Hotel California": {"artist": "Eagles", "genre": "Rock"},
    "Smooth": {"artist": "Santana ft. Rob Thomas", "genre": "Rock"},
    "Hips Don't Lie": {"artist": "Shakira ft. Wyclef Jean", "genre": "Latin"},
    "Smells Like Teen Spirit": {"artist": "Nirvana", "genre": "Rock"},
    "Shape of My Heart": {"artist": "Sting", "genre": "Pop"},
    "Livin' on a Prayer": {"artist": "Bon Jovi", "genre": "Rock"},
    "Girls Just Want to Have Fun": {"artist": "Cyndi Lauper", "genre": "Pop"},
    "Every Breath You Take": {"artist": "The Police", "genre": "Rock"},
    "Hey Jude": {"artist": "The Beatles", "genre": "Rock"},
    "I Will Always Love You": {"artist": "Whitney Houston", "genre": "Pop"},
    "Imagine": {"artist": "John Lennon", "genre": "Pop"},
    "Wonderwall": {"artist": "Oasis", "genre": "Rock"},
    "Like a Rolling Stone": {"artist": "Bob Dylan", "genre": "Rock"},
    "Sweet Caroline": {"artist": "Neil Diamond", "genre": "Pop"},
    "Take On Me": {"artist": "a-ha", "genre": "Pop"},
    "Thriller": {"artist": "Michael Jackson", "genre": "Pop"},
    "Wonderful Tonight": {"artist": "Eric Clapton", "genre": "Rock"},
    "I Want to Hold Your Hand": {"artist": "The Beatles", "genre": "Rock"},
    "Love Shack": {"artist": "The B-52's", "genre": "Pop"},
    "Boogie Wonderland": {"artist": "Earth, Wind & Fire with The Emotions", "genre": "Funk"},
    "My Heart Will Go On": {"artist": "Celine Dion", "genre": "Pop"},
    "Kashmir": {"artist": "Led Zeppelin", "genre": "Rock"},
    "Another Brick in the Wall, Pt. 2": {"artist": "Pink Floyd", "genre": "Rock"},
    "Purple Rain": {"artist": "Prince and The Revolution", "genre": "Pop"},
    "Piano Man": {"artist": "Billy Joel", "genre": "Pop"},
    "Crazy": {"artist": "Gnarls Barkley", "genre": "Pop"},
    "Every Little Thing She Does Is Magic": {"artist": "The Police", "genre": "Rock"},
    "Africa": {"artist": "Toto", "genre": "Rock"},
    "Eye of the Tiger": {"artist": "Survivor", "genre": "Rock"},
    "Under Pressure": {"artist": "Queen & David Bowie", "genre": "Rock"},
    "Careless Whisper": {"artist": "George Michael", "genre": "Pop"},
    "Brown Eyed Girl": {"artist": "Van Morrison", "genre": "Pop"},
    "I Want to Know What Love Is": {"artist": "Foreigner", "genre": "Rock"},
    "Don't You (Forget About Me)": {"artist": "Simple Minds", "genre": "Pop"},
    "Here Comes the Sun": {"artist": "The Beatles", "genre": "Pop"},
    "I Wanna Dance with Somebody (Who Loves Me)": {"artist": "Whitney Houston", "genre": "Pop"},
    "Dancing Queen": {"artist": "ABBA", "genre": "Pop"},
    "Bohemian Like You": {"artist": "The Dandy Warhols", "genre": "Rock"},
    "Drops of Jupiter (Tell Me)": {"artist": "Train", "genre": "Rock"},
    "Total Eclipse of the Heart": {"artist": "Bonnie Tyler", "genre": "Pop"},
    "I Will Survive": {"artist": "Gloria Gaynor", "genre": "Disco"},
    "The Sound of Silence": {"artist": "Simon & Garfunkel", "genre": "Folk"},
    "Take Me Home, Country Roads": {"artist": "John Denver", "genre": "Country"},
    "Let It Be": {"artist": "The Beatles", "genre": "Pop"},
    "American Pie": {"artist": "Don McLean", "genre": "Pop"},
    "Wannabe": {"artist": "Spice Girls", "genre": "Pop"},
    "My Way": {"artist": "Frank Sinatra", "genre": "Jazz"},
    "Black Dog": {"artist": "Led Zeppelin", "genre": "Rock"},
    "Dream On": {"artist": "Aerosmith", "genre": "Rock"},
    "Don't Speak": {"artist": "No Doubt", "genre": "Pop"},
    "Bennie and the Jets": {"artist": "Elton John", "genre": "Pop"},
    "Hotel California (Acoustic Version)": {"artist": "Eagles", "genre": "Rock"},
    "Lose Yourself": {"artist": "Eminem", "genre": "Hip Hop"},
    "Blue Suede Shoes": {"artist": "Elvis Presley", "genre": "Rock"},
    "Stairway to Heaven": {"artist": "Led Zeppelin", "genre": "Rock"},
    "I'm Yours": {"artist": "Jason Mraz", "genre": "Pop"},
    "The Scientist": {"artist": "Coldplay", "genre": "Pop"},
    "Brown Sugar": {"artist": "The Rolling Stones", "genre": "Rock"},
    "Let's Get It On": {"artist": "Marvin Gaye", "genre": "R&B"},
    "Sultans of Swing": {"artist": "Dire Straits", "genre": "Rock"},
    "Here, There and Everywhere": {"artist": "The Beatles", "genre": "Pop"},
    "I Still Haven't Found What I'm Looking For": {"artist": "U2", "genre": "Rock"}
}

# Function to recommend books and songs based on user preferences
def recommend_items(preferences):
    recommended_items = []
    for item, details in books_data.items():
        if (details["genre"] in preferences or details["author"] in preferences or item in preferences) and item not in recommended_items:
            recommended_items.append(item)
    for item, details in songs_data.items():
        if (details["genre"] in preferences or details["artist"] in preferences or item in preferences) and item not in recommended_items:
            recommended_items.append(item)
    return recommended_items

# Example usage
def main():
    print("Welcome to the Recommendation System!")
    print("Please enter your preferences. You can enter genres, authors, artists, or specific titles.")
    preferences = input("Enter your preferences (separated by commas): ").split(",")
    recommended_items = recommend_items(preferences)
    if recommended_items:
        print("\nRecommended items based on your preferences:")
        for item in recommended_items:
            print(item)
    else:
        print("Sorry, no items match your preferences.")

if __name__ == "__main__":
    main()