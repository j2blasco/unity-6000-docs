* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.AddListener.html

#  [UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html).AddListener
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
public void AddListener([Events.UnityAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction.html) call); 
### Parameters
Parameter | Description  
---|---  
call | Callback function.  
### Description
Adds a non-persistent listener to the UnityEvent.
Adds a runtime callback. You can add many different listeners. If you add identical listeners multiple times, it results in only one call being made to that specific listener.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script creates a UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) that calls a method when a key is pressed
//Note that 'q' exits this application.
using UnityEngine;
using UnityEngine.Events;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) m_MyEvent = new UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html)();  
  
    void Start()
    {
        //Add a listener to the new Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html). Calls MyAction method when invoked
        m_MyEvent.AddListener(MyAction);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Press Q to close the Listener
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("q") && m_MyEvent != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Quitting");
            m_MyEvent.RemoveListener(MyAction);  
  
            #if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
            #endif  
  
            Application.Quit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Quit.html)();
        }  
  
        //Press any other key to begin the action if the Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) exists
        if (Input.anyKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-anyKeyDown.html) && m_MyEvent != null)
        {
            //Begin the action
            m_MyEvent.Invoke();
        }
    }  
  
    void MyAction()
    {
        //Output message to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do Stuff");
    }
}

```

Additional resources: [UnityEventTools.AddPersistentListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.AddPersistentListener.html).
* * *
