import logging

# Standard logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class DataProcessor:
    """A professional utility for data sanitization and processing."""
    
    def __init__(self, data_source):
        self.data_source = data_source
        self.cleaned_data = []

    def process(self):
        logger.info("Starting data processing workflow...")
        if not self.data_source:
            logger.warning("Data source is empty.")
            return []
        
        # Clean whitespace and standardize strings
        self.cleaned_data = [
            str(item).strip().capitalize() 
            for item in self.data_source 
            if item is not None
        ]
        return self.cleaned_data

if __name__ == "__main__":
    # Example dataset for demonstration
    sample_input = [" python ", " javascript", None, "react ", " sql"]
    
    processor = DataProcessor(sample_input)
    results = processor.process()
    
    print(f"Final Output: {results}")
