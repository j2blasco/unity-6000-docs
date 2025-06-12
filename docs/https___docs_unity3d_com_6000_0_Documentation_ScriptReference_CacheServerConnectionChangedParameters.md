* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerConnectionChangedParameters.html

# CacheServerConnectionChangedParameters
struct in UnityEditor
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
Struct used for [AssetDatabase.cacheServerConnectionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-cacheServerConnectionChanged.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CacheServerConnectionChangedExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Correct connection to the Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server")]
    static void CorrectChangeCacheServer()
    {
        var correctEndpoint = "192.168.1.210:8080";
        EditorSettings.cacheServerEndpoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEndpoint.html) = correctEndpoint;
        AssetDatabase.RefreshSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RefreshSettings.html)();
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Wrong connection to the Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Server")]
    static void WrongChangeCacheServer()
    {
        var invalidEndpoint = "Invalid IP Address";
        EditorSettings.cacheServerEndpoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEndpoint.html) = invalidEndpoint;
        AssetDatabase.RefreshSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RefreshSettings.html)();
    }  
  
    [InitializeOnLoadMethod]
    static void OncacheServerConnectionChanged()
    {
        AssetDatabase.cacheServerConnectionChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-cacheServerConnectionChanged.html) += ConsoleLog;
    }  
  
    static void ConsoleLog(CacheServerConnectionChangedParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerConnectionChangedParameters.html) param)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Connection Changed");
    }
}

```

* * *
