* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html

#  [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html).allowSceneActivation
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
allowSceneActivation; 
### Description
Allow Scenes to be activated as soon as it is ready.
You can use this with [SceneManager.LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html) to delay the actual activation of the Scene and unloading of the previous Scene.  
  
When [allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) is set to false, Unity stops progress at 0.9, and [AsyncOperation.isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html) remains false. When [AsyncOperation.allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) is set to true, [isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html) can complete. While [isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html) is false, the [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) queue is stalled. For example, if a LoadSceneAsync.allowSceneActivation is set to false, and another [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) (e.g. [SceneManager.UnloadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html) ) initializes, Unity does not call the second operation until the first [AsyncOperation.allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) is set to true.  
  
You should set and use [AsyncOperation.allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) in coroutine functions. You cannot set and use [AsyncOperation.allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) within Awake, because this function is not a coroutine.
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
