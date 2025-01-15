const startCameraButton = document.getElementById("startCameraButton");
    const capturePhotoButton = document.getElementById("capturePhotoButton");
    const uploadButton = document.getElementById("uploadButton");
    const photoContainer = document.getElementById("photoContainer");
    const photoInput = document.getElementById("photoInput");
    const cameraStream = document.getElementById("cameraStream");
    const photoCanvas = document.getElementById("photoCanvas");

    let cameraStreamObject;

    // Start the camera
    startCameraButton.addEventListener("click", async () => {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            alert("Camera not supported on this device.");
            return;
        }

        cameraStreamObject = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraStream.srcObject = cameraStreamObject;
        capturePhotoButton.disabled = false;
    });

    // Capture photo
    capturePhotoButton.addEventListener("click", () => {
        const context = photoCanvas.getContext("2d");
        photoCanvas.width = cameraStream.videoWidth;
        photoCanvas.height = cameraStream.videoHeight;
        context.drawImage(cameraStream, 0, 0, photoCanvas.width, photoCanvas.height);

        const photoDataUrl = photoCanvas.toDataURL("image/png");

        // Add photo to the page
        const img = document.createElement("img");
        img.src = photoDataUrl;
        photoContainer.appendChild(img);

        // Convert Data URL to Blob and append to the file input
        const photoBlob = dataURLToBlob(photoDataUrl);
        const file = new File([photoBlob], `photo-${Date.now()}.png`, { type: "image/png" });
        const dataTransfer = new DataTransfer();
        Array.from(photoInput.files).forEach((file) => dataTransfer.items.add(file));
        dataTransfer.items.add(file);
        photoInput.files = dataTransfer.files;

        uploadButton.disabled = false;
    });

    // Helper function to convert Data URL to Blob
    function dataURLToBlob(dataURL) {
        const parts = dataURL.split(",");
        const mime = parts[0].match(/:(.*?);/)[1];
        const b64 = atob(parts[1]);
        let len = b64.length;
        const u8arr = new Uint8Array(len);
        while (len--) {
            u8arr[len] = b64.charCodeAt(len);
        }
        return new Blob([u8arr], { type: mime });
    }