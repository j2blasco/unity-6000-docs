* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).OnVideoCaptureResourceCreatedCallback
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
public delegate void OnVideoCaptureResourceCreatedCallback([Windows.WebCam.VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) captureObject); 
### Parameters
Parameter | Description  
---|---  
captureObject | The VideoCapture instance.  
### Description
Called when a VideoCapture resource has been created.
If the instance failed to be created, the instance returned will be null.
* * *
