def process_data(filename):
  champions = {}
  countries = set()
  with open(filename, "r", encoding="utf-8-sig") as f:
    for line in f:
      year, country, champion, _ = line.strip().split(", ")
      champions.setdefault(champion, 0)
      champions[champion] += 1
      countries.add(country)
  return champions, countries

def main():
  filename = "wimbledon.csv"
  champions, countries = process_data(filename)
  print("Wimbledon Champions:")
  for champion, count in sorted(champions.items()):
    print(f"{champion}: {count}")
  print("\nThese", len(countries), "countries have won Wimbledon:")
  print(", ".join(sorted(countries)))

if __name__ == "__main__":
  main()