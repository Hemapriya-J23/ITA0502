import cv2
import numpy as np

# Input video
input_video = "image38.mp4"

# Open the video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open video!")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video
output_video = "perspective_transformed_image38.mp4"

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

# Source points
# Change these points according to the area you want to transform
src_points = np.float32([
    [100, 100],              # Top-left
    [width - 100, 100],      # Top-right
    [width - 100, height - 100],  # Bottom-right
    [100, height - 100]      # Bottom-left
])

# Destination points
dst_points = np.float32([
    [0, 0],
    [width, 0],
    [width, height],
    [0, height]
])

# Calculate transformation matrix
matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

while True:

    # Read one frame
    ret, frame = cap.read()

    if not ret:
        break

    # Apply perspective transformation
    transformed_frame = cv2.warpPerspective(
        frame,
        matrix,
        (width, height)
    )

    # Display the transformed video
    cv2.imshow(
        "Perspective Transformed Video",
        transformed_frame
    )

    # Save transformed frame
    out.write(transformed_frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print("Perspective transformation completed!")
print("Output saved as:", output_video)
