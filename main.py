from colorama import Fore, Style, init

init()

class NovaLogger:
    """
    Terminal Custom Colored Logger
    Provides visually stunning debugging and status reports.
    """
    @staticmethod
    def success(message):
        print(f"{Fore.GREEN}✔ SUCCESS: {message}{Style.RESET_ALL}")

    @staticmethod
    def error(message):
        print(f"{Fore.RED}✘ ERROR: {message}{Style.RESET_ALL}")

if __name__ == "__main__":
    logger = NovaLogger()
    logger.success("Build compiled successfully.")
    logger.error("Vulnerability check failed.")
