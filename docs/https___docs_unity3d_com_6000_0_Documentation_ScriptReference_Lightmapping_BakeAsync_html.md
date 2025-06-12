* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeAsync.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).BakeAsync
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
public static bool BakeAsync(); 
### Returns
**bool** Returns true if the bake was successfully started. Will return false and print a warning message if it's not possible to start the bake. 
### Description
Starts an asynchronous bake job.
The progress can be monitored via [isRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-isRunning.html) property. [bakeStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeStarted.html) will be called when the bake starts, and [bakeCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeCompleted.html) when it is done.  
Only works in [Lightmapping.GIWorkflowMode.OnDemand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GIWorkflowMode.OnDemand.html) mode.   
  
For synchronous bakes see [Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html).
* * *
