* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerPort.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetCacheServerPort
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
public static ushort GetCacheServerPort(); 
### Returns
**ushort** Returns the Port number of the Cache Server in Editor Settings. Returns 0 if Port number is not set in Editor Settings. 
### Description
Gets the Port number of the Cache Server in Editor Settings.
Note: If you set a new value for the Port number, your new settings are not applied until you call AssetDatabase.RefreshSettings(). However, this method will return the value you have set regardless of whether you have applied the setting or no.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)  
  
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Debugging Connection to the Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server")]
    static void DebuggingConnectionToTheCacheServer()
    {
        //This will Enable Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server in Project Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)
        EditorSettings.cacheServerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerMode.html) = CacheServerMode.Enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerMode.Enabled.html);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server Enabled? - " + AssetDatabase.IsCacheServerEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsCacheServerEnabled.html)());  
  
        var cacheServerIP = "10.37.44.195";
        ushort cacheServerPort = 10443;  
  
        if (AssetDatabase.IsConnectedToCacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsConnectedToCacheServer.html)() == false)
        {
            if (AssetDatabase.CanConnectToCacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanConnectToCacheServer.html)(cacheServerIP, cacheServerPort) == false)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) server is not available, check IP address and Port[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Port.html) Number");
            }  
  
            else
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) server is available, but not connected now. Set correct IP and Port[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Port.html) Number in Project Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)");
            }
        }  
  
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server is connected");
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server IP: " + AssetDatabase.GetCacheServerAddress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerAddress.html)());
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server Port[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Port.html) Number: " + AssetDatabase.GetCacheServerPort[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerPort.html)());
        }
    }
}
```

* * *
