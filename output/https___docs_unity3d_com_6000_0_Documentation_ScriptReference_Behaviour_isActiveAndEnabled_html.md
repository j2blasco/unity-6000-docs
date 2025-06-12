* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html

#  [Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html).isActiveAndEnabled
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
isActiveAndEnabled; 
### Description
Reports whether a GameObject and its associated Behaviour is active and enabled.
A GameObject can be active or inactive. Similarly, a Behaviour can be enabled or disabled. If a GameObject is active and has an enabled behaviour then [isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) will return `true`. Otherwise `false` is returned.  
**Note:** value is `ReadOnly`.  
To determine whether GameObject is active, [isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) uses the equivalent of [activeInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html).
```
using UnityEngine;
using System.Collections;
using UnityEngine.UI;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) pauseMenu;  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Checks if the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) are active and enabled.
        if (pauseMenu.isActiveAndEnabled)
        {
            //If the Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) is enabled, print "Enabled" in the console. Stops when the image or GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is disabled.
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Enabled");
        }
    }
}

```

* * *
