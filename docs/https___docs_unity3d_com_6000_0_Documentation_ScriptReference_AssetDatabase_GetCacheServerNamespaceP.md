* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerNamespacePrefix.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetCacheServerNamespacePrefix
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
public static string GetCacheServerNamespacePrefix(); 
### Returns
**string** Returns the Namespace prefix for the Cache Server. 
### Description
Gets the Cache Server Namespace prefix set in Editor Settings.
Note: If you set a new value for the Namespace prefix your new settings are not applied until you call AssetDatabase.RefreshSettings(). However, this method will return the value you have set regardless of whether you have applied the setting or no.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)  
  
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Set Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server Project Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)")]
    static void SetCacheServerProjectSettings()
    {
        EditorSettings.cacheServerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerMode.html) = CacheServerMode.Enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerMode.Enabled.html);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server enabled? - " + AssetDatabase.IsCacheServerEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsCacheServerEnabled.html)());  
  
        EditorSettings.cacheServerEndpoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEndpoint.html) = "192.168.31.210:10443";
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server IP and Port[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Port.html) number: " + AssetDatabase.GetCacheServerAddress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerAddress.html)() + ":" + AssetDatabase.GetCacheServerPort[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerPort.html)());  
  
        EditorSettings.cacheServerEnableAuth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableAuth.html) = false;
        EditorSettings.cacheServerEnableTls[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableTls.html) = false;  
  
        EditorSettings.cacheServerEnableDownload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableDownload.html) = true;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server download enabled? - " + AssetDatabase.GetCacheServerEnableDownload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerEnableDownload.html)());  
  
        EditorSettings.cacheServerEnableUpload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableUpload.html) = true;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server upload enabled? - " + AssetDatabase.GetCacheServerEnableUpload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerEnableUpload.html)());  
  
        EditorSettings.cacheServerNamespacePrefix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerNamespacePrefix.html) = "default";
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server Namespace prefix: " + AssetDatabase.GetCacheServerNamespacePrefix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerNamespacePrefix.html)());  
  
        //This command is required to apply changes to some of the EditorSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html) properties above
        AssetDatabase.RefreshSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RefreshSettings.html)();
    }
}
```

* * *
