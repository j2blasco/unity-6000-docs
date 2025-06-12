* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IUnityLinkerProcessor.html

# IUnityLinkerProcessor
interface in UnityEditor.Build
Leave feedback
  

Implements interfaces:[IOrderedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IOrderedCallback.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Implement this interface to receive callbacks related to the running of UnityLinker.
Additional resources: [BuildPlayerProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.html), [IFilterBuildAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IFilterBuildAssemblies.html), [IPostBuildPlayerScriptDLLs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPostBuildPlayerScriptDLLs.html), [IPreprocessBuildWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessBuildWithReport.html)
### Public Methods
Method | Description  
---|---  
[GenerateAdditionalLinkXmlFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IUnityLinkerProcessor.GenerateAdditionalLinkXmlFile.html) | Generates additional link.xml files for preserving additional types and their members.  
* * *
