* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.html

# PrefabAssetType
enumeration
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
Enum indicating the type of Prefab Asset, such as Regular, Model and Variant.
For an object on a Prefab Asset, the asset itself is checked. For an object on a Prefab instance, its corresponding asset is checked.
### Properties
Property | Description  
---|---  
[NotAPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.NotAPrefab.html) | The object being queried is not part of a Prefab at all.  
[Regular](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.Regular.html) | The object being queried is part of a regular Prefab.  
[Model](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.Model.html) | The object being queried is part of a Model Prefab.  
[Variant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.Variant.html) | The object being queried is part of a Prefab Variant.  
[MissingAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.MissingAsset.html) | The object being queried is part of a Prefab instance, but because the asset is missing the actual type of Prefab can’t be determined.  
* * *
