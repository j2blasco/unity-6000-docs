* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.html

# PhotoCaptureFrame
class in UnityEngine.Windows.WebCam
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Contains information captured from the web camera.
Information captured can include the image has well as spatial data.
### Properties
Property | Description  
---|---  
[dataLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame-dataLength.html) | The length of the raw IMFMediaBuffer which contains the image captured.  
[hasLocationData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame-hasLocationData.html) | Specifies whether or not spatial data was captured.  
[pixelFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame-pixelFormat.html) | The raw image data pixel format.  
### Public Methods
Method | Description  
---|---  
[CopyRawImageDataIntoBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.CopyRawImageDataIntoBuffer.html) | Will copy the raw IMFMediaBuffer image data into a byte list.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.Dispose.html) | Disposes the PhotoCaptureFrame and any resources it uses.  
[GetUnsafePointerToBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.GetUnsafePointerToBuffer.html) | Provides a COM pointer to the native IMFMediaBuffer that contains the image data.  
[TryGetCameraToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.TryGetCameraToWorldMatrix.html) | This method will return the camera to world matrix at the time the photo was captured if location data if available.  
[TryGetProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.TryGetProjectionMatrix.html) | This method will return the projection matrix at the time the photo was captured if location data if available.  
[UploadImageDataToTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.UploadImageDataToTexture.html) | This method will copy the captured image data into a user supplied texture for use in Unity.  
* * *
