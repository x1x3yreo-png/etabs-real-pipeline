import logging
from src.etabs.pipeline import ETABSPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    pipeline = ETABSPipeline(
        input_dir="data/input",
        output_dir="data/output"
    )
    result = pipeline.run()
    print(result)

if __name__ == "__main__":
    main()