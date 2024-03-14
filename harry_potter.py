import os
import string

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}


# Step 1

# os.mkdir("Harry Potter")
os.chdir("Harry Potter")

forbidden_chars = ["\\", "/", ":", "|", "?", "*"]

# for title in films_titles["results"]:
#     for char in forbidden_chars:
#         if char in title["title"]:
#             title["title"] = title["title"].replace(char, "")
#     os.mkdir(title["title"])


# Step 2

letters = string.ascii_uppercase
potter_films_dirs = os.listdir()

# for title in potter_films_dirs:
#     for char in letters:
#         char_path = os.path.join(title, char)
#         os.mkdir(char_path)

print(os.listdir())
print(os.getcwd())
