* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType.html

# ManagedReferenceMissingType
struct in UnityEditor
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
Represents a managed reference object that has a missing type.
ManagedReferenceMissingType describes a managed reference object that could not be deserialized because it is missing its type.  
  
It includes the details of the type (expressed by its assembly, class and namespace) that is expected in order to reinstantiate the object.  
  
A type can be missing if the class was renamed, moved to another assembly, or moved inside a different namespace. A missing type may be a sign that an entire assembly or source script is missing from the project.  
  
If the original types are not available, this info can aid in migrating data to new types, or making a decision to clear the associated data.  
  
Additional resources: [SerializationUtility.HasManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.HasManagedReferencesWithMissingTypes.html), [SerializationUtility.GetManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.GetManagedReferencesWithMissingTypes.html), [SerializationUtility.ClearManagedReferenceWithMissingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.ClearManagedReferenceWithMissingType.html), [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)
### Properties
Property | Description  
---|---  
[assemblyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType-assemblyName.html) | Name of the Assembly where Unity expects to find the class. (Read Only)  
[className](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType-className.html) | Name of the class that is needed to instantiate the Managed Reference. (Read Only)  
[namespaceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType-namespaceName.html) | Namespace where Unity expects to find the class. Namespaces are optional so this might contain an empty string. (Read Only)  
[referenceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType-referenceId.html) | The Managed Reference ID. (Read Only)  
[serializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType-serializedData.html) | String summarizing the content of the serialized data of the missing object. (Read Only)  
* * *
