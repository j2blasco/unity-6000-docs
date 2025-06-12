* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).main
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) main; 
### Description
The first enabled Camera component that is tagged "MainCamera" (Read Only).
If there is no enabled Camera component with the "MainCamera" tag, this property is null.  
  
Internally, Unity caches all GameObjects with the "MainCamera" tag. When you access this property, Unity returns the first valid result from its cache. Accessing this property has a small CPU overhead, comparable to calling [GameObject.GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponent.html). Where CPU performance is important, consider caching this property.  
  
Additional resources: [Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html)
```
//Place this script on a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to switch between the main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and your own second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) on the press of the "L" key
//Place a second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and assign it as the "Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) Two" in the Inspector.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //This is Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) m_MainCamera;
    //This is the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and is assigned in inspector
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) m_CameraTwo;  
  
    void Start()
    {
        //This gets the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) from the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        m_MainCamera = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
        //This enables Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
        m_MainCamera.enabled = true;
        //Use this to disable secondary Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
        m_CameraTwo.enabled = false;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the L Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to switch cameras
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.L[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.L.html)))
        {
            //Check that the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) is enabled in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), then switch to the other Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) on a key press
            if (m_MainCamera.enabled)
            {
                //Enable the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
                m_CameraTwo.enabled = true;  
  
                //The Main first Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) is disabled
                m_MainCamera.enabled = false;
            }
            //Otherwise, if the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) is not enabled, switch back to the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) on a key press
            else if (!m_MainCamera.enabled)
            {
                //Disable the second camera
                m_CameraTwo.enabled = false;  
  
                //Enable the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
                m_MainCamera.enabled = true;
            }
        }
    }
}

```

* * *
