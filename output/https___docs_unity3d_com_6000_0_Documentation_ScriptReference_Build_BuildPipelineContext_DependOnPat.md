* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.DependOnPath.html

#  [BuildPipelineContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.html).DependOnPath
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
public static void DependOnPath(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path of the dependency.  
### Description
Allows you to specify that a Scene depends on contents of a source asset at the provided path.
Scene rebuild will be triggered if either of the conditions are true: * The asset at the path changes * The asset at the path moves.
* * *
