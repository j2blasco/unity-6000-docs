* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageCache.html

# BuildUsageCache
class in UnityEditor.Build.Content
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
Caching object for the Scriptable Build Pipeline.
This class helps improve performance when calling the [ContentBuildInterface.CalculateBuildUsageTags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculateBuildUsageTags.html) api multiple times.  
  
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Constructors
Constructor | Description  
---|---  
[BuildUsageCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageCache-ctor.html) | Default contructor.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageCache.Dispose.html) | Dispose the BuildUsageCache destroying all internal state.  
* * *
