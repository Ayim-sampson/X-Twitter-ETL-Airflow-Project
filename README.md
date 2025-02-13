# 🌐 **X-Twitter-ETL-Airflow-Project** 

A simple ETL (Extract, Transform, Load) project that automates data collection from **Elon Musk's X (formerly known as Twitter)** page, processes the data, and stores it as a CSV file in an **Amazon S3** bucket using Python scripts and **Apache Airflow**.

## ✨ **Features**
- **Data Extraction:** Fetches tweets from Elon Musk's X page using the **Tweepy** library.
- **Data Transformation:** Cleans and structures the extracted data for meaningful analysis.
- **Data Loading:** Saves the transformed data as a CSV file and uploads it to an **Amazon S3** bucket for storage.
- **Automation with Airflow:** Schedules and monitors the entire ETL pipeline with **Apache Airflow**.

## 📁 **Project Files**
- `twitter_etl.py`: Handles data extraction and transformation using the Tweepy library.
- `x_etl.py`: Coordinates the ETL process logic.
- `x_dag.py`: Defines the Airflow DAG (Directed Acyclic Graph) to automate and orchestrate the ETL tasks.
- `elonmusk_twitter_data.csv`: Example CSV output storing the transformed tweet data.

## 🛠️ **Technologies Used**
- **Python**: For scripting and ETL logic.
- **Tweepy**: To fetch data from X (formerly Twitter).
- **Apache Airflow**: For workflow automation and scheduling.
- **Amazon S3**: To store the extracted data.
- **GitHub**: For version control.

## ⚙️ **Setup Instructions**
### *Prerequisites*
- Install **Python 3.10+** and **Apache Airflow**.
- Configure an **Amazon S3** bucket for data storage.
- Obtain **Twitter/X API credentials** from the developer portal.

### **Steps**
1. Clone this repository:
    ```bash
    git clone https://github.com/Ayim-sampson/X-Twitter-ETL-Airflow-Project.git
    cd X-Twitter-ETL-Airflow-Project
    ```
2. Install the required Python packages:
    ```bash
    pip install tweepy pandas boto3
    ```
3. Update the `twitter_etl.py` file with your Twitter API credentials and S3 bucket details.

4. Set up Airflow:
   - Initialize the database:
     ```bash
     airflow db init
     ```
   - Start the Airflow web server and scheduler:
     ```bash
     airflow webserver & airflow scheduler
     ```
5. Trigger the Airflow DAG to start the ETL pipeline.

---

🌟 **Contributions and Feedback are Welcome!** 🌟
