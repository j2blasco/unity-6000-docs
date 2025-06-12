* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).SetInt
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
public static void SetInt(string key, int value); 
### Parameters
Parameter | Description  
---|---  
key | Name of key to write integer to.  
value | Value of the integer to write into the storage.  
### Description
Sets the value of the preference identified by key as an integer.
Sets the value of the preference identified by `key` as an integer.  
  
Additional resources: [GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html). 
```
// A small editor window that allows an integer value to be
// read and written to the EditorPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html) online storage.
//
// SetIntExample is the name of the int to read/write.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int intValue = 42;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Prefs.SetInt Example")]
    static void Init()
    {
        ExampleClass window = (ExampleClass)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(ExampleClass));
        window.Show();
    }  
  
    void OnGUI()
    {
        int temp;
        temp = EditorPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html)("SetIntExample", -1);
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Current stored value: " + temp.ToString());
        intValue = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Value to write to Prefs: ", intValue);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Save value: " + intValue.ToString()))
        {
            EditorPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html)("SetIntExample", intValue);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("SetInt: " + intValue);
        }
    }
}

```

* * *
