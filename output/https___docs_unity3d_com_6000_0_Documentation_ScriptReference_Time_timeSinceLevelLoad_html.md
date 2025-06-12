* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeSinceLevelLoad.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).timeSinceLevelLoad
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
timeSinceLevelLoad; 
### Description
The time in seconds since the last non-additive scene finished loading (Read Only).
This behaves in the same way as [Time.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) with a negative offset.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Create a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) (Create>UI>Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)) and a Text GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (Create>UI>Text)
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) and Text in the fields in the Inspector  
  
//This script outputs the time since the last level load. It also allows you to load a new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) by pressing the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html). When this new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) loads, the time resets and updates.  
  
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;  
  
public class TimeSinceLevelLoad : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) m_MyButton;
    public Text m_MyText;  
  
    void Awake()
    {
        // Don't destroy the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) when loading a new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        DontDestroyOnLoad(gameObject);
        // Make sure the Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) isn't deleted so the UI stays on the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) load
        DontDestroyOnLoad(GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html)"));  
  
        if (m_MyButton != null)
            // Add a listener to call the LoadSceneButton function when the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) is clicked
            m_MyButton.onClick.AddListener(LoadSceneButton);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Output the time since the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) loaded to the screen using this label
        m_MyText.text = "Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) Since Loaded : " + Time.timeSinceLevelLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeSinceLevelLoad.html);
    }  
  
    void LoadSceneButton()
    {
        // Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to load another Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        // Load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) named "Scene2"
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("Scene2");
    }
}

```

* * *
