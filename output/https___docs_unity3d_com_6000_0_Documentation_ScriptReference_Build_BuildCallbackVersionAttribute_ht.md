* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildCallbackVersionAttribute.html

# BuildCallbackVersionAttribute
class in UnityEditor.Build
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
### Description
Attribute to provide a version number for IProcessSceneWithReport callbacks.
This attribute is used to inform the build system when the callback implementation changes and the build result needs to be regenerated. Therefore, developers should bump the version number when changing the implementation of the callback. If the attribute is not specified, the implied version number is 1.  
  
Additional resources: [IProcessSceneWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.html), [EditorBuildSettings.UseParallelAssetBundleBuilding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.UseParallelAssetBundleBuilding.html)
### Properties
Property | Description  
---|---  
[Version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildCallbackVersionAttribute.Version.html) | Version number.  
### Constructors
Constructor | Description  
---|---  
[BuildCallbackVersionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildCallbackVersionAttribute-ctor.html) | Constructor taking the version number for the callback.  
* * *
