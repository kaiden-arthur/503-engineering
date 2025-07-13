# FFXIV Job Balance in Early Dawntrail
### MSDS DATA 503 final project

This project was done for my Data Engineering course as part of my MSDS curriculum. It involved collecting data from an API as JSON files and processing it to produce an analysis, which was then compared to the visuals from the original data source. 

For a number of reasons, the scope of this project did not pan out as it was originally concepted. In the end I consider it a reasonable analysis and a fantastic learning opportunity, but there were a number of stumbling points along the way that meant I had to pare the project down as I went. 

#### Original Concept 
The MMORPG Final Fantasy XIV (FFXIV) released its most recent expansion, Dawntrail, in July of 2024. This expansion came with two new playable classes, one of which was incredibly overpowered on release--and stayed that way for much of the early release cycle. 

I wanted to use data available through the FFLogs website and API to compare class performance on Dawntrail's release with class performance after substantial rebalancing was done. The plan was to select data from the first week of two comparable endgame raid series, one before the rebalance and one after. The first week was a control effort made to account for things like variable gear access over time that would result in a wider range of performance statistics. The FFLogs website does not allow for specific filtering by date when displaying performance graphs, so I turned to the API. I also webscraped information from the official FFXIV website. 

#### Workflow and Skills Used 

This project required use of a number of skills that were unique to the class and the project: 
- SQL database construction and data ingestion
- API access using queries in Postman and Python
- JSON file manipulation in R
- Webscraping using Webscraper.io

...as well as a few I had prior experience with: 
- String wrangling in R
- GGPlot data visualizations 

#### Final Results 

The final output of this project was a much smaller dataset than I originally anticipated, due to API queries not returning information filtered to my queries as well as JSON string parsing issues. However, I was still able to construct a database that looked as I had originally concepted it, though with less data than expected. After I had re-filtered the data to what I was actually interested in, I was able to reconstruct the graphs I was interested in, which were comparable to those displayed (for different time frames) on the FFLogs website. While I was unable to get all the data I was interested in in the timeframe available for this project, I was able to make a relatively successful analysis and demonstrate my database construction and population skills. 

Project presentation video is available on YouTube: https://youtu.be/9QTIdb-jhLg. 
