* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).HasUserAuthorization
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
public static bool HasUserAuthorization([UserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html) mode); 
### Description
Check if the user has authorized use of the webcam or microphone on iOS and WebGL.
This is used to check the result of a previous call to [Application.RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html). Explicit user consent to use features is only needed in WebGL. In other build targets, this function always returns true.
* * *
