* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html

# PropertyPath
struct in Unity.Properties
/
Implemented in:[UnityEngine.PropertiesModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PropertiesModule.html)
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
A [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) is used to store a reference to a single property within a tree. 
The path is stored as an array of parts and can be easily queried for algorithms. 
### Properties
Property | Description  
---|---  
[IsEmpty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.IsEmpty.html) |  Gets if there is any part contained in the PropertyPath.   
[Length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.Length.html) |  Gets the number of parts contained in the PropertyPath.   
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.Index_operator.html) |  Gets the PropertyPathPart at the given index.   
### Constructors
Constructor | Description  
---|---  
[PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath-ctor.html) |  Initializes a new instance of the PropertyPath based on the given property string.   
### Public Methods
Method | Description  
---|---  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.Equals.html) |  Indicates whether this instance and a specified object are equal.   
### Static Methods
Method | Description  
---|---  
[AppendIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendIndex.html) |  Returns a new PropertyPath combining the given PropertyPath and an index-type PropertyPathPart.   
[AppendKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendKey.html) |  Returns a new PropertyPath combining the given PropertyPath and an key-type PropertyPathPart.   
[AppendName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendName.html) |  Returns a new PropertyPath combining the given PropertyPath and an name-type PropertyPathPart.   
[AppendPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendPart.html) |  Returns a new PropertyPath combining the given PropertyPath and PropertyPathPart.   
[AppendProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendProperty.html) |  Returns a new PropertyPath combining the given PropertyPath and a PropertyPathPart whose type will be based on the property interfaces.   
[Combine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.Combine.html) |  Returns a new PropertyPath combining the parts of the two given PropertyPath.   
[FromIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.FromIndex.html) |  Returns a new PropertyPath from the provided index.   
[FromKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.FromKey.html) |  Returns a new PropertyPath from the provided key.   
[FromName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.FromName.html) |  Returns a new PropertyPath from the provided name.   
[FromPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.FromPart.html) |  Returns a new PropertyPath from the provided PropertyPathPart.   
[Pop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.Pop.html) |  Returns a new PropertyPath that will not include the last PropertyPathPart.   
[SubPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.SubPath.html) |  Returns a new PropertyPath containing the PropertyPathPart starting at the given start index.   
* * *
