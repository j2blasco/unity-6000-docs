* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.html

# RemovedGameObject
class in UnityEditor.SceneManagement
/
Inherits from:[SceneManagement.PrefabOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabOverride.html)
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
Class with information about a GameObject that has been removed from a Prefab instance.
Additional resources: [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html), [PrefabUtility.RevertRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedGameObject.html), [PrefabUtility.GetRemovedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html).
### Properties
Property | Description  
---|---  
[assetGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject-assetGameObject.html) | The GameObject in the Prefab Asset that has been removed in the Prefab instance.  
[parentOfRemovedGameObjectInInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject-parentOfRemovedGameObjectInInstance.html) | The parent of the removed GameObject in the instance.  
### Public Methods
Method | Description  
---|---  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.Apply.html) | See: PrefabOverride.Apply.  
[GetAssetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.GetAssetObject.html) | See PrefabOverride.GetAssetObject.  
[Revert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.Revert.html) | Restore the removed GameObject to the Prefab instance. See PrefabOverride.Revert.  
### Inherited Members
### Protected Methods
Method | Description  
---|---  
[FindApplyTargetAssetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabOverride.FindApplyTargetAssetObject.html) | Finds the object in the Prefab Asset at the given path which will be applied to.  
* * *
