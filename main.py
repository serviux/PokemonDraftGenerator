import pandas as pd
from find_pokemon_names import get_names
from get_legendary_pokemon import *
from config import Config


def construct_df():
    names = get_names()
    data = [{"name": name} for name in names]
    df = pd.DataFrame(data)
    df.set_index("name")
    return df


def apply_tags(df):
    soup = get_page(SEREBII_URL)

    legendaries = get_legendaries(soup)
    mythicals = get_mythicals(soup)
    sub_legendaries = get_sub_legendaries(soup)
    ultra_beasts = get_ultra_beasts(soup)

    def __map(x):
        if x in legendaries:
            return "legendary"
        elif x in mythicals:
            return "mythical"
        elif x in sub_legendaries:
            return "sub_legendary"
        elif x in ultra_beasts:
            return "ultra_beast"
        else:
            return "pokemon"

    pokemon_tags = []
    for name in df["name"]:
        tag = __map(name)
        pokemon_tags.append(tag)

    df["pokemon_category"] = pokemon_tags
    return df


def make_draft(df):
    bools = ~df["pokemon_category"].isin(Config.DONT_USE)
    filtered = df[bools]
    sample = filtered.sample(n=Config.SAMPLE_SIZE)
    sample.to_csv(Config.OUT_FILE, index=False)
    print(f"File saved to {Config.OUT_FILE}")


def main():
    df = construct_df()
    df = apply_tags(df)
    make_draft(df)


if __name__ == "__main__":
    main()
