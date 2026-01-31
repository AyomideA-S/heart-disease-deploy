# Use an official Python runtime as a parent image
FROM python:3.14

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# the first `.` refers to the host machine, the second `.` to the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Start backend server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]