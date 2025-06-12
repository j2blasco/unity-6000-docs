* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetObjectOverrides.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetObjectOverrides
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
public static List<ObjectOverride> GetObjectOverrides([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabInstance, bool includeDefaultOverrides); 
### Parameters
Parameter | Description  
---|---  
prefabInstance | The Prefab instance to get information about.  
includeDefaultOverrides | If true, components will also be included even if they only contain overrides that are [default overrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html). False by default.  
### Returns
**List <ObjectOverride>** List of objects with information about object overrides. 
### Description
Retrieves a list of objects with information about object overrides on the Prefab instance.
If includeDefaultOverrides is true, components will also be included even if they only contain overrides that are [default overrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html). This parameter is false by default.  
  
Additional resources: [ObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.ObjectOverride.html)
* * *
