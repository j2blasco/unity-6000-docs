* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetParentId.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).GetParentId
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
public static int GetParentId(int id); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
### Returns
**int** The unique ID of the progress indicator's parent. If the progress indicator is not a child of any other progress indicators, returns -1. 
### Description
Gets the unique ID of the progress indicator's parent, if any.
* * *
