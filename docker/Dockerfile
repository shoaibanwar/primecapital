FROM python:3.12-slim

# Working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    build-essential \
    && apt-get clean


# Copy the requirements file into the container
COPY ../src/requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#COPY ../src /app

EXPOSE 5000

# Copy the db seed file into the container
COPY ../src/populate_db.py /app/

# Populate the database
#RUN python populate_db.py

# Run the application
CMD ["python", "app.py"]