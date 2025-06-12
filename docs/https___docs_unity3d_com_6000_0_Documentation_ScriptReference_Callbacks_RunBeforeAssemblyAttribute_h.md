* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute.html

# RunBeforeAssemblyAttribute
class in UnityEditor.Callbacks
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
Add this attribute to a callback method to indicate that this callback must be run before any callbacks that are part of the specified assembly.
To define dependencies for a callback, use the following attributes: 
  * [RunAfterClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterClassAttribute.html), [RunBeforeClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeClassAttribute.html)
  * [RunAfterAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterAssemblyAttribute.html), [RunBeforeAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute.html)
  * [RunAfterPackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterPackageAttribute.html), [RunBeforePackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforePackageAttribute.html)


When the callback is invoked, Unity generates a dependency graph and uses topological sorting to ensure that all dependencies are run in sequence based on their dependencies. If callbacks dependencies are not present in the project then the instruction will be ignored during the generation of the dependency graph.  
  
**Note:** Defining callback dependencies is currently only supported by the [AssetPostprocessor.OnPostprocessAllAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html) callback.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Callbacks;
using UnityEngine;  
  
// This example shows how to ensure that a callback is called before the Addressables assembly has been called.
class MyPostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    [RunBeforeAssembly("Unity.Addressables.Editor")]
    static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyAllPostprocessor");
    }
}

```

### Properties
Property | Description  
---|---  
[assemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute-assemblyName.html) | The name of the assembly that should be called after this callback.  
### Constructors
Constructor | Description  
---|---  
[RunBeforeAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute-ctor.html) | Add this attribute to a callback method to indicate that this callback must be run before any callbacks that are part of the specified assembly.  
* * *
