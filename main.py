
from recommender.Vtest import Vtest

def main():
    recommender = Vtest("data/outfits.csv")
    print("Recommendations for color='Red', occasion='Party':")
    print(recommender.recommend(color='Red', occasion='Party'))

if __name__ == "__main__":
    main()
