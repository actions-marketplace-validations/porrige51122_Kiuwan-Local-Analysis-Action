# Image that contains both Java and Python in a Unix container
# Needs to change to only java in the future
FROM openkbs/jdk-mvn-py3

# Copies the python script to the container and executes the python script
COPY kla.py /kla.py
ENTRYPOINT ["python3", "/kla.py"]
