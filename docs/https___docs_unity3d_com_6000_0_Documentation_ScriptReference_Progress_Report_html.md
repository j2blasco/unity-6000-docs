* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Report
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
public static void Report(int id, float progress); 
## Declaration
public static void Report(int id, float progress, string description); 
## Declaration
public static void Report(int id, int currentStep, int totalSteps); 
## Declaration
public static void Report(int id, int currentStep, int totalSteps, string description); 
### Parameters
Parameter | Description  
---|---  
id | The progress indicator's unique ID.  
progress | A new progress value between 0 and 1.  
description | An updated description of the progress indicator. If the the progress status has not changed, or you do not set a description, this is null. To clear the current progress description, pass an empty string such as _""_.  
currentStep | An updated current step.  
totalSteps | An updated total number of steps, from start to finish.  
### Description
Reports a running progress indicator's current status.
When you report in steps, you can set the label for the steps with [Progress.SetStepLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetStepLabel.html). Note: Changes are applied on the next application tick unless you call this function from the main thread using a synchronous progress indicator (see [Synchronous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.Synchronous.html)).  
  
Additional resources: [Progress.Report](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html), [Progress.GetProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetProgress.html), [Progress.GetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.GetDescription.html), [Progress.SetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.SetDescription.html).
* * *
