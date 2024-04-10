\*\*\* Test Local:

Run ngrok to test webhook
ngrok http http://127.0.0.1.5000

curl -d '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
 -H "Content-Type: application/json" \
 -X POST http://127.0.0.1:5000/webhook

\*\*\* Test Prod

curl -d '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
 -H "Content-Type: application/json" \
 -X POST https://intake-form.onrender.com/webhook
