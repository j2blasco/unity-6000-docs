* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings-objectMatchMode.html

#  [PrefabReplacingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings.html).objectMatchMode
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
Use this property to control if GameObjects and Components should be matched up when replacing the Prefab Asset of an Prefab instance.
Using [ObjectMatchMode.ByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByName.html) will retain references and added objects if names match up. Note that the hierarchy of GameObjects are ignored and only the GameObject name is used for matching. Only if a GameObject have the same name and Transform type is found in both the new Prefab Asset and in the Prefab instance then they are matched up. Components have their GameObject name prefixed to their type name for the final name matching. If the name is found more than once in the Prefab Asset or in the instance then the match cannot be performed; the name must be unique in each GameObject hierarchy.
* * *
