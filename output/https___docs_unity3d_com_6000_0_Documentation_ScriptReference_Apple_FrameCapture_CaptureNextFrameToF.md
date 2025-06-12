* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCapture.CaptureNextFrameToFile.html

#  [FrameCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCapture.html).CaptureNextFrameToFile
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
public static void CaptureNextFrameToFile(string path); 
### Description
Begin capture to the specified file at the beginning of the next frame, and end it at the end of the next frame.
This is the same as calling [FrameCapture.BeginCaptureToFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCapture.BeginCaptureToFile.html) and [FrameCapture.EndCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCapture.EndCapture.html), but with implicit boundaries at the start and end of the frame.
* * *
