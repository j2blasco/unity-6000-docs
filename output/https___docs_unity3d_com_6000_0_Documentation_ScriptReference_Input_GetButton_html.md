* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetButton
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
public static bool GetButton(string buttonName); 
### Parameters
Parameter | Description  
---|---  
buttonName | The name of the button such as Jump.  
### Returns
**bool** True when an axis has been pressed and not released. 
### Description
Returns true while the virtual button identified by `buttonName` is held down.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Think auto fire - this will return true as long as the button is held down. Use this only when implementing events that trigger an action, eg, shooting a weapon. The `buttonName` argument will normally be one of the names in [InputManager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) such as Jump or Fire1. [GetButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html) will return to `false` when it is released.  
  
**Note:** Use [GetAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html) for input that controls continuous movement.
```
// Instantiates a projectile every 0.5 seconds,
// if the Fire1 button (default is Ctrl) is pressed.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) projectile;
    public float fireDelta = 0.5F;  
  
    private float nextFire = 0.5F;
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) newProjectile;
    private float myTime = 0.0F;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        myTime = myTime + Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Fire1") && myTime > nextFire)
        {
            nextFire = myTime + fireDelta;
            newProjectile = Instantiate(projectile, transform.position, transform.rotation) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);  
  
            // create code here that animates the newProjectile  
  
            nextFire = nextFire - myTime;
            myTime = 0.0F;
        }
    }
}

```

* * *
