* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsOutermostPrefabInstanceRoot.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsOutermostPrefabInstanceRoot
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
public static bool IsOutermostPrefabInstanceRoot([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to check.  
### Returns
**bool** True if the GameObject is an outermost Prefab instance root. 
### Description
Returns true if the given GameObject is an outermost Prefab instance root.
Returns true if the GameObject is the root GameObject of a Prefab instance, which is not itself part of another Prefab instance.  
  
This also returns true for outermost Prefab instance roots inside a Prefab Asset. Note that a Prefab Asset is not in itself a Prefab instance, but it may contain Prefab instances.  
  
If the GameObject is a Prefab instance root which is an added GameObject to another Prefab instance, it will return true, since it is not itself part of another Prefab instance.  
  
The method will return false if the given object is not part of a Prefab instance. This includes GameObjects that have been added and not applied to a Prefab instance.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PrefabInstanceRoots.png)  
_Overview of which objects are Prefab instance roots._  
  
In the editor, outermost Prefab instance roots have the Overrides dropdown, whereas other Prefab instance roots don’t.  
  
Additional resources: [IsAnyPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsAnyPrefabInstanceRoot.html).
* * *
