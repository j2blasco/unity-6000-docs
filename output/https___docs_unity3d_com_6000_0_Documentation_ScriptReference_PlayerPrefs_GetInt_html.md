* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetInt.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).GetInt
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
public static int GetInt(string key); 
## Declaration
public static int GetInt(string key, int defaultValue); 
### Description
Returns the value corresponding to `key` in the preference file if it exists.
If it doesn't exist, PlayerPrefs.GetInt will return `defaultValue`.
```
//Use this script to fetch the settings and show them as text on the screen.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class PlayerPrefsGetIntExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int m_Score;  
  
    void Start()
    {
        //Fetch the PlayerPref settings
        SetText();
    }  
  
    void SetText()
    {
        //Fetch the score from the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) (set these PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) in another script). If no Int of this name exists, the default is 0.
        m_Score = PlayerPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetInt.html)("Score", 0);
    }  
  
    void OnGUI()
    {
        //Fetch the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings and output them to the screen using Labels
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 130, 200, 30), "Score : " + m_Score);
    }
}

```

* * *
