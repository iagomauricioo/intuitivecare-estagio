# docker_manager.py
import subprocess
import time

class DockerManager:
    def start_postgres_with_docker(self):
        try:
            subprocess.run("docker-compose up -d", shell=True, check=True)
            print("Waiting for PostgreSQL to start...")
            time.sleep(10)
        except subprocess.CalledProcessError as e:
            print(f"Error starting PostgreSQL: {e}")
            return False
        return True
