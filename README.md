# Autonomous Vehicle Simulation Interface

Autonomous vehicle simulation interface built using Python, TensorFlow, OpenCV, and CustomTkinter. The application simulates an autonomous vehicle environment, where users can interact with various controls to start/stop the simulation, simulate lane switching, detect obstacles, and adjust traffic density.

## Features

- **Real-Time Video Feed**: Displays live video from a webcam, simulating the camera feed of an autonomous vehicle.
- **Object Detection**: Uses a pre-trained TensorFlow model to detect objects in the video feed.
- **Performance Metrics**: Displays key performance metrics like Frames Per Second (FPS), objects detected, lane status, and obstacle status.
- **Interactive Controls**: Provides controls to:
  - Start and stop the simulation.
  - Simulate lane switching.
  - Simulate obstacle detection.
  - Adjust traffic density using a slider.

## Requirements

- Python 3.x
- TensorFlow
- OpenCV
- CustomTkinter
- NumPy
- Pillow

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kayung-developer/Autonomous-Vehicle-Simulation-Interface.git
```

2. Navigate to the project directory:
```bash
cd autonomous-vehicle-simulation
```
3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


4. Install the required dependencies:

```bash
pip install -r requirements.txt
```
5. Ensure you have a pre-trained TensorFlow model saved as `model.h5` in the project directory.


### Usage
1. Run the application:
```bash
python app.py
```

2. The application window will appear with a live video feed, performance metrics, and control buttons on the sidebar.

3. Interact with the controls to:

- Start/stop the simulation.
- Simulate lane switching and obstacle detection.
- Adjust the traffic density using the slider.

### Structure
- `app.py`: Main Python script that runs the application.
- `model.h5`: Pre-trained TensorFlow model used for object detection (make sure to have this file in the project directory).
- `requirements.txt`: Lists the dependencies needed to run the project.

### TensorFlow Model
The `model.h5` file is a pre-trained TensorFlow model that performs object detection. The model should be trained to recognize the objects relevant to autonomous vehicles, such as pedestrians, other vehicles, traffic signs, etc.

### Model Training (Optional)
To train your own model, you can use a dataset of images with labeled objects. Then, follow TensorFlow's tutorial for training object detection models, and save the model as `model.h5`.


### Screenshots
![Screenshots]()
### Credits
- CustomTkinter: For the beautiful and functional user interface.
- TensorFlow: For the object detection capabilities.
- OpenCV: For real-time video capture and image processing.
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Special thanks to the open-source community for providing the tools and libraries that made this project possible.
Thanks to TensorFlow and OpenCV for their extensive documentation and support.


### Future Improvements
- Integrate more complex object detection models for real-world applications.
- Add vehicle control simulation (steering, acceleration, etc.) for a more immersive experience.
- Implement additional safety and decision-making algorithms to simulate autonomous driving more realistically.

<i>Created by Oryiman Pascal Aondover</i>

```markdown

### Explanation of the Sections

1. **Project Overview**: A brief explanation of the app's purpose and functionality.
2. **Features**: Lists the key features of the application.
3. **Requirements**: Python version and libraries needed to run the application.
4. **Installation**: Detailed steps for cloning, setting up the environment, and installing dependencies.
5. **Usage**: Instructions on how to run the application and interact with the user interface.
6. **Structure**: Details the important files and directories in the project.
7. **TensorFlow Model**: Explains how the pre-trained model is used for object detection and how you can train your own model if needed.
8. **Credits**: Acknowledges the libraries and tools used in the project.
9. **License**: Provides licensing information (adjust it according to your chosen license).
10. **Acknowledgments**: Recognizes contributions from the community and any sources you relied on.
11. **Future Improvements**: Mentions possible directions for future updates or enhancements to the project.

This `README.md` provides a complete overview of the project, and it can be easily customized or expanded to suit your needs.
```