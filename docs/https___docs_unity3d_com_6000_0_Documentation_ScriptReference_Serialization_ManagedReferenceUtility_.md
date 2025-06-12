* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html

#  [ManagedReferenceUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.html).GetManagedReferenceIdForObject
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
## Declaration
public static long GetManagedReferenceIdForObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, object scriptObj); 
### Parameters
Parameter | Description  
---|---  
hostObj | The host object that supports [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html). For example, [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) or [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html).  
refObj | The C# object, to which the reference Id is associated.  
### Returns
**long** Returns the managed reference Id. Returns [ManagedReferenceUtility.RefIdUnknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.RefIdUnknown.html) if the managed reference Id has not been assigned yet. 
### Description
Retrieves the managed reference Id for an object that is referenced using [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html).
Unity assigns an Id for an object when the Unity Object referencing the object has been serialized, or when [SetManagedReferenceIdForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html) is called.  
  
Additional resources: [SetManagedReferenceIdForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html), [GetManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.GetManagedReference.html), [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html). 
* * *
