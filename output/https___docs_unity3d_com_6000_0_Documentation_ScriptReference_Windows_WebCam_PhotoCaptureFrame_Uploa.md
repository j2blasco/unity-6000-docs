* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.UploadImageDataToTexture.html

#  [PhotoCaptureFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.html).UploadImageDataToTexture
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
public void UploadImageDataToTexture([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) targetTexture); 
### Parameters
Parameter | Description  
---|---  
targetTexture | The target texture that the captured image data will be copied to.  
### Description
This method will copy the captured image data into a user supplied texture for use in Unity.
You may only use this method if you specified the **BGRA32** format in your [CameraParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html). Keep in mind that this operation will happen on the main thread and therefore be slow. The captured image will also appear flipped on the HoloLens. You can reorient the image by using a custom shader.
* * *
