* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetFloat.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).GetFloat
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
public static float GetFloat(string key); 
## Declaration
public static float GetFloat(string key, float defaultValue); 
### Description
Returns the value corresponding to `key` in the preference file if it exists.
If it doesn't exist, PlayerPrefs.GetFloat will return `defaultValue`.
```
//Use this script to fetch the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings and show them as text on the screen.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class PlayerPrefsDeleteAllExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float m_Health;  
  
    void Start()
    {
        //Fetch the PlayerPref settings
        SetText();
    }  
  
    void SetText()
    {
        //Fetch the health from the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) (set these PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) elsewhere). If no float of this name exists, the default is 0
        m_Health = PlayerPrefs.GetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetFloat.html)("Health", 0);
    }  
  
    void OnGUI()
    {
        //Fetch the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings and output them to the screen using Labels
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 90, 200, 30), "Health : " + m_Health);
    }
}

```

* * *
