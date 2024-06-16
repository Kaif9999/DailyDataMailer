import logging
from web_scraper.scraper import WebScraper
from data_cleaner.cleaner import DataCleaner
from report_generator.generator import ReportGenerator
from notification_sender.notifier import Notifier

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting automation suite...")

    # Step 1: Scrape News
    logger.info("Starting web scraping...")
    scraper = WebScraper('https://www.creativebloq.com/web-design/best-blogging-platforms-121413634')
    headlines = scraper.scrape()
    if headlines:
        logger.info(f"Scraped {len(headlines)} headlines.")
    else:
        logger.error("Failed to scrape headlines.")
        return

    # Step 2: Clean Data
    logger.info("Starting data cleaning...")
    cleaner = DataCleaner('user_data.csv')
    try:
        cleaner.clean('cleaned_user_data.csv')
        logger.info("Data cleaning completed.")
    except Exception as e:
        logger.error(f"Data cleaning failed: {e}")
        return

    # Step 3: Generate Report
    logger.info("Starting report generation...")
    generator = ReportGenerator('sales_data.csv')
    try:
        generator.generate_report('monthly_sales_report.pdf')
        logger.info("Report generation completed.")
    except Exception as e:
        logger.error(f"Report generation failed: {e}")
        return

    # Step 4: Send Notification
    logger.info("Sending notification...")
    notifier = Notifier('youremail@example.com', 'yourpassword')
    subject = "Automation Suite Completed"
    body = "All tasks in the automation suite have been completed successfully."
    try:
        notifier.send_email(subject, body, 'recipient@example.com')
        logger.info("Notification sent.")
    except Exception as e:
        logger.error(f"Notification failed: {e}")
        return

    logger.info("Automation suite completed successfully.")

if __name__ == "__main__":
    main()
