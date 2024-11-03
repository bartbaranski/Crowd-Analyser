<h1>Crowd Analysis Application</h1>

<p>A Python-based application designed to analyze the size and density of crowds at public gatherings using real-time video processing and AI algorithms. This application leverages YOLO (You Only Look Once) for object detection to count individuals in video frames, providing insights into the total participants and crowd density over time.</p>

<h2>Features</h2>
<ul>
    <li><strong>Real-Time Video Processing:</strong> Analyzes video frames to detect and count people in crowds.</li>
    <li><strong>User Interface:</strong> Simple GUI built with Tkinter for selecting videos and viewing analysis results.</li>
    <li><strong>Data Visualization:</strong> Real-time graph showing the cumulative count of people detected in video frames.</li>
    <li><strong>Frame Counter:</strong> Displays the current and total frames for easy tracking of the analysis process.</li>
    <li><strong>Database Storage:</strong> Stores video and analysis metadata in PostgreSQL for easy retrieval and reporting.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Programming Language:</strong> Python</li>
    <li><strong>Machine Learning Framework:</strong> PyTorch (YOLOv5 model for object detection)</li>
    <li><strong>GUI Framework:</strong> Tkinter</li>
    <li><strong>Data Processing and Visualization:</strong> OpenCV, Matplotlib</li>
    <li><strong>Database:</strong> PostgreSQL</li>
</ul>
<h2>Future Improvements</h2>
<ul>
    <li><strong>Advanced Object Tracking:</strong> Implement SORT or DeepSORT for improved accuracy in crowded scenes.</li>
    <li><strong>Additional Analysis Metrics:</strong> Include more in-depth statistics, such as participant age and movement tracking.</li>
    <li><strong>Export Reports:</strong> Enable export of detailed reports in PDF or CSV format for further analysis.</li>
</ul>
