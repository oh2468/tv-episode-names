import re

if __name__ == "__main__":
    invalid_chars = r'\\/:;*?"<>|'
    replacement = "_"
    file_name = "names.txt"

    with open(file_name, "r", encoding="UTF-8") as file:
        episodes = file.read()
    
    if episodes.startswith("mv -v -i -- "):
        print("\n  ---  THE EPISODES HAVE ALREADY BEEN RENAMED...  ---  ")
        raise SystemExit(0)
    
    episodes = re.sub(f"[{invalid_chars}]", replacement, episodes)

    len_wo_name = episodes.find("s01e01") + 6
    end = ".mp4"

    new_names = [f'mv -v -i -- "{ep[:len_wo_name]}{end}" "{ep}{end}"' for ep in episodes.splitlines()]

    with open(file_name, "w", encoding="UTF-8") as file:
        file.write("\n".join(new_names))

    print(f"Done renameing the show: {episodes[:len_wo_name - 7]}")
