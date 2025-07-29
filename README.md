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

## 📈 Results and Impact

The system successfully demonstrates:
- Automated large-scale sentiment analysis capabilities
- Real-time geographic sentiment tracking
- Interactive data exploration through dashboards
- Objective analysis reducing human bias in sentiment assessment

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

*This system provides a foundation for researchers, data scientists, and organizations to conduct objective sentiment analysis on social media data with geographic context and real-time visualization capabilities.*
