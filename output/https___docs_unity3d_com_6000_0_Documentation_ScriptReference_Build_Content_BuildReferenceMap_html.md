* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.html

# BuildReferenceMap
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
Container for holding information about where objects will be serialized in a build.
This class helps ensure that Object references can be correctly resolved in the final built data.  
  
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Constructors
Constructor | Description  
---|---  
[BuildReferenceMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap-ctor.html) | Default constructor for an empty BuildReferenceMap.  
### Public Methods
Method | Description  
---|---  
[AddMapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.AddMapping.html) | Adds a mapping for a single Object to where it will be serialized out to the build.  
[AddMappings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.AddMappings.html) | Adds mappings for a set of Objects to where they will be serialized out to the build.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.Dispose.html) | Dispose the BuildReferenceMap destroying all internal state.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.Equals.html) | Returns true if the objects are equal.  
[FilterToSubset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.FilterToSubset.html) | Filters this BuildReferenceMap instance to remove references to any objects that are not in the array of ObjectIdentifiers specified by objectIds.  
[GetHash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.GetHash128.html) | Gets the hash for the BuildReferenceMap.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.GetHashCode.html) | Gets the hash code for the BuildReferenceMap.  
[GetObjectData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.GetObjectData.html) | ISerializable method for serialization support outside of Unity's internal serialization system.  
* * *
