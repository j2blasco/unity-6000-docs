* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.RegisterBuildPlayerHandler.html

#  [BuildPlayerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.html).RegisterBuildPlayerHandler
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
public static void RegisterBuildPlayerHandler(Action<BuildPlayerOptions> func); 
### Parameters
Parameter | Description  
---|---  
func | Delegate System.Action that takes a BuildPipeline.BuildPlayerOptions parameter.  
### Description
Register a delegate to intercept or override the build process executed with the "Build" and "Build and Run" buttons. Registering a null value will restore default behavior, which is the equivalent of calling [BuildPlayerWindow.DefaultBuildMethods.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.DefaultBuildMethods.BuildPlayer.html).
* * *
