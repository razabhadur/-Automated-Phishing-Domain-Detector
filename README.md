# Automated Phishing Domain Detector

This tool is designed to automatically detect potential phishing domains based on various criteria such as common misspellings, homoglyphs, recent domain registration, content analysis, and more.

## Features

- Domain Generation: Generates potential phishing domains based on common misspellings and homoglyphs.
- Content Analysis: Checks for common phishing keywords in the content of the domain.
- SSL Certificate Verification: Checks if the domain has a valid SSL certificate.
- Domain Age Calculation: Calculates and displays the age of flagged domains.
- User-Agent Spoofing: Sets a user-agent that mimics a popular browser to potentially bypass restrictions set by some websites.
- Blacklist Check: Checks if a domain is blacklisted.
- Redirect Check: Checks if a domain redirects to another URL.
- Interactive Mode: Allows the user to input a domain directly into the console for checks.
- Parallel Processing: Processes multiple domains concurrently for faster checks.

## Usage

1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```
   pip install requests whois bs4
   ```
3. Run the script:
   ```
   python phishing_domain_detector.py
   ```
4. Choose the mode of operation:
   - Enter 1 for default mode.
   - Enter 2 for interactive mode, where you can input a domain to check.

## Configuration

You can modify the configuration options at the beginning of the script to customize the behavior:

- LOG_FILE_PATH: Path for the log file.
- RECENT_REGISTRATION_DAYS: Number of days to consider for recent domain registration.
- MAX_WORKERS: Maximum number of worker threads for parallel processing.
- REQUEST_TIMEOUT: Timeout for domain requests.
- USER_AGENT: User-agent string for requests.
- BLACKLIST_URL: URL of the blacklist service to check domains against.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or add new features.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational purposes only. Always seek permission before conducting any security testing.
