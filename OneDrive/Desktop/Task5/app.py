from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis-container")  # Use container name as hostname
redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def visits():
    count = redis_client.incr('counter')  # Increment visit count
    return f'Hello! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
