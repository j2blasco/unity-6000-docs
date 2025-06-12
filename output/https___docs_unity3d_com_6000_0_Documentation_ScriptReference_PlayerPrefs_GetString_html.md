* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).GetString
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
public static string GetString(string key); 
## Declaration
public static string GetString(string key, string defaultValue); 
### Description
Returns the value corresponding to `key` in the preference file if it exists.
If it doesn't exist, PlayerPrefs.GetString will return `defaultValue`.
```
//Use this script to fetch the settings and show them as text on the screen.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class PlayerPrefsGetStringExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_PlayerName;  
  
    void Start()
    {
        //Fetch the PlayerPref settings
        SetText();
    }  
  
    void SetText()
    {
        //Fetch name (string) from the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) (set these PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) in another script). If no string exists, the default is "No Name"
        m_PlayerName = PlayerPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html)("Name", "No Name");
    }  
  
    void OnGUI()
    {
        //Fetch the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings and output them to the screen using Labels
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 50, 200, 30), "Name : " + m_PlayerName);
    }
}

```

* * *
