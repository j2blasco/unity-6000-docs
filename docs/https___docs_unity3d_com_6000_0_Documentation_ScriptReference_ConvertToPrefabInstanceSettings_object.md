* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-objectMatchMode.html

#  [ConvertToPrefabInstanceSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html).objectMatchMode
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
[ObjectMatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.html) objectMatchMode; 
### Description
Use this property to control how GameObjects and Components are matched up or not when converting a plain GameObject to a Prefab instance.
The root GameObject and its components will always be matched up regardless of the ObjectMatchMode so a reference to the root GameObject will always be retained regardless of ObjectMatchMode. Use [ObjectMatchMode.ByHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByHierarchy.html) which will retain references if GameObjects and Components are matched up using their full hierarchy path. In this mode you can use [componentsNotMatchedBecomesOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-componentsNotMatchedBecomesOverride.html) and [gameObjectsNotMatchedBecomesOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-gameObjectsNotMatchedBecomesOverride.html) to control what happens with objects that are not matched up. Alternatively use [ObjectMatchMode.ByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByName.html) will retain references if individual GameObject names matches up. Note that the hierarchy of GameObjects are ignored and only the GameObject name is used for matching. Only if a GameObject have the same name and same Transform type as in the used Prefab Asset then they are matched up. Components have their GameObject name prefixed to their type name for the final name matching. If the name is found more than once in the Prefab Asset or in the instance then the match cannot be performed; the name must be unique in each GameObject hierarchy.
* * *
