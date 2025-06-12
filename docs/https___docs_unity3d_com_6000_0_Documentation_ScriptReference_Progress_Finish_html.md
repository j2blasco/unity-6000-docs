* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Finish.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Finish
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
public static void Finish(int id, [Progress.Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Status.html) status); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
status | The status of the associated task when the progress indicator finishes. Indicates whether the task succeeded, failed, or was canceled.  
### Description
Marks the progress indicator as finished.
The system removes finished progress indicators unless they are sticky. Sticky progress indicators display progress information even after their associated tasks are complete. The system does not remove them automatically.
* * *
