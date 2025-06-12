* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-progress.html

#  [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html).progress
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
progress; 
### Description
What's the operation's progress. (Read Only)
Return an operation's progress. (Read Only) This returns how close the operation is to finishing. The operation is finished when the progress float reaches 1.0 and isDone is called. If you set allowSceneActivation to false, progress is halted at 0.9 until it is set to true. This is extremely useful for creating loading bars.  
  
Additional resources: [isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html).
```
//This script lets you load a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) asynchronously. It uses an asyncOperation to calculate the progress and outputs the current progress to Text (could also be used to make progress bars).  
  
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Create a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) (**Create**>**UI**>**Button**) and a Text GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (**Create**>**UI**>**Text**) and attach them both to the Inspector of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//In Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), press your Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), and the Text changes depending on progress. Press the space key to activate the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
//**Note:** The progress may look like it goes straight to 100% if your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) doesn’t have a lot to load.  
  
using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;  
  
public class AsyncOperationProgressExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Text m_Text;
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) m_Button;  
  
    void Start()
    {
        //Call the LoadButton() function when the user clicks this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        m_Button.onClick.AddListener(LoadButton);
    }  
  
    void LoadButton()
    {
        //Start loading the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) asynchronously and output the progress bar
        StartCoroutine(LoadScene());
    }  
  
    IEnumerator LoadScene()
    {
        yield return null;  
  
        //Begin to load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) you specify
        AsyncOperation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) asyncOperation = SceneManager.LoadSceneAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html)("Scene3");
        //Don't let the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) activate until you allow it to
        asyncOperation.allowSceneActivation = false;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pro :" + asyncOperation.progress);
        //When the load is still in progress, output the Text and progress bar
        while (!asyncOperation.isDone)
        {
            //Output the current progress
            m_Text.text = "Loading progress: " + (asyncOperation.progress * 100) + "%";  
  
            // Check if the load has finished
            if (asyncOperation.progress >= 0.9f)
            {
                //Change the Text to show the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) is ready
                m_Text.text = "Press the space bar to continue";
                //Wait to you press the space key to activate the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
                if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
                    //Activate the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
                    asyncOperation.allowSceneActivation = true;
            }  
  
            yield return null;
        }
    }
}

```

* * *
