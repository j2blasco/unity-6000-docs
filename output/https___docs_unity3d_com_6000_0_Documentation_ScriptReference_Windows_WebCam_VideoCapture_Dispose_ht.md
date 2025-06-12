* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.Dispose.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).Dispose
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
public void Dispose(); 
### Description
You must call Dispose to shutdown the VideoCapture instance and release the native WinRT objects.
If your VideoCapture instance successfully called [VideoCapture.StartVideoModeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StartVideoModeAsync.html), you must make sure that you call [VideoCapture.StopVideoModeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StopVideoModeAsync.html) before disposing your VideoCapture instance. If a recording is in progress when Dispose is called, the output file will be corrupted and unusable.  
  
**Note:** Exiting PlayMode in the Editor will automatically Dispose all VideoCapture instances regardless of their current state.
* * *
