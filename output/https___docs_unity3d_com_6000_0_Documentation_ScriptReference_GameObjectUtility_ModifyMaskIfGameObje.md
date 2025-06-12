* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.ModifyMaskIfGameObjectIsHiddenForPrefabModeInContext.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).ModifyMaskIfGameObjectIsHiddenForPrefabModeInContext
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
public static ulong ModifyMaskIfGameObjectIsHiddenForPrefabModeInContext(ulong sceneCullingMask, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
sceneCullingMask | The scene culling mask intended to be used with the custom renderer.  
gameObject | The GameObject associated with the custom renderer.  
### Returns
**ulong** If the GameObject is hidden for Prefab Mode in Context, a modified scene culling mask is returned. If it's not hidden, then the input scene culling mask is returned. 
### Description
Use this method if a custom scene culling mask is needed for renderers that should be shown or hidden in a Scene view when Prefab Mode in Context is active.
When entering Prefab Mode in Context for a Prefab Asset the Prefab instance in the Main Stage is hidden. Use this method to ensure that any custom renderers associated with a given GameObject are hidden in the same Scene views if that GameObject is part of a hidden Prefab instance.
* * *
