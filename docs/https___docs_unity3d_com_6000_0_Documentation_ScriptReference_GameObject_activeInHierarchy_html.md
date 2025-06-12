* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).activeInHierarchy
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
activeInHierarchy; 
### Description
The active state of the GameObject in the Scene hierarchy. True if active, false if inactive. (Read Only)
A GameObject is active in the scene hierarchy if [GameObject.activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) is `true` for the object and all parent objects. A GameObject is not active in the scene hierarchy if [GameObject.activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) is `false` for a parent object, even if [GameObject.activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) is `true` for the object itself.  
  
`GameObject.activeInHierarchy` changing to `false` triggers [MonoBehaviour.OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDisable.html) for attached scripts. `GameObject.activeInHierarchy` changing to `true` triggers [MonoBehaviour.OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnEnable.html). 
```
//This script shows how the activeInHierarchy state changes depending on the active state of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s parent  
  
using UnityEngine;  
  
public class ActiveInHierarchyExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Attach these in the Inspector
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_ParentObject, m_ChildObject;
    //Use this for getting the toggle data
    bool m_Activate;  
  
    void Start()
    {
        //Deactivate parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and toggle
        m_Activate = false;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Activate the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attach depending on the toggle output
        m_ParentObject.SetActive(m_Activate);
    }  
  
    void OnGUI()
    {
        //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) this toggle to activate and deactivate the parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Activate = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 30), m_Activate, "Activate Parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");  
  
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
        {
            //Output the status of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s active state in the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Active : " + m_ChildObject.activeInHierarchy);
        }
    }
}

```

Child objects of a deactivated parent GameObject may continue to be active according to [GameObject.activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) despite being invisible in the scene. [GameObject.activeInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html) is the reliable way to check if a GameObject has been effectively deactivated by the status of a parent object.
```
//This script shows how activeInHierarchy differs from activeSelf. Use the toggle  to alter the parent and child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s active states. This makes it output the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s state in the console.
//It also shows how activeSelf outputs that the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is active when the parent is not, while the activeInHierarchy lists the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as inactive.  
  

using UnityEngine;  
  
public class ActiveInHierarchyExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_ParentObject, m_ChildObject;
    //Use this for getting the toggle data
    bool m_ActivateParent, m_ActivateChild;
    //Use these for deciding if console is needing updated
    bool m_HierarchyOutput, m_SelfOutput;  
  
    void Start()
    {
        //Deactivate parent and child GameObjects and toggles
        m_ActivateParent = false;
        m_ActivateChild = false;
        //Ables script to output current state of GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to console
        m_HierarchyOutput = false;
        m_SelfOutput = false;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Activates the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attach depending on the toggle output
        m_ParentObject.SetActive(m_ActivateParent);
        m_ChildObject.SetActive(m_ActivateChild);  
  
        //Find out if the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is active in the Game and checks if this state has been output to the console
        if (m_HierarchyOutput == false)
        {
            //Output the state of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s activity if it hasn't already been output
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Object Active : " + m_ChildObject.activeInHierarchy);
            //The state of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is output already, so no need to do it again
            m_HierarchyOutput = true;
        }
        //Check to see if the assigned GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is active despite parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s status
        if (m_ChildObject.activeSelf && m_SelfOutput == false)
        {
            //Output the message if the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is still active
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child Active, parent might not be");
            //You no longer need to output the message
            m_SelfOutput = true;
        }
    }  
  
    void OnGUI()
    {
        //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) this toggle to activate and deactivate the parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_ActivateParent = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 30), m_ActivateParent, "Activate Parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");
        //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) this toggle to activate and deactivate the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_ActivateChild = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 100, 30), m_ActivateChild, "Activate Child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");  
  

        //If a change is detected with the toggle, the console outputs updates
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
        {
            m_SelfOutput = false;
            m_HierarchyOutput = false;
        }
    }
}

```

* * *
