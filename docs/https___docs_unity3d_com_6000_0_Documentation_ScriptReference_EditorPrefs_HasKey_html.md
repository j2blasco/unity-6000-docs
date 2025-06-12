* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).HasKey
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
public static bool HasKey(string key); 
### Parameters
Parameter | Description  
---|---  
key | Name of key to check for.  
### Returns
**bool** The existence or not of the key. 
### Description
Returns true if `key` exists in the preferences file.
The preferences file is examined to identify whether the specified key exists. True or false is returned. In the following example a key and value can be written into the preference file, or deleted. The existence of the key is checked with the [HasKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html) function and a message displayed.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorPrefsHasKey.png)  
_Use save, delete, and HasKey preference check._
```
// Small example where the XyZ key can be saved or deleted from the Preferences file.
// The existence of the key is checked using the HasKey() function.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class HasKeyExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    private string keyName = "XyZ";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/HasKey Example")]
    static void Init()
    {
        HasKeyExample window = (HasKeyExample)EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)(
            typeof(HasKeyExample), new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 250, 80));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Save '" + keyName + "' as Key"))
            EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)(keyName, "abc123");  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Delete Key '" + keyName + "'"))
            EditorPrefs.DeleteKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteKey.html)(keyName);  
  
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(keyName + " key exists: " + EditorPrefs.HasKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html)(keyName));  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }  
  
    // delete the key each time the demo starts
    void OnFocus()
    {
        EditorPrefs.DeleteKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteKey.html)(keyName);
    }
}

```

* * *
