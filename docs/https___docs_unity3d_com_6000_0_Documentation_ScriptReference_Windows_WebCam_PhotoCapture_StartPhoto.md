* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.StartPhotoModeAsync.html

#  [PhotoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.html).StartPhotoModeAsync
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
public void StartPhotoModeAsync([Windows.WebCam.CameraParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html) setupParams, [Windows.WebCam.PhotoCapture.OnPhotoModeStartedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.OnPhotoModeStartedCallback.html) onPhotoModeStartedCallback); 
### Parameters
Parameter | Description  
---|---  
setupParams | The various settings that should be applied to the web camera.  
onPhotoModeStartedCallback | This callback will be invoked once photo mode has been activated.  
### Description
Asynchronously starts photo mode.
Activates the web camera with the various settings specified in [CameraParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html). Only one PhotoCapture instance can start the photo mode at any given time. After starting the photo mode, you make take photos via [PhotoCapture.TakePhotoAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.TakePhotoAsync.html). While in photo mode, more power will be consumed so make sure that you call [PhotoCapture.StopPhotoModeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.StopPhotoModeAsync.html) when you are done taking photos.
* * *
