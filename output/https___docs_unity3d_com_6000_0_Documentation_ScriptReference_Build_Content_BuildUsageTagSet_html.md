* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.html

# BuildUsageTagSet
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
Container for holding information about how objects are being used in a build.
This class helps ensure the correct Shared Variants, Mesh Channels, and more are included in the build correctly.  
  
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Constructors
Constructor | Description  
---|---  
[BuildUsageTagSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet-ctor.html) | Default constructor for an empty BuildUsageTagSet.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.Dispose.html) | Dispose the BuildUsageTagSet destroying all internal state.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.Equals.html) | Returns true if the objects are equal.  
[FilterToSubset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.FilterToSubset.html) | Filters this BuildUsageTagSet instance to remove references to any objects that are not in the array of ObjectIdentifiers specified by objectIds.  
[GetHash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.GetHash128.html) | Gets the hash for the BuildReferenceMap.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.GetHashCode.html) | Gets the hash code for the BuildUsageTagSet.  
[GetObjectData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.GetObjectData.html) | ISerializable method for serialization support outside of Unity's internal serialization system.  
[GetObjectIdentifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.GetObjectIdentifiers.html) | Returns an array of ObjectIdentifiers that this BuildUsageTagSet contains usage information about.  
[UnionWith](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.UnionWith.html) | Adds the Object usage information from another BuildUsageTagSet to this BuildUsageTagSet.  
* * *
