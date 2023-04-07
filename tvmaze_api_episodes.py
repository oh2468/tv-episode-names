import sys
import urllib.request as request
import urllib.parse as parse
import json


headers = {
    "User-Agent":  "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
}

base_url = "https://api.tvmaze.com"
search_endpoint = "/search/shows?q={query}"
episode_endpoint = "/shows/{id}/episodes"

default_outfile = "names.txt"


def request_builder(url):
    return request.Request(url, None, headers)


def shut_it_down():
    print("\n  *******  NOT SHUTTING DOWN  *******  \n")
    sys.exit(0)


def get_user_input(input_msg):
    user_input = input(input_msg).lower()
    
    if user_input == "0":
        shut_it_down()
    
    return user_input


def validate_input(msg):
    choices = ["y", "n"]
    choice = get_user_input(f"{msg} (y/n): ")
    return choice == "y" if choice in choices else validate_input(msg)


def get_show_name():
    return get_user_input("Enter a show name: ")


def search_show(show_name):
    req = request_builder(base_url + search_endpoint.format(query=parse.quote(show_name)))
    with request.urlopen(req) as resp:
        return json.loads(resp.read())


def select_show(search, shows):
    if not shows:
        print(f" -- NO SHOWS WERE FOUND FOR SEARCH: {search}")
        shut_it_down()


    print(f" -- Found shows based on the search: {search}")
    print("\n0: SHOW ISN'T IN THE LIST, EXIT AND RESEARCH!")

    for i, show in enumerate(shows, start=1):
        show = show["show"]
        name = show["name"]
        start = s.split("-")[0] if (s := show["premiered"]) else ""
        end = s.split("-")[0] if (s := show["ended"]) else ""
        descr = s[3:-4] if (s := show["summary"]) else ""
        print(f"{i}:\t{name},\t({start} - {end}),\t{descr}")

    print()
    show_index = int(get_user_input("Enter the number of the show: "))
    show = shows[show_index - 1]["show"]
    return (show["name"], show["id"])


def get_episodes(show_id):
    req = request_builder(base_url + episode_endpoint.format(id=show_id))
    with request.urlopen(req) as resp:
        return json.loads(resp.read().decode("UTF-8"))


def parse_episodes(show_name, episodes):
    named_episodes = []
    
    for episode in episodes:
        ep_name = episode["name"]
        season = f"0{n}" if (n := episode["season"]) < 10 else n
        number = f"0{n}" if (n := episode["number"]) < 10 else n
        named = f"{show_name} s{season}e{number} {ep_name}"
        print(named)
        named_episodes.append(named)

    return named_episodes


def save_output_to_file(episode_names):
    choice = get_user_input("Do you want to save the episodes to a file? (y/n): ").lower()

    if choice != "y":
        print("Nothing is written to file...")
        return

    file_name = get_user_input("Enter a file name: ") + ".txt"
    file_name = default_outfile if file_name == ".txt" else file_name

    with open(file_name, "w", encoding="UTF-8") as out_file:
        out_file.write("\n".join(episode_names))
    
    print(f"Episodes now written to: {file_name}")


if __name__ == "__main__":
    print("IF ANY INPUT EQUALS: 0 THE PROGRAM IS TERMINATED!")

    show_search = get_show_name()
    found_shows = search_show(show_search)
    show_name, show_id = select_show(show_search, found_shows)
    episodes = get_episodes(show_id)
    parsed_eps = parse_episodes(show_name, episodes)
    save_output_to_file(parsed_eps)

    print("PROGRAM IS NOW FINISHED!")