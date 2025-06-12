* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.DependOnAsset.html

#  [BuildPipelineContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.html).DependOnAsset
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
public static void DependOnAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) asset); 
### Parameters
Parameter | Description  
---|---  
asset | The Unity Object from an asset.  
### Description
Allows you to specify that a Scene depends on contents of an asset directly provided.
Scene rebuild will be triggered if the condition is true: * if the asset or any of its dependencies changes.
* * *
