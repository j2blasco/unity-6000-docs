* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnDestroy()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Destroying the attached Behaviour will result in the game or Scene receiving [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html).
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) occurs when a Scene or game ends. Stopping the Play mode when running from inside the Editor will end the application. As this end happens an [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) will be executed. Also, if a Scene is closed and a new Scene is loaded the [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) call will be made.  
When built as a standalone application [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) calls are made when Scenes end. A Scene ending typically means a new Scene is loaded.  
  
**Note:** [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) will only be called on game objects that have previously been active.  
  
  
  
In the following scripts the behaviour of [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) is shown. When running inside `ExampleClass1` a button is available. Using this button calls [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) and then switches to `ExampleClass2`. Once `ExampleClass2` is active [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) will be used when the application is closed. If `ExampleClass1` quits by closing the application it will call [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html). (In the build and run of the application the console displays the text output to the Player Log.)  
  
**Warning** : If the user suspends your application on a mobile platform, the operating system can quit the application to free up resources. In this case, depending on the operating system, Unity might be unable to call this method. On mobile platforms, it is best practice to not rely on this method to save the state of your application. Instead, consider every loss of application focus as the exit of the application and use [MonoBehaviour.OnApplicationFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) to save any data. 
```
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;  
  
public class ExampleClass1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float timePass = 0.0f;
    private int updateCount = 0;  
  
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start1");
    }  
  
    // code that generates a message every second
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        timePass += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        if (timePass > 1.0f)
        {
            timePass = 0.0f;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Update1: " + updateCount);
            updateCount = updateCount + 1;
        }
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 250, 60), "Change to scene2"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Exit1");
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)(1);
        }
    }  
  
    // generate a message before the Start() function
    void OnEnable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnEnable1");
    }  
  
    // generate a message when the game shuts down or switches to another Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
    // or switched to ExampleClass2
    void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDestroy1");
    }
}

```

ExampleClass2: 
```
using UnityEngine;
using UnityEngine.UI;  
  
public class ExampleClass2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start2");
    }  
  
    void OnEnable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnEnable2");
    }  
  
    // generate a message when the game shuts down
    void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDestroy2");
    }
}

```

[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) cannot be a co-routine.
* * *
