from docx import Document

output = r"C:\Users\JOSEPH DEEB\Desktop\lab8\Lab8-Joe-Dib-Submission.docx"
document = Document()

document.add_heading("Software Tools Lab 8 – Docker and Containers", 0)
document.add_paragraph("Student: Joe Dib")
document.add_paragraph("AUB Username: jjd17")
document.add_heading("GitHub Repository", 1)
document.add_paragraph("https://github.com/Djoe2490/Lab8-Joe-Dib")

document.add_heading("Activity 1: Docker Commands", 1)
document.add_heading("docker ps -a", 2)
document.add_paragraph("Lists all containers, including running and stopped containers. It shows the container ID, image, command, creation time, status, ports, and container name.")

document.add_heading("docker stop <image_name>", 2)
document.add_paragraph("Stops a running container. The command is normally given a container name or container ID. Docker sends a stop signal to the container process.")

document.add_heading("docker logs <image_name>", 2)
document.add_paragraph("Displays log output from a container. This is useful for checking startup errors, HTTP requests, and application output.")

document.add_heading("Activity 2: Container Images", 1)
document.add_paragraph("Image 1: jjd17/lab8-joe-dib:0.0.1-RELEASE")
document.add_paragraph("Runs the Lab 5 Flask/Postman API project on port 5000. GET /api/users returned the Maya Haddad record from database.db.")
document.add_paragraph("Image 2: jjd17/lab8-joe-dib:0.0.2-RELEASE")
document.add_paragraph("Runs the user-names API on port 3000. GET /api/users/names returned [\"Maya Haddad\"] from database.db.")

document.add_heading("Test Results", 1)
document.add_paragraph("Port 5000 container: running and reachable at http://localhost:5000/api/users")
document.add_paragraph("Port 3000 container: running and reachable at http://localhost:3000/api/users/names")
document.add_paragraph("The Docker Desktop snapshot is saved as docker_desktop.png in the submission folder.")

document.save(output)
print(output)
