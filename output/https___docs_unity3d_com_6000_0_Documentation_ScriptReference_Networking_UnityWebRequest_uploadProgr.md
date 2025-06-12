* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uploadProgress.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).uploadProgress
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
uploadProgress; 
### Description
Returns a floating-point value between 0.0 and 1.0, indicating the progress of uploading body data to the server.
If the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) is complete (either a success or a system error), this property will always return 1. If the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) is still communicating with the remote server, and [uploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uploadHandler.html) is `null`, this property will return zero. If [Send](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Send.html) has not yet been called, this property will return -1.
* * *
