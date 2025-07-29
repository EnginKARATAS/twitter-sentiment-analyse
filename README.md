# Twitter Sentiment Analysis and Visualization Project

This project aims to develop a real-time sentiment analysis system that processes Twitter data and visualizes the results through interactive dashboards and geographic mapping.

## 📋 Project Overview

![image](https://github.com/user-attachments/assets/7747bd8f-4716-43d7-9dbe-5ed5da2d721f)

![image](https://github.com/user-attachments/assets/ff178038-dbae-4933-80dd-6f172480e8b1)

An automated system that analyzes tweets about specific topics, classifies user emotional responses as positive, negative, or neutral, and visualizes the results through interactive charts and world maps. The project focuses on analyzing public sentiment regarding major events like the Ukraine-Russia conflict and economic indicators.

## 🎯 Objectives

- Extract large-scale data from Twitter using APIs
- Process and analyze sentiment using data mining techniques
- Create meaningful visualizations and real-time analytics
- Provide geographic sentiment mapping capabilities

## 🛠️ Technology Stack

### Core Technologies
- **Python**: Main programming language for data processing and sentiment analysis
- **Twitter API**: Data extraction via Tweepy library
- **TextBlob**: Natural language processing and sentiment analysis
- **Elastic Search**: NoSQL database for storing and indexing tweet data
- **Kibana**: Real-time data visualization and dashboard creation
- **AWS EC2**: Cloud infrastructure for hosting the application

### Key Libraries
- `tweepy` - Twitter API integration
- `textblob` - Sentiment analysis
- `elasticsearch-py` - Database operations
- `geopy` - Geographic coordinate conversion
- `pandas` - Data manipulation and preprocessing
- `re` - Text preprocessing with regular expressions

## 🏗️ System Architecture

1. **Data Collection**: Real-time tweet streaming using Twitter API
2. **Data Preprocessing**: Text cleaning and standardization
3. **Sentiment Analysis**: Classification using TextBlob polarity scores
4. **Geographic Processing**: Location extraction and coordinate conversion
5. **Data Storage**: Indexing in Elasticsearch with proper mapping
6. **Visualization**: Interactive dashboards and maps via Kibana

## 📊 Analytics Features

### Dashboard Visualizations
![8](https://github.com/user-attachments/assets/ce4d9ac4-f523-44bd-9f6a-40b687883a7e)

![21](https://github.com/user-attachments/assets/5477c0b0-65ca-4da3-845e-ccd113642503)

- Tweet volume by location
- Sentiment distribution (positive/negative/neutral)
- Geographic sentiment mapping
- Time-series analysis of sentiment trends
- Top locations by follower count
- Message intensity distribution

### Geographic Mapping
- World map visualization of sentiment data
- Country and region-based sentiment analysis
- Real-time geographic sentiment tracking

## 🔍 Case Study: Ukraine Crisis Analysis

The system was tested by analyzing sentiment around the Ukraine-Russia conflict across different time periods:

- **May 3-5, 2022**: 84,114 tweets analyzed
- **May 10-12, 2022**: 32,000 tweets analyzed  
- **June 17, 2022**: 8,951 tweets analyzed

### Key Findings
- Limited Turkish engagement on Ukraine topics
- High negative sentiment in UK and Spain
- Significant tweet volume across European locations
- Notable activity concentration in specific African regions (Togo)

## 🚀 Implementation Highlights

### Real-time Processing
```python
class TweetStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        # Process tweet data
        # Perform sentiment analysis
        # Extract geographic coordinates
        # Store in Elasticsearch
```

### Sentiment Classification
- **Positive**: Polarity score > 0
- **Negative**: Polarity score < 0  
- **Neutral**: Polarity score = 0

### Geographic Integration
- Location text extraction from user profiles
- Coordinate conversion using Nominatim API
- Geo-point mapping for Kibana visualization

## 📦 Installation and Setup

### Prerequisites
- Python 3.7+
- Twitter Developer Account
- Elasticsearch Cloud instance
- AWS EC2 instance (optional)

### Environment Variables
Create a `.env` file with the following variables:
```env
# Twitter API
api_key=your_twitter_api_key
api_key_secret=your_twitter_api_secret
access_token=your_access_token
access_token_secret=your_access_token_secret

# Elasticsearch
cloud_id=your_elasticsearch_cloud_id
user=your_elasticsearch_username
password=your_elasticsearch_password
```

### Installation
```bash
pip install tweepy textblob elasticsearch geopy pandas
```

# Twitter Sentiment Analysis Thesis - Key Conclusions

## Research Overview
This thesis, conducted by Engin Karataş at Yozgat Bozok University, focused on implementing sentiment analysis and visualization of Twitter data using modern data science technologies including Python, Elastic Search, Kibana, and AWS cloud services.

## Technical Implementation Achievements

### 1. Data Collection and Processing
- Successfully implemented real-time Twitter data collection using Twitter API and Tweepy library
- Developed automated data preprocessing pipeline using Python and regular expressions
- Achieved processing of up to 2 million tweets monthly (Twitter hobby account limit)

### 2. Sentiment Analysis Implementation
- Utilized TextBlob library for sentiment classification
- Classified tweets into three categories: positive, negative, and neutral
- Implemented polarity scoring system ranging from -1 (negative) to +1 (positive)

### 3. Geographic Data Integration
- Successfully integrated geolocation data using Geopy library
- Converted location names to latitude/longitude coordinates
- Enabled geographic visualization of sentiment patterns

### 4. Data Storage and Visualization
- Implemented Elastic Search as NoSQL database for efficient data storage and retrieval
- Created real-time dashboards using Kibana for data visualization
- Developed multiple visualization types including bar charts, pie charts, and world maps

## Case Study Results

### Ukraine-Russia War Analysis
**Data Analyzed:** Multiple time periods (May 3-5, May 10-12, June 17, 2022)
**Total Records:** Over 125,000 tweets analyzed

**Key Findings:**
- Limited Turkish participation in Ukraine war discussions on Twitter
- High negative sentiment concentration in UK and Spain
- Significant tweet volume across European regions, particularly in UK
- Notable activity in African countries, especially Togo

### Turkish Lira Exchange Rate Analysis
**Key Findings:**
- High concentration of tweets from Turkey (as expected for Turkish-language hashtag)
- Predominantly negative sentiment regarding exchange rate discussions
- Clear correlation between economic concerns and negative sentiment

## Technical Contributions

### 1. Real-time Processing Pipeline
- Developed end-to-end pipeline from data collection to visualization
- Implemented stream processing for live sentiment analysis
- Created automated data quality checks and preprocessing

### 2. Geographic Sentiment Mapping
- Successfully mapped sentiment data to world coordinates
- Enabled regional sentiment analysis capabilities
- Provided location-based filtering and analysis tools

### 3. Scalable Architecture
- Utilized cloud infrastructure (AWS EC2) for processing
- Implemented distributed data storage with Elastic Search
- Created scalable visualization platform with Kibana

## Research Impact and Applications

### 1. Social Media Monitoring
- Demonstrated effectiveness for real-time public opinion tracking
- Provided tools for crisis communication monitoring
- Enabled geographic sentiment analysis for global events

### 2. Data Science Methodology
- Integrated multiple technologies (Python, ELK Stack, AWS) effectively
- Created open-source solution for academic research

### 3. Visualization Innovation
- Developed interactive dashboards for real-time sentiment monitoring
- Created geographic heat maps for sentiment distribution
- Implemented filtering capabilities for temporal and spatial analysis

## Technical Specifications

### Data Processing Capabilities
- **Volume:** Up to 2 million tweets per month
- **Languages:** Multi-language support with translation capabilities
- **Real-time Processing:** Near real-time sentiment classification
- **Storage:** NoSQL database with full-text search capabilities

### Visualization Features
- Location-based record counts
- Total tweet statistics
- Average sentiment analysis values
- Positive/negative tweet ratios
- Country and location-based sentiment analysis
- Intensity-based location, author, and message tables
- Distribution graphs of intensity values
- Top follower count locations

## Limitations and Considerations

### 1. Data Limitations
- Restricted to Twitter hobby account limits (2M tweets/month)
- Dependent on user-provided location data accuracy
- Limited to publicly available tweets

### 2. Technical Constraints
- Sentiment analysis accuracy dependent on TextBlob algorithm
- Geographic mapping limited to location data availability
- Real-time processing constrained by API rate limits

## Future Research Directions

### 1. Enhanced Analytics
- Integration of machine learning models for improved sentiment accuracy
- Implementation of emotion detection beyond positive/negative classification
- Development of trend prediction capabilities

### 2. Expanded Data Sources
- Integration with other social media platforms
- Incorporation of news media sentiment analysis
- Cross-platform sentiment correlation studies

### 3. Advanced Visualization
- Development of predictive sentiment models
- Implementation of anomaly detection for unusual sentiment patterns
- Creation of automated alert systems for significant sentiment changes

## Conclusion

This research successfully demonstrates the feasibility and effectiveness of implementing a comprehensive Twitter sentiment analysis system using modern data science technologies. The project provides valuable insights into public opinion patterns during significant global events and establishes a reusable framework for future social media sentiment analysis research.

The integration of real-time data processing, sentiment analysis, geographic mapping, and interactive visualization creates a powerful tool for understanding public sentiment at scale. The findings from the Ukraine-Russia war and Turkish Lira exchange rate analyses demonstrate the system's capability to provide meaningful insights into public opinion dynamics across different geographic regions and topics.

The open-source nature of the implementation and detailed documentation provided in this thesis contribute to the academic community's resources for social media research and sentiment analysis methodologies.

![3](https://github.com/user-attachments/assets/e24de8fe-5a16-467c-b7d5-5549114e7dc1)
![20](https://github.com/user-attachments/assets/8d17ed91-e450-4a3b-9a90-614f4b07957c)
![19](https://github.com/user-attachments/assets/1e19935e-7ce6-4e1a-a38f-a9c6a60610d5)

![18](https://github.com/user-attachments/assets/c1ef20e6-da2e-45e2-a500-eb1d499898c7)
![17](https://github.com/user-attachments/assets/dab84110-f97f-4427-9d57-8205f5a52c53)
![16](https://github.com/user-attachments/assets/e2f373db-f21c-42d0-b705-69aefed99313)
![15](https://github.com/user-attachments/assets/883587f5-4c1f-45d1-8b93-86c9876d2a02)
![14](https://github.com/user-attachments/assets/d0ceedb8-ecf0-4d9c-b4a7-ba754a9f6835)
![13](https://github.com/user-attachments/assets/2252f439-2b5d-44c3-9996-d77869ba8722)
![12](https://github.com/user-attachments/assets/4237053d-ed45-4d38-bb48-565c347d1a64)
![11](https://github.com/user-attachments/assets/4ee9f42f-d124-4852-ba7b-7540422700f1)

![10](https://github.com/user-attachments/assets/2d1ea243-1724-46bc-9e11-1c71d0bddfd1)
![9](https://github.com/user-attachments/assets/36468a9f-34d6-497e-b4f7-54d03aa956b2)



## 🔒 Security Features

- Environment variable protection for API keys
- Secure cloud deployment on AWS
- SSH protocol for secure server access
- API rate limiting compliance

## 📖 Usage

1. Set up your environment variables
2. Configure Twitter API credentials
3. Set up Elasticsearch instance
4. Run the main Python script to start streaming tweets
5. Access Kibana dashboard for real-time visualization

## 🤝 Contributing

This project serves as a foundation for researchers and developers interested in social media sentiment analysis. Contributions and improvements are welcome.

## 📄 License

This project was developed for academic purposes as part of a graduation thesis.

## 🎓 Academic Context

This project was developed as a graduation thesis at Yozgat Bozok University, Computer Engineering Department, supervised by Assoc. Prof. Dr. Mehmet Bakır.

**Author**: Engin Karataş (Student ID: 16008118040)  
**Year**: 2022

---

*This system provides a foundation for researchers, data scientists, and organizations to conduct objective sentiment analysis on social media data with geographic context and real-time visualization capabilities.

![7](https://github.com/user-attachments/assets/dd2a4665-16f6-4bd1-aabd-81b7a2093513)
![6](https://github.com/user-attachments/assets/c85e5d24-ccbe-47c3-9446-700a067e5252)
![5](https://github.com/user-attachments/assets/38235e26-c46f-4d4e-a5bd-f683db3c582c)
![4](https://github.com/user-attachments/assets/d4dddbe2-01f4-463f-9419-34a74bbad0f2)

