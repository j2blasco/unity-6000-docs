* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html

# EditorPrefs
class in UnityEditor
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
Stores and accesses Unity Editor preferences.
On macOS, EditorPrefs are stored in `~/Library/Preferences/com.unity3d.UnityEditor5.x.plist`.  
  
On Windows, EditorPrefs are stored in the registry under the `HKCU\Software\Unity Technologies\Unity Editor 5.x` key.  
  
On Linux, EditorPrefs are stored in `~/.local/share/unity3d/prefs`. 
### Static Methods
Method | Description  
---|---  
[DeleteAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteAll.html) | Removes all keys and values from the preferences. Use with caution.  
[DeleteKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.DeleteKey.html) | Removes key and its corresponding value from the preferences.  
[GetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetBool.html) | Returns the value corresponding to key in the preference file if it exists.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetFloat.html) | Returns the float value corresponding to key if it exists in the preference file.  
[GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html) | Returns the value corresponding to key in the preference file if it exists.  
[GetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetString.html) | Returns the value corresponding to key in the preference file if it exists.  
[HasKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html) | Returns true if key exists in the preferences file.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html) | Sets the value of the preference identified by key.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetFloat.html) | Sets the float value of the preference identified by key.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html) | Sets the value of the preference identified by key as an integer.  
[SetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html) | Sets the value of the preference identified by key. Note that EditorPrefs does not support null strings and will store an empty string instead.  
* * *
