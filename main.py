# main.py
from analytics import clean_and_transform
from get_joined_data import get_joined_data

def main():
    # Fetch joined data
    df_joined = get_joined_data()
    
    # Clean and transform
    df_ready = clean_and_transform(df_joined)
    
    # Save to CSV
    df_ready.to_csv("final_analytics_ready.csv", index=False)

    print("Saved final_analytics_ready.csv successfully!")

if __name__ == "__main__":
    main()
