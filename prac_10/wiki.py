import wikipedia

def main():
    """Program to search a page on wikipedia and print title, summary and url."""
    title  = input("Enter a search page: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page id {title} does not match any pages. Try another id!")
        title = input("Enter a search term: ")

main()
