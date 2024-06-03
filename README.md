# demo-bot
This project is a slack bot that uses the OpenAI API.

It demonstrates defining multiple custom tools that call out to APIs to retrieve product information and send emails.


## Setup

```
make install
```

### Environment Variables
Configure the following environment variables, either by setting them in the `.env` file or by setting them in the environment.

| Variable             | Description                                 |
|----------------------|---------------------------------------------|
| BOT_NAME             | The name of the bot                         |
| CATALOG_DATABASE_URL | The Postgres URL to the catalog database    |
| CATALOG_API_URL      | The URL to the catalog API                  |
| CATALOG_API_TOKEN    | The token for the catalog API               |
| EMAIL_API_URL        | The URL to the email API                    |
| EMAIL_API_TOKEN      | The token for the email API                 |
| OPENAI_API_KEY       | The OpenAI API key                          |
| OPENAI_ASSISTANT_ID  | The OpenAI assistant ID                     |
| SLACK_APP_TOKEN      | The Slack app token                         |
| SLACK_BOT_TOKEN      | The Slack bot token                         |
| SMTP_SERVER          | The SMTP server                             |
| SMTP_PORT            | The SMTP port                               |
| SMTP_USERNAME        | The SMTP username                           |
| SMTP_PASSWORD        | The SMTP password                           |
| SMTP_FROM_EMAIL      | The address that emails should be sent from |

### Creating/Updating the OpenAI Assistant

```bash
make update-assistant
``` 

## Running the Bot

Use `make run-demo-bot` to run the bot. You will also need to run the catalog and email APIs separately using `make run-catalog-api` and `make run-email-api`.

```bash
make run-catalog-api
```

```bash
make run-email-api
```

```bash
make run-demo-bot
```

