* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.EnsureUniqueNameForSibling.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).EnsureUniqueNameForSibling
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
public static void EnsureUniqueNameForSibling([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) self); 
### Parameters
Parameter | Description  
---|---  
self | The GameObject whose name you want to ensure is unique.  
### Description
You can use this method _after_ parenting one GameObject to another to ensure the child GameObject has a unique name compared to its siblings in the hierarchy.
If the GameObject already has a unique name compared to its siblings, its name will remain unchanged. If the GameObject has the same name as one of its siblings, Unity will rename it to a unique name by using an incremental number after the GameObject’s current name. This is useful when trying to avoid duplicate naming.  
  
Additional resources: [GameObjectUtility.GetUniqueNameForSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.GetUniqueNameForSibling.html), [ObjectNames.GetUniqueName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.GetUniqueName.html).
* * *
