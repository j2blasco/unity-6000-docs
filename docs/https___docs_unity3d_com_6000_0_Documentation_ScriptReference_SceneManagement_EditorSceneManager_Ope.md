* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenPreviewScene.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).OpenPreviewScene
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
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) OpenPreviewScene(string scenePath); 
### Parameters
Parameter | Description  
---|---  
scenePath | Scene file to open.  
### Returns
**Scene** The created preview Scene. 
### Description
Opens a Scene Asset in a preview Scene.
You can use this function for tooling that needs to access GameObjects but where the scene should not be displayed in the Hierarchy. Make sure to call [ClosePreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.ClosePreviewScene.html) to prevent leaking scenes.  
  
Additional resources: [NewPreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewPreviewScene.html), [ClosePreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.ClosePreviewScene.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;
using UnityEngine;  
  
public static class TestOpenAsPreviewScene
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Assets/Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Root Names")]
    static void OpenContextClickedSceneInAPreviewScene()
    {
        SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html) sceneAsset = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html);
        if (sceneAsset == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Context click on a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) file");
            return;
        }  
  
        var assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(sceneAsset);
        var scene = EditorSceneManager.OpenPreviewScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenPreviewScene.html)(assetPath);
        try
        {
            var rootGameObjects = scene.GetRootGameObjects();  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Root GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Names (count: {rootGameObjects.Length})");
            foreach (var gameObject in rootGameObjects)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(gameObject.name);
        }
        finally
        {
            EditorSceneManager.ClosePreviewScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.ClosePreviewScene.html)(scene);
        }
    }
}

```

* * *
