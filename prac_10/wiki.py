import wikipedia


def main():
    # allows users to search for a Wikipedia page by entering a title.
    title = input("Enter page title: ")
    while title != "":
        try:

            search_results = wikipedia.search(title)
            if not search_results:
                print(f'Page id "{title}" does not match any pages. Try another id!')
            else:

                page = wikipedia.page(search_results[0])
                print(f'{page.title}')
                print(f'{wikipedia.summary(page.title)}')
                print(f'{page.url}')
        except wikipedia.exceptions.DisambiguationError as e:

            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        title = input("Enter page title: ")
    print("Thank you.")

main()
