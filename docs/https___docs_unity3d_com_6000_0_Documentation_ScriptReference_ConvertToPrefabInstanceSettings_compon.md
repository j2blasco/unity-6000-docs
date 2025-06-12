* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-componentsNotMatchedBecomesOverride.html

#  [ConvertToPrefabInstanceSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html).componentsNotMatchedBecomesOverride
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
componentsNotMatchedBecomesOverride; 
### Description
If a Component is not matched up then it can become an added Component on the new Prefab instance. This property is only used when used together with [ObjectMatchMode.ByHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByHierarchy.html).
If this property is false then the Component will be deleted if it doesn't match a Component on the PrefabAsset. Additional resources: [gameObjectsNotMatchedBecomesOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-gameObjectsNotMatchedBecomesOverride.html), [recordPropertyOverridesOfMatches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-recordPropertyOverridesOfMatches.html).
* * *
