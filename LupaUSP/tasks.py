import celery
app = Celery('example')

@app.task
def add(x, y):
    return x + y