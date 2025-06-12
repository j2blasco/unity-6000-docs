* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteAll.html

#  [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).DeleteAll
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
Call this function in a script to delete all current settings in the [PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).  
  
The following example demonstrates creating a button that deletes all PlayerPrefs. 
```
//This example creates a button on the screen that deletes any PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings when you press it.
//Note that you must set values or keys in the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) first to see the button.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        //Delete all of the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings by pressing this button.
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 200, 200, 60), "Delete"))
        {
            PlayerPrefs.DeleteAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteAll.html)();
        }
    }
}

```

The following example demonstrates setting PlayerPrefs and deleting them afterwards. 
```
//First attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to set up the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html).  
  
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class SetUpPlayerPrefsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_PlayerName;  
  
    void Start()
    {
        m_PlayerName = "Enter Your Name";
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Give the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) some values to send over to the next Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        PlayerPrefs.SetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetFloat.html)("Health", 50.0F);
        PlayerPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetInt.html)("Score", 20);
        PlayerPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetString.html)("Name", m_PlayerName);
    }  
  
    void OnGUI()
    {
        //Create a Text Field where the user inputs their name
        m_PlayerName = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 20), m_PlayerName, 25);  
  
        //Create a button which loads the appropriate level when you press it
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 200, 60), "Next Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)"))
        {
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("Scene2");
        }
    }
}

```

```
//This other script shows how the values of the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) reset using the PlayerPrefs.DeleteAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteAll.html)() function.
//Open a different Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) (the one you named before- "Scene2") and attach this script to a new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Use this script to fetch the settings and show them as text on the screen.
//Use the button included in the script to delete all these settings and the text on the screen will also reset to reflect this.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class PlayerPrefsDeleteAllExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int m_Score;
    float m_Health;
    string m_PlayerName;  
  
    void Start()
    {
        //Fetch the PlayerPref settings
        SetText();
    }  
  
    void SetText()
    {
        //Fetch the score, health and name from the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) (set these Playerprefs in another script)
        m_Health = PlayerPrefs.GetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetFloat.html)("Health", 0);
        m_Score = PlayerPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetInt.html)("Score", 0);
        m_PlayerName = PlayerPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html)("Name", "No Name");
    }  
  
    void OnGUI()
    {
        //Fetch the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings and output them to the screen using Labels
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 50, 200, 30), "Name : " + m_PlayerName);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 90, 200, 30), "Health : " + m_Health);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 130, 200, 30), "Score : " + m_Score);  
  
        //Delete all of the PlayerPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) settings by pressing this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 0, 100, 30), "Delete"))
        {
            PlayerPrefs.DeleteAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteAll.html)();
            //Fetch the updated settings to change the Text
            SetText();
        }
    }
}

```

* * *
