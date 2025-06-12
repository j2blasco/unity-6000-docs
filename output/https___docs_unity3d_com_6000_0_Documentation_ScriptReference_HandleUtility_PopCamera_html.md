* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PopCamera.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).PopCamera
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
public static void PopCamera([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Description
Retrieve all camera settings.
A call to PopCamera will retrieve the most recently stored Camera settings added to a "stack" structure by [PushCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PushCamera.html). This allows for easy saving and restoration of temporary camera changes.
* * *
