* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializationInfo.html

# SerializationInfo
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
Container for holding object serialization order information for a build.
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[serializationIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializationInfo-serializationIndex.html) | Order in which the object will be serialized to disk.  
[serializationObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializationInfo-serializationObject.html) | Source object to be serialzied to disk.  
### Constructors
Constructor | Description  
---|---  
[SerializationInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializationInfo-ctor.html) | Default constructor for an empty SerializationInfo.  
* * *
