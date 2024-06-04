# Use the official Python image as base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "chemical_lab.py"]
