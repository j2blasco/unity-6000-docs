* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.HasManagedReferencesWithMissingTypes.html

#  [SerializationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.html).HasManagedReferencesWithMissingTypes
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
public static bool HasManagedReferencesWithMissingTypes([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Description
This API returns true if one or more managed references is missing its type.
Managed references are objects that are referenced from a [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) or other "host" object using the [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) attribute. When managed references are serialized, their type information is persisted by recording the namespace, class name and assembly name.  
  
When an asset is deserialized, the recorded type information is used to reinstantiate the object. If the recorded type is missing during this process, then the fields on the C# object referencing that object remain null. However the persisted state of the object is retained and included when the asset is resaved.  
  
If the missing types become available at a later time, for example by adding a missing assembly or source file to the project, then the state of the Managed Reference object can be recovered.  
  
Additional resources: [GetManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.GetManagedReferencesWithMissingTypes.html), [ClearAllManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.ClearAllManagedReferencesWithMissingTypes.html), [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html). 
* * *
