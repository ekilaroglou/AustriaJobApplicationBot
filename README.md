# AustriaJobApplicationBot

AustriaJobApplicationBot is a Python-based automation tool that sends job applications to positions listed on the [Paznaun-Ischgl job portal](https://www.paznaun-ischgl.com/en/crew/jobs/jobs). It simplifies the process of applying to multiple positions by automating the submission of your CV and application details.

## Features
- Takes a URL with filters applied from the Paznaun-Ischgl job portal.
- Automates job applications for all job listings in the specified query.
- Configurable via a `config.json` file for user details and application settings.
- Attachments like CVs are organized in an `Attachments` folder.


## How to Use

1. **Prepare the URL with Filters**:
   - Go to the [Paznaun-Ischgl job portal](https://www.paznaun-ischgl.com/en/crew/jobs/jobs).
   - Apply any desired filters (e.g., job category, employment type, region, etc.).
   - Copy the URL with the query parameters.

2. **Update the `config.json` File**:
   - Paste the filtered URL into the `url` field of the `config.json` file.
   - Fill in the other fields such as your name, email, phone number, address, and cover letter text.

3. **Add Attachments**:
   - Place your CV and other required files in the `Attachments/` folder.
   - Ensure file names are descriptive (e.g., `CV.pdf`).

4. **Run the Bot**:
   - Install Requirements:
        You'll need to install selenium and a compatible webdriver.
   - Execute the bot:
     ```bash
     python main.py
     ```

5. **Application Process**:
   - The bot will automatically send your CV and application details to all job listings matching the query parameters in the URL.

## Configuration
Below is an example of the `config.json` file:

```json
{
    "url": "Your filtered URL from the job portal",
    "salutation": "Mr/Mrs/Other",
    "first_name": "Your first name",
    "last_name": "Your last name",
    "date_of_birth": "YYYY-MM-DD",
    "phone": "Your phone number",
    "email": "Your email",
    "street": "Your street address",
    "street_number": "Your house/apartment number",
    "zip": "Your postal code",
    "city": "Your city",
    "country": "Your country",
    "cover_letter": "Your cover letter text"
}
```

## Notes

- Ensure you have the correct WebDriver installed for your browser.

