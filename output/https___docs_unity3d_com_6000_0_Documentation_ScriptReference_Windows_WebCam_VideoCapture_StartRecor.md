* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StartRecordingAsync.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).StartRecordingAsync
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
public void StartRecordingAsync(string filename, [Windows.WebCam.VideoCapture.OnStartedRecordingVideoCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnStartedRecordingVideoCallback.html) onStartedRecordingVideoCallback); 
### Parameters
Parameter | Description  
---|---  
filename | The name of the video to be recorded to.  
onStartedRecordingVideoCallback | Invoked as soon as the video recording begins.  
### Description
Asynchronously records a video from the web camera to the file system.
* * *
