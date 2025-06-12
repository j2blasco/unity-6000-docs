* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetButtonDown
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
public static bool GetButtonDown(string buttonName); 
### Description
Returns true during the frame the user pressed down the virtual button identified by `buttonName`.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Call this function from the [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) function, since the state gets reset each frame. It will not return true until the user has released the key and pressed it again.  
  
Use this only when implementing action like events IE: shooting a weapon.  
Use [Input.GetAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html) for any kind of movement behaviour.  
  
To edit, set up, or remove buttons and their names (such as "Fire1"): 1. Go to **Edit** > **Project Settings** > **Input Manager** to bring up the Input Manager. 2. Expand **Axis** by clicking the arrow next to it. This shows the list of the current buttons you have. You can use one of these as the parameter "buttonName". 3. Expand one of the items in the list to access and change aspects such as the button's name and the key, joystick or mouse movement that triggers it. 4. For more information about buttons, see the [Input Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) page.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) projectile;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Fire1"))
            Instantiate(projectile, transform.position, transform.rotation);
    }
}

```

* * *
