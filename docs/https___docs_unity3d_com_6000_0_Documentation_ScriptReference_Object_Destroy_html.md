* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).Destroy
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html "Go to Object Component in the Manual")
## Declaration
public static void Destroy([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, float t = 0.0F); 
### Parameters
Parameter | Description  
---|---  
obj | The object to destroy.  
t | The optional amount of time to delay before destroying the object.  
### Description
Removes a GameObject, component or asset.
The object `obj` is destroyed immediately after the current Update loop, or `t` seconds from now if a time is specified. If `obj` is a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), this method removes the component from the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and destroys it. If `obj` is a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), it destroys the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), all its components and all transform children of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Actual object destruction is always delayed until after the current Update loop, but is always done before rendering.  
  
Note: When destroying MonoBehaviour scripts, Unity calls OnDisable and OnDestroy before the script is removed.  
  
Additional resources: [Object.DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void DestroyGameObject()
    {
        Destroy(gameObject);
    }  
  
    void DestroyScriptInstance()
    {
        // Removes this script instance from the game object
        Destroy(this);
    }  
  
    void DestroyComponent()
    {
        // Removes the rigidbody from the game object
        Destroy(GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>());
    }  
  
    void DestroyObjectDelayed()
    {
        // Kills the game object in 5 seconds after loading the object
        Destroy(gameObject, 5);
    }  
  
    // When the user presses Ctrl, it will remove the
    // BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) component from the game object
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html)("Fire1") && GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>())
        {
            Destroy(GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>());
        }
    }
}

```

Destroy is inherited from the UnityEngine.Object base class.
* * *
