# Base image
FROM python:3.10-slim
# Set the working directory
WORKDIR /is-final/is-final
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code
COPY . .
# Expose the gRPC port
EXPOSE 50051
# Start the gRPC server
CMD ["python", "main.py"]
