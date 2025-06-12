* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.html

# ObjectIdentifier
struct in UnityEditor.Build.Content
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
Struct that identifies a specific object project wide.
Note: this struct and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[filePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-filePath.html) | The file path on disk that contains this object. (Only used for objects not known by the AssetDatabase).  
[fileType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-fileType.html) | Type of file that contains this object.  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-guid.html) | The specific asset that contains this object.  
[localIdentifierInFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-localIdentifierInFile.html) | The index of the object inside a serialized file.  
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.CompareTo.html) | Implements the IComparable interface.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.Equals.html) | Returns true if the objects are equal.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.GetHashCode.html) | Gets the hash code for the ObjectIdentifier.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.ToString.html) | Returns a nicely formatted string for this ObjectIdentifier.  
### Static Methods
Method | Description  
---|---  
[ToInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.ToInstanceID.html) | Tries to return the InstanceID that represents this ObjectIdentifier.  
[ToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.ToObject.html) | Tries to find, load, and return the Object that represents this ObjectIdentifier.  
[TryGetObjectIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.TryGetObjectIdentifier.html) | Tries to convert a persistent Object into an ObjectIdentifier.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-operator_ne.html) | Returns true if the ObjectIdentifiers are different.  
[operator <](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-operator_lt.html) | Returns true if the first ObjectIdentifier is less than the second ObjectIdentifier.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-operator_eq.html) | Returns true if the ObjectIdentifiers are the same.  
[operator >](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier-operator_gt.html) | Returns true if the first ObjectIdentifier is greater than the second ObjectIdentifier.  
* * *
