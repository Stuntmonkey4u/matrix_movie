# The Matrix Resurrections: Web Experience

Welcome, Operator. You've accessed a unique system diagnostic: a web-based "movie" that reimagines *The Matrix Resurrections* from the perspective of the Matrix system itself. Witness the unfolding events as a series of logs, process traces, AI debug messages, and cryptic system commentary, all within your browser.

This project is a nerdy, immersive experience for tech enthusiasts and Matrix fans, designed to simulate a system administrator watching the digital world react to Neo and Trinity's return.

## Features

*   **Interactive Web Interface**: Experience the movie in a terminal-like interface in your web browser.
*   **Self-Paced Navigation**: Use the left and right arrow keys to move forward and backward through the scenes at your own pace.
*   **Animated Scenes**: Each scene remains animated, with typing effects and simulated system processes.
*   **Matrix Code Rain**: Iconic green code rain animations run in the background.
*   **System Log Aesthetic**: Output styled to mimic `dmesg`, `journalctl`, `strace`, `tcpdump`, and other familiar Linux tools, but with a Matrix twist.
*   **Dockerized Environment**: The entire application runs in a Docker container for easy setup and consistent performance.

## Prerequisites

*   **Docker**: You must have Docker installed and running on your system. You can download it from the official [Docker website](https://www.docker.com/products/docker-desktop/).

## Installation & Running the Experience

1.  **Clone the Repository**:
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd name_of_cloned_repository
    ```

2.  **Build the Docker Image**:
    In the root directory of the project, run the following command to build the Docker image. This will download the necessary dependencies and package the application.
    ```bash
    docker build -t matrix-web .
    ```

3.  **Run the Docker Container**:
    Once the build is complete, start the web server by running the following command. This will make the application available on port 5000 of your local machine.
    ```bash
    docker run -p 5000:5000 matrix-web
    ```

4.  **Open in Your Browser**:
    Open your favorite web browser and navigate to:
    [http://localhost:5000](http://localhost:5000)

5.  **Enjoy the Show!**
    Use the left and right arrow keys to navigate through the scenes.

## Project Structure

*   `main.py`: The Flask web server that serves the application.
*   `Dockerfile`: Defines the Docker container for the application.
*   `scenes.json`: Contains all the text and animation data for each scene.
*   `templates/`: Contains the `index.html` file for the main web page.
*   `static/`: Contains the `style.css` and `script.js` files for the frontend.
*   `scenes/`: The original Python scene files (kept for reference).
*   `utils/`: The original Python utility files (kept for reference).

---

"We can't see it, but we're all trapped inside a routine. A loop." - Bugs, *The Matrix Resurrections*