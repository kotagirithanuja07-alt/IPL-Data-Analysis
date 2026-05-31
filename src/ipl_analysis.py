import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# IPL DATA ANALYSIS PROJECT
# --------------------------------------------------

sns.set_style("whitegrid")

# Load Dataset
try:
    df = pd.read_csv("data/matches.csv")
except FileNotFoundError:
    print("Dataset not found. Place matches.csv inside the data folder.")
    exit()

print("=" * 60)
print("IPL DATA ANALYSIS PROJECT")
print("=" * 60)

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# DATA CLEANING
# --------------------------------------------------

df.drop_duplicates(inplace=True)

if "winner" in df.columns:
    df = df[df["winner"].notna()]

print("\nShape After Cleaning:")
print(df.shape)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

print("\nKEY INSIGHTS")
print("-" * 40)

total_matches = len(df)
total_seasons = df["season"].nunique()

print(f"Total Matches: {total_matches}")
print(f"Total Seasons: {total_seasons}")

# --------------------------------------------------
# TEAM PERFORMANCE ANALYSIS
# --------------------------------------------------

team_wins = df["winner"].value_counts()

print("\nTop 10 Teams By Wins")
print(team_wins.head(10))

plt.figure(figsize=(12,6))
sns.barplot(
    x=team_wins.head(10).values,
    y=team_wins.head(10).index
)
plt.title("Top 10 IPL Teams by Match Wins")
plt.xlabel("Wins")
plt.ylabel("Teams")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# PLAYER OF MATCH ANALYSIS
# --------------------------------------------------

player_awards = (
    df["player_of_match"]
    .value_counts()
    .head(10)
)

print("\nTop Players of the Match")
print(player_awards)

plt.figure(figsize=(12,6))
sns.barplot(
    x=player_awards.values,
    y=player_awards.index
)
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# TOSS ANALYSIS
# --------------------------------------------------

toss_decision = df["toss_decision"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    toss_decision.values,
    labels=toss_decision.index,
    autopct="%1.1f%%"
)
plt.title("Toss Decision Distribution")
plt.show()

# --------------------------------------------------
# TOSS WINNER VS MATCH WINNER
# --------------------------------------------------

same_result = df[df["toss_winner"] == df["winner"]]

percentage = round(
    len(same_result) / len(df) * 100,
    2
)

print(f"\nToss Winner Won Match: {percentage}%")

# --------------------------------------------------
# VENUE ANALYSIS
# --------------------------------------------------

top_venues = df["venue"].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(
    x=top_venues.values,
    y=top_venues.index
)
plt.title("Top IPL Venues")
plt.xlabel("Matches Hosted")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# CITY ANALYSIS
# --------------------------------------------------

if "city" in df.columns:

    city_matches = (
        df["city"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(12,6))
    sns.barplot(
        x=city_matches.values,
        y=city_matches.index
    )

    plt.title("Top IPL Host Cities")
    plt.xlabel("Matches")
    plt.ylabel("City")
    plt.tight_layout()
    plt.show()

# --------------------------------------------------
# SEASON ANALYSIS
# --------------------------------------------------

season_matches = (
    df.groupby("season")
    .size()
)

plt.figure(figsize=(12,6))
plt.plot(
    season_matches.index,
    season_matches.values,
    marker="o"
)

plt.title("Matches Played Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# CHAMPION ANALYSIS
# --------------------------------------------------

season_winners = (
    df.groupby("season")["winner"]
    .last()
)

print("\nSeason Winners")
print(season_winners)

# --------------------------------------------------
# EXPORT SUMMARY REPORT
# --------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Total Matches",
        "Total Seasons",
        "Top Team"
    ],
    "Value": [
        total_matches,
        total_seasons,
        team_wins.idxmax()
    ]
})

summary.to_csv(
    "ipl_summary_report.csv",
    index=False
)

print("\nSummary report saved as:")
print("ipl_summary_report.csv")

print("\nAnalysis Completed Successfully")
