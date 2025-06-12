* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetPreloadedAssets.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetPreloadedAssets
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static Object[] GetPreloadedAssets(); 
### Returns
**Object[]** The assets to be preloaded. 
### Description
Returns the assets that will be loaded at start up in the player and be kept alive until the player terminates.
This example shows how a ScriptableObject can be used to store data that can be accessed at any time throughout the lifetime of the player.
```
using System.Linq;
using UnityEngine;  
  
// We use this class to store general config data that can be used in the player
public class ConfigObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string text;  
  
    public static ConfigObject configInstance;  
  
    #if UNITY_EDITOR
    [UnityEditor.MenuItem("Assets/Create/Config Object")]
    public static void CreateAsset()
    {
        var path = UnityEditor.EditorUtility.SaveFilePanelInProject("Save Config", "config", "asset", string.Empty);
        if (string.IsNullOrEmpty(path))
            return;  
  
        var configObject = CreateInstance<ConfigObject>();
        UnityEditor.AssetDatabase.CreateAsset(configObject, path);  
  
        // Add the config asset to the build
        var preloadedAssets = UnityEditor.PlayerSettings.GetPreloadedAssets().ToList();
        preloadedAssets.Add(configObject);
        UnityEditor.PlayerSettings.SetPreloadedAssets(preloadedAssets.ToArray());
    }
    #endif  
  
    void OnEnable()
    {
        configInstance = this;
    }
}

```

```
using UnityEngine;  
  
public class UseConfigObject : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (ConfigObject.configInstance != null)
        {
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Found the config asset. The message was: " + ConfigObject.configInstance.text);
        }
    }
}

```

* * *
