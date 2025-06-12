* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.StopProfileCapture.html

#  [ContentBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html).StopProfileCapture
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
public static ContentBuildProfileEvent[] StopProfileCapture(); 
### Description
Returns an array of ContentBuildProfileEvent structs that contain information for each occuring event. Also stops the profile capture.
Throws an InvalidOperationException if no profile capture has started.
* * *
