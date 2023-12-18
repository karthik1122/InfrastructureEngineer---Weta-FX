# Use Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY Renumber-image-sequences.py /app/

# Copy the 'photos' folder into the container
COPY photos /app/photos/

# Set permissions to make script.py executable
RUN chmod +x /app/Renumber-image-sequences.py

# Set permissions to make the 'photos' folder and its contents executable
RUN chmod -R +x /app/photos/

# Command to run the Python script when the container starts
CMD ["python", "Renumber-image-sequences.py"]
