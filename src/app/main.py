from src.config.settings import Settings
from src.pipeline.orchestrator import Orchestrator

def main():
    settings = Settings()
    orchestrator = Orchestrator(settings)
    result = orchestrator.run()
    print(result)

if __name__ == "__main__":
    main()