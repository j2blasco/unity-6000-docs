* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.HasPrefabInstanceAnyOverrides.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).HasPrefabInstanceAnyOverrides
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
public static bool HasPrefabInstanceAnyOverrides([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, bool includeDefaultOverrides); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | The root GameObject of the Prefab instance to check.  
includeDefaultOverrides | Set to true to consider default overrides as overrides too.  
### Returns
**bool** Returns true if there are any overrides. 
### Description
Returns true if the given Prefab instance has any overrides.
This method is the quickest way to check if a Prefab instance has any overrides, when not needing to know what those overrides are.  
  
The includeDefaultOverrides parameter should normally be set to false, except for debugging purposes. If set to true, the method will normally return true for all Prefabs instances, since all Prefab instances have default overrides for the root position and rotation, among others.
* * *
