* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetRemainingTime.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).SetRemainingTime
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
public static void SetRemainingTime(int id, long seconds); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
seconds | The progress indicator's remaining time, in seconds.  
### Description
Sets the progress indicator's remaining time, in seconds.
Call this function to set the progress indicator's remaining time. When this function is called, the system stops automatically computing the estimated remaining time. To use automatic computation again, you need to call the function [Progress.ClearRemainingTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.ClearRemainingTime.html).
* * *
