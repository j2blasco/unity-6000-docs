* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Remove
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
public static int Remove(int id); 
## Declaration
public static int Remove(int id, bool forceSynchronous); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
forceSynchronous | When you set this parameter to true it forces this method to remove the progress indicator synchronously.  
### Returns
**int** -1 if the progress indicator is removed. Otherwise, returns the progress indicator's ID. 
### Description
Finishes and removes an active progress indicator.
The progress indicator is removed on the next application tick unless it is synchronous (see [Synchronous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Synchronous.html)). To force this method to remove the progress indicator synchronously, set the "forceSynchronous" parameter to true.
* * *
