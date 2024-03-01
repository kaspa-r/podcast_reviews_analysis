# karutka-DA.1.5

# Podcast Reviews Analysis

## Foreground

The analysis concerns a podcast reviews dataset ranging in review dates from `2005-12-09` to `2023-02-16`. The study pertains specifically to the number, rating, sentiment (positivity) & proportion of positive reviews of the Top 20 categories of podcasts by review count. We also only create a customary Looker Studio dashboard to accompany the Exploratory Data Analysis by focusing on the data-related aspect of the podcast reviews dataset : https://lookerstudio.google.com/s/j-DUSmh90NU.

The analysis dives deeper into statistical inference by asking 6 major groups of questions based on the exploratory data analsysis section within the Jupyter Notebook.

## Table of Contents

* Executive Summary
* Data Extraction & Preparation
* Feature Engineering
* Exploratory Data Analysis
* Questions to be Answered
* Conclusions
* Potential Improvements

## Tables Used

The dataset used for this analysis comes from a sqlite database of `4 tables`:

`Runs` table:
* `run_at` - run date of when the has been pulled
* `max_rowid` - thtimee highest rowid at run time
* `reviews_added` - the number of reviews added on the specific run
 
`Podcasts` table:
* `Podcast_id` - Primary key for each podcast
* `Itunes_id` - unique identifier for a podcast generate by iTunes (the source of the data)
* `Slug` - shortened version of the title of the podcast
* `Itunes_URL` - the URL that the podcast was pulled from
* `Title` - title of the podcast

`Categories` table:
* `Podcast_id` - Foreign key used to link each podcast from the `podcast` table with a specific category
* `Category` - a set of categories that each podcast represents

`Reviews` table:
* `Podcast_id` - Foreign key used to link each review to each podcast in the `podcast` table
* `Title` - title given to the review by the author
* `Content` - text within th review
* `Rating` - rating given by the author in the review to the podcast
* `Author_id` - the author_id that wrote the review for a podcast
* `Created` - date and time at which the review was written


The tables are thus linked in this format:
* `Podcast_id` (Primary Key in `Podcasts`) <===> `Podcast_id` (Foreign Key in `Categories`)
* `Podcast_id` (Primary Key in `Podcasts`) <===> `Podcast_id` (Foreign Key in `Reviews`)


## Conclusions made: 
* `Society-culture` Podcasts Analysis
    * With 95% confidence, we can specify that the true population of the mean sentiment compound score for `Society-culture` podcasts is between `0.5858843807976221` & `0.5946764504135423`. 
* `History` - `Science` Podcasts comparison
    * The difference between the mean `ratings` of podcasts specializing towards `history` and `science` is insignificant.
    * The true population mean `compound sentiment scores` between podcasts specializing towards `history` and `science` is different.
    * The true population proportions of positive reviews between podcasts specializing towards `history` and `science` is the same and falls on ~82-86%.
* `News` Podcast Negativity
    * `News` podcasts gather lower proportions of `positive` reviews than other podcast categories on average.
    * The true population mean `sentiment compound score` for `news` podcasts is `smaller` than the true population mean sentiment compound score for `other podcast categories`.
* `Comedy` Podcast Positivity
    * `Comedy` podcasts DO NOT gather the highest proportion of `positive` reviews compared to other categories on average.
    * The true population `sentiment compound score` for `comedy` podcasts is `lower` than the true population sentiment score for the `health podcast` category on average.
* `Adult-centric` vs `Child-centric` Education Podcasts
    * The true population mean `ratings` of `adult-centric` educational podcasts are `higher` than that of `children-centric` educational podcasts.
    * The true population mean `compound sensitivity scores` of `adult-centric` educational podcasts is `higher` than that of children-centric educational podcasts.
    * `Adult-centric` educational podcasts gather `higher` proportions of `positive` reviews than `children-centric` educational podcasts on average.
* `Business` Podcasts Subcategories
    * The true population `rating` for general `business` podcasts is `LOWER` than the true population average rating for other `sub-categorized business podcasts`.
    * With 95% confidence, the best performing `business` category podcasts are ones that have the sub-category `management`. 
