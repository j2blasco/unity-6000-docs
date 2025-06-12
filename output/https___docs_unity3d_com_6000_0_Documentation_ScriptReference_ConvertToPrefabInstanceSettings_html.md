* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html

# ConvertToPrefabInstanceSettings
class in UnityEditor
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
### Description
Settings controlling the behavior of [PrefabUtility.ConvertToPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstance.html).
### Properties
Property | Description  
---|---  
[changeRootNameToAssetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-changeRootNameToAssetName.html) | Change the name of the root GameObject to match the name of the Prefab Asset used when converting.  
[componentsNotMatchedBecomesOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-componentsNotMatchedBecomesOverride.html) | If a Component is not matched up then it can become an added Component on the new Prefab instance. This property is only used when used together with ObjectMatchMode.ByHierarchy.  
[gameObjectsNotMatchedBecomesOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-gameObjectsNotMatchedBecomesOverride.html) | If a GameObject is not matched up then it can become an added GameObject on the new Prefab instance. This property is only used when used together with ObjectMatchMode.ByHierarchy.  
[logInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-logInfo.html) | Enables logging to the console with information about which objects were matched when converting a plain GameObject to a Prefab instance.  
[objectMatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-objectMatchMode.html) | Use this property to control how GameObjects and Components are matched up or not when converting a plain GameObject to a Prefab instance.  
[recordPropertyOverridesOfMatches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings-recordPropertyOverridesOfMatches.html) | When a Component or GameObject is matched with objects in the Prefab Asset then existing values can be recorded as overrides on the new Prefab instance if this property is set to true.  
* * *
