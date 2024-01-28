# Backend Requirement
## Data CRON service
1. Add CRON service to store latest data that we get from flood warning api https://api.data.gov.my/flood-warning/
2. Store the data to database (sqlite / mysql)
3. Make the CRON job performs every 1 hour

## API server
1. Create API server that allows browser from localhost:4200 to access (CORS)
2. API expectation
   1. GET /flood-warnings?state={state}&district={district}
   2. GET /flood-warnings/count/group-by?water_level_indicator=DANGER
