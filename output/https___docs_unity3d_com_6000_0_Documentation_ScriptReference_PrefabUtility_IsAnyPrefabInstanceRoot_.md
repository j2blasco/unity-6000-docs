* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsAnyPrefabInstanceRoot.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsAnyPrefabInstanceRoot
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
public static bool IsAnyPrefabInstanceRoot([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to check.  
### Returns
**bool** True if the GameObject is the root GameObject of any Prefab instance. 
### Description
Is the GameObject the root of any Prefab instance?
Returns true if the GameObject is the root GameObject of a Prefab instance or the root GameObject of a nested Prefab.  
  
This also returns true for a root GameObject of a nested Prefab instance inside a Prefab Asset.  
  
The method return false for the root GameObject of a Prefab Asset itself, except if it’s a Prefab Variant, in which case it returns true.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PrefabInstanceRoots.png)  
_Overview of which objects are Prefab instance roots._  
  
Additional resources: [IsOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsOutermostPrefabInstanceRoot.html).
* * *
