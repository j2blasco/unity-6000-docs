* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetOutermostPrefabInstanceRoot
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) GetOutermostPrefabInstanceRoot([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**GameObject** The outermost Prefab instance root. 
### Description
Retrieves the GameObject that is the root of the outermost Prefab instance the object is part of.
The method will search up the parents in the Transform hierarchy until it finds the root of a Prefab instance which is not an applied nested Prefab inside another Prefab.  
  
If the method finds a Prefab instance root which is an added GameObject to another Prefab instance, it will return that root, since it it not an applied nested Prefab root.  
  
The method will return null if the given object is not part of a Prefab instance. This includes GameObjects or components that have been added and not applied to a Prefab instance.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PrefabInstanceRoots.png)  
_Overview of which objects are Prefab instance roots._  
  
In the editor, outermost Prefab instance roots have the Overrides dropdown, whereas other Prefab instance roots don’t.  
  
Additional resources: [GetNearestPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetNearestPrefabInstanceRoot.html).
* * *
