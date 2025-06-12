* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetRemainingTime.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).GetRemainingTime
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
public static long GetRemainingTime(int id); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
### Returns
**long** The number of seconds remaining. 
### Description
Gets a progress indicator's remaining time, in seconds.
If the remaining time is not set manually, Unity computes it automatically. Unity computes a progress indicator's remaining time based on the average of the last five updates of its current running time, and progress. This helps prevent large fluctuations in the displayed value, and results in smoother progress reporting.
* * *
