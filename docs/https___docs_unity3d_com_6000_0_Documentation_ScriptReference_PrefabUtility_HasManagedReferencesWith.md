* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.HasManagedReferencesWithMissingTypes.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).HasManagedReferencesWithMissingTypes
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
public static bool HasManagedReferencesWithMissingTypes([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetComponentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | An object which is part of a Prefab asset.  
### Returns
**bool** Returns true if there are missing SerializeReference types directly within a Prefab asset excluding nested Prefab. 
### Description
Determines whether the object Prefab asset contains any MonoBehaviours with missing SerializeReference types.
This method returns true if the Prefab asset contains missing SerializeReference types. Applying property modifications to a Prefab asset removes missing type information from the Prefab Asset. However, editing a Prefab asset in Prefab Mode preserves missing type information. If you are on an instance, you can use [PrefabUtility.GetCorrespondingObjectFromSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html) to validate if the Prefab asset has missing types. Additional resources: [SerializationUtility.HasManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.HasManagedReferencesWithMissingTypes.html), [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)
* * *
