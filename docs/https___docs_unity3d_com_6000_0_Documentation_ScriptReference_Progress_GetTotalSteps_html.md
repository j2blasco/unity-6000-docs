* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetTotalSteps.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).GetTotalSteps
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
public static int GetTotalSteps(int id); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
### Returns
**int** The number of steps. 
### Description
Gets the total number of steps, from start to finish, for a progress indicator.
Returns -1 if you don't use steps to report progress on this indicator. To set the type of steps that the progress window displays, use [Progress.SetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetStepLabel.html).  
  
Additional resources: [Progress.Report](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html), [Progress.GetCurrentStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetCurrentStep.html), [Progress.GetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetStepLabel.html), [Progress.SetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetStepLabel.html).
* * *
