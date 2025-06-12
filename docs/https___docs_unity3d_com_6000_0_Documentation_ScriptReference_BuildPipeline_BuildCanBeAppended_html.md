* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildCanBeAppended.html

#  [BuildPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.html).BuildCanBeAppended
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
public static [CanAppendBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanAppendBuild.html) BuildCanBeAppended([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, string location); 
### Parameters
Parameter | Description  
---|---  
target | The [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) to build.  
location | The path where Unity builds the application.  
### Returns
**CanAppendBuild** Returns a UnityEditor.CanAppendBuild enum that indicates whether Unity can append the build. 
### Description
Checks if Unity can append the build.
* * *
