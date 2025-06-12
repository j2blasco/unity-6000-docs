* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.TryGetCameraToWorldMatrix.html

#  [PhotoCaptureFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.html).TryGetCameraToWorldMatrix
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public bool TryGetCameraToWorldMatrix(out [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) cameraToWorldMatrix); 
### Parameters
Parameter | Description  
---|---  
cameraToWorldMatrix | A matrix to be populated by the Camera to world Matrix.  
### Returns
**bool** True if a valid matrix is returned or false otherwise. This will be false if the frame has no location data. 
### Description
This method will return the camera to world matrix at the time the photo was captured if location data if available.
If location data is unavailable then the camera to world matrix will be set to the identity matrix.
* * *
