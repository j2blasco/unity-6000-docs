* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteAll.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).DeleteAll
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
public static void DeleteAll(); 
### Description
Removes all keys and values from the preferences. Use with caution.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ClearEditorPrefs.png)   
_Clears all editor prefs keys._
```
// Clear all the editor prefs keys.
//
// Warning: this will also remove editor preferences as the opened projects, etc.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class DeleteAllExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/EditorPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html)/Clear all Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Preferences")]
    static void deleteAllExample()
    {
        if (EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Delete all editor preferences.",
            "Are you sure you want to delete all the editor preferences? " +
            "This action cannot be undone.", "Yes", "No"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("yes");
            EditorPrefs.DeleteAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteAll.html)();
        }
    }
}

```

* * *
