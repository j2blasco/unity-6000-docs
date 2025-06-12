* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).SetActiveScene
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
public static bool SetActiveScene([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | The Scene to be set.  
### Returns
**bool** Returns false if the Scene is not loaded yet. 
### Description
Set the Scene to be active.
The active Scene is the Scene which will be used as the target for new GameObjects instantiated by scripts and from what Scene the lighting settings are used. When you add a Scene additively (see [LoadSceneMode.Additive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html)), the first Scene is still kept as the active Scene. Use this to switch the active Scene to the Scene you want as the target.  
  
There must always be one Scene marked as the active Scene. Note the active Scene has no impact on what Scenes are rendered.
```
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
// Create 2 Buttons (**Create**>**UI**>**Button**)
// Attach the 2 Buttons to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Inspector  
  
// This script allows you to load a second Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) as an Additive Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). Click the first Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) (Load Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)) to load the Additive Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). Even though the second Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) loads, the first Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) remains the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// If you press the second Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) (Set Active Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)), it sets the second Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) as the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) (and outputs the current active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to the console)  
  

using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    bool m_SceneLoaded;
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) m_LoadSceneButton, m_SetActiveButton;  
  
    void Awake()
    {
        // Outputs the current active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) : " + SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)().name);  
  
        // Check that this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) exists
        if (m_LoadSceneButton != null)
        {
            // Fetch the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) from the Inspector. Make sure to set this in the Inspector window
            Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) loadButton = m_LoadSceneButton.GetComponent<Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)>();  
  
            // Call the LoadScene2Button() function when this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) is clicked
            loadButton.onClick.AddListener(LoadSceneButton);
        }  
  
        if (m_SetActiveButton != null)
        {
            Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) buttonTwo = m_SetActiveButton.GetComponent<Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)>();
            buttonTwo.onClick.AddListener(SetActiveSceneButton);
        }
    }  
  
    // Load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) when this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) is pressed
    void LoadSceneButton()
    {
        // Check that the second Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) hasn't been added yet
        if (m_SceneLoaded == false)
        {
            // Loads the second Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("Scene2", LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));  
  
            // Outputs the name of the current active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
            // Notice it still outputs the name of the first Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) : " + SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)().name);  
  
            // The Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) has been loaded, exit this method
            m_SceneLoaded = true;
        }
    }  
  
    // Change the newly loaded Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to be the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) if it is loaded
    void SetActiveSceneButton()
    {
        // Allow this other Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to be pressed when the other Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) has been pressed (Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) 2 is loaded)
        if (m_SceneLoaded == true)
        {
            // Set Scene2 as the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
            SceneManager.SetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html)(SceneManager.GetSceneByName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByName.html)("Scene2"));  
  
            // Ouput the name of the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
            // See now that the name is updated
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) : " + SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)().name);
        }
    }
}

```

* * *
