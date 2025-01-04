import customtkinter as ctk
import tkinter as tk
import cv2
import numpy as np
import tensorflow as tf
import tf_keras
from PIL import Image, ImageTk
from threading import Thread
import time
from customtkinter import CTkImage
from PIL import Image as PILImage

class AutonomousVehicleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autonomous Vehicle Simulation Interface")
        self.root.geometry("1100x800")

        # Initialize UI Elements
        self.setup_ui()

        # Load TensorFlow Model
        self.model = self.load_model()

        # Video Capture
        self.cap = cv2.VideoCapture(0)
        self.running = True

        # Start Video Thread
        self.video_thread = Thread(target=self.update_video)
        self.video_thread.start()

    def setup_ui(self):
        """Set up the user interface."""
        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self.root, width=200, height=800, corner_radius=10)
        self.sidebar.pack(side="left", fill="y")

        # Sidebar Elements
        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="Controls", font=("Arial", 18), anchor="w")
        self.sidebar_label.grid(row=0, column=0, padx=10, pady=20, sticky="w")  # Left-aligned label

        self.start_button = ctk.CTkButton(self.sidebar, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Button at the bottom

        self.stop_button = ctk.CTkButton(self.sidebar, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.slider_label = ctk.CTkLabel(self.sidebar, text="Traffic Density", font=("Arial", 14), anchor="w")
        self.slider_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")  # Left-aligned text for slider

        self.traffic_slider = ctk.CTkSlider(self.sidebar, from_=0, to=10, command=self.update_traffic_density)
        self.traffic_slider.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.lane_switch_button = ctk.CTkButton(self.sidebar, text="Simulate Lane Switching",
                                                command=self.simulate_lane_switching)
        self.lane_switch_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.obstacle_button = ctk.CTkButton(self.sidebar, text="Simulate Obstacle", command=self.simulate_obstacle)
        self.obstacle_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Main Video Frame
        self.video_frame = ctk.CTkFrame(self.root, width=800, height=600, corner_radius=10)
        self.video_frame.pack(side="right", padx=20, pady=20)

        self.video_label = ctk.CTkLabel(self.video_frame, text="", width=800, height=600)
        self.video_label.pack()

        # Metrics Frame
        self.metrics_frame = ctk.CTkFrame(self.root, width=200, height=600, corner_radius=10)
        self.metrics_frame.pack(side="left", fill="y")

        self.metrics_label = ctk.CTkLabel(self.metrics_frame, text="Performance Metrics", font=("Arial", 18),
                                          anchor="w")
        self.metrics_label.grid(row=0, column=0, padx=10, pady=20, sticky="w")

        self.fps_label = ctk.CTkLabel(self.metrics_frame, text="FPS: --", font=("Arial", 14), anchor="w")
        self.fps_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.objects_label = ctk.CTkLabel(self.metrics_frame, text="Objects Detected: --", font=("Arial", 14),
                                          anchor="w")
        self.objects_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.lane_status_label = ctk.CTkLabel(self.metrics_frame, text="Lane Status: Clear", font=("Arial", 14),
                                              anchor="w")
        self.lane_status_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.obstacle_status_label = ctk.CTkLabel(self.metrics_frame, text="Obstacle: None", font=("Arial", 14),
                                                  anchor="w")
        self.obstacle_status_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def load_model(self):
        """Load the TensorFlow model."""
        try:
            model = tf_keras.models.load_model("model.h5")
            print("Model loaded successfully.")
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def update_video(self):
        """Update the video feed."""
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                # Preprocess frame for object detection
                processed_frame, detections = self.process_frame(frame)

                # Convert frame to a format compatible with CTkImage
                pil_image = PILImage.fromarray(processed_frame)  # Convert frame to a PIL Image
                img = CTkImage(pil_image, size=(800, 600))  # Create a CTkImage instance with the desired size

                # Update the image in the video label
                self.video_label.imgtk = img
                self.video_label.configure(image=img)

                # Update metrics
                self.update_metrics(detections)

            time.sleep(0.03)
    def process_frame(self, frame):
        """Process the frame and perform object detection."""
        # Resize frame for TensorFlow model
        input_frame = cv2.resize(frame, (224, 224)) / 255.0
        input_frame = np.expand_dims(input_frame, axis=0)

        # Predict with model
        if self.model:
            predictions = self.model.predict(input_frame)
            detections = np.argmax(predictions, axis=-1)
        else:
            detections = []

        # Draw bounding boxes (simulation)
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)
        cv2.putText(frame, "Detected Object", (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame, detections

    def update_metrics(self, detections):
        """Update performance metrics."""
        self.fps_label.configure(text=f"FPS: {int(self.cap.get(cv2.CAP_PROP_FPS))}")
        self.objects_label.configure(text=f"Objects Detected: {len(detections)}")

    def start_simulation(self):
        """Start the simulation."""
        self.running = True
        if not self.video_thread.is_alive():
            self.video_thread = Thread(target=self.update_video)
            self.video_thread.start()

    def stop_simulation(self):
        """Stop the simulation."""
        self.running = False
        self.cap.release()

    def update_traffic_density(self, value):
        """Update traffic density based on slider value."""
        print(f"Traffic Density: {value}")

    def simulate_lane_switching(self):
        """Simulate lane switching behavior."""
        self.lane_status_label.configure(text="Lane Status: Switching")
        time.sleep(1)
        self.lane_status_label.configure(text="Lane Status: Clear")

    def simulate_obstacle(self):
        """Simulate obstacle detection."""
        self.obstacle_status_label.configure(text="Obstacle: Detected")
        time.sleep(2)
        self.obstacle_status_label.configure(text="Obstacle: None")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Options: "light", "dark"
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = AutonomousVehicleApp(root)
    root.mainloop()
