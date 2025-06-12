* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetNearestPrefabInstanceRoot.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetNearestPrefabInstanceRoot
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) GetNearestPrefabInstanceRoot([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**GameObject** The nearest Prefab instance root. 
### Description
Retrieves the GameObject that is the root of the nearest Prefab instance the object is part of.
The method searches the Transform hierarchy until it finds the root of any Prefab instance, regardless of whether that instance is an applied nested Prefab inside another Prefab, or not.  
  
The method returns null if the given object is not part of a Prefab instance. This includes GameObjects or components that have been added and not applied to a Prefab instance.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PrefabInstanceRoots.png)  
_Overview of which objects are Prefab instance roots._  
  
In the editor, Prefab instance roots have Open and Select buttons, and in the case of an outermost Prefab instance root, an Overrides dropdown.  
  
Additional resources: [GetOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html).
* * *
