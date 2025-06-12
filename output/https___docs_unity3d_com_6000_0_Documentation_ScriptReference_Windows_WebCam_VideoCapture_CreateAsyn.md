* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.CreateAsync.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).CreateAsync
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
public static void CreateAsync([Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback.html) onCreatedCallback); 
## Declaration
public static void CreateAsync(bool showHolograms, [Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback.html) onCreatedCallback); 
### Parameters
Parameter | Description  
---|---  
showHolograms | Allows capturing holograms in your video.  
onCreatedCallback | This callback will be invoked when the VideoCapture instance is created and ready to be used.  
### Description
Asynchronously creates an instance of a VideoCapture object that can be used to record videos from the web camera to disk.
If the instance failed to be created, the instance returned will be null.
* * *
