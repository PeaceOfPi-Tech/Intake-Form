\*\* Run ngrok to test webhook
ngrok http http://127.0.0.1.5000

Test:
d
curl -d '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
 -H "Content-Type: application/json" \
 -X POST https://e985-99-43-16-59.ngrok-free.app/webhook

curl -d '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
 -H "Content-Type: application/json" \
 -X POST http://127.0.0.1:5000/webhook
