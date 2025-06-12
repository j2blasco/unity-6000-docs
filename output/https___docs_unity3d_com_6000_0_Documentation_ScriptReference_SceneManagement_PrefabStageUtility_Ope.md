* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStageUtility.OpenPrefab.html

#  [PrefabStageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStageUtility.html).OpenPrefab
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
public static [SceneManagement.PrefabStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.html) OpenPrefab(string prefabAssetPath); 
## Declaration
public static [SceneManagement.PrefabStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.html) OpenPrefab(string prefabAssetPath, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) openedFromInstance); 
## Declaration
public static [SceneManagement.PrefabStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.html) OpenPrefab(string prefabAssetPath, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) openedFromInstance, [SceneManagement.PrefabStage.Mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.Mode.html) prefabStageMode); 
### Parameters
Parameter | Description  
---|---  
prefabAssetPath | File path for the Prefab Asset to open in Prefab Mode.  
openedFromInstance | Opens Prefab Mode in context of this Prefab instance GameObject.  
prefabStageMode | Mode that determines whether to open in isolation or in context.  
### Returns
**PrefabStage** The opened PrefabStage. 
### Description
Opens a Prefab Asset in Prefab Mode.
After opening Prefab Mode you can return to the main scenes by using [StageUtility.GoToMainStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.GoToMainStage.html). See also: [Editing in Prefab Mode](https://docs.unity3d.com/Manual/EditingInPrefabMode.html).
* * *
