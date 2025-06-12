* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.ClearManagedReferenceWithMissingType.html

#  [SerializationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.html).ClearManagedReferenceWithMissingType
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
public static bool ClearManagedReferenceWithMissingType([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, long id); 
### Description
Drop the serialized data associated with a specific managed reference object that is missing its type.
This method returns false if there is no reference with a missing type matching the specified Id.  
  
Additional resources: [ClearAllManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.ClearAllManagedReferencesWithMissingTypes.html), [GetManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.GetManagedReferencesWithMissingTypes.html), [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html). 
* * *
