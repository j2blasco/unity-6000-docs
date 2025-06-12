* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SendMessageUpwards.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).SendMessageUpwards
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
## Declaration
public void SendMessageUpwards(string methodName, object value = null, [SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) options = SendMessageOptions.RequireReceiver); 
### Parameters
Parameter | Description  
---|---  
methodName | The name of the MonoBehaviour method to call.  
value | An optional parameter value to pass to the called method.  
options | Whether an error should be raised if the method doesn't exist on the target object.  
### Description
Calls the specified method on every MonoBehaviour attached to the GameObject and on every ancestor of the behaviour.
A `value` parameter specified for a method that doesn't accept parameters is ignored. If `options` is set to [SendMessageOptions.RequireReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.RequireReceiver.html) an error is printed when the message is not picked up by any component.  
  
**Note** : Messages are not sent to MonoBehaviours attached to objects for which [GameObject.activeSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeSelf.html) or [GameObject.activeInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-activeInHierarchy.html) are `false`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Calls the function ApplyDamage with a value of 5
        gameObject.SendMessageUpwards("ApplyDamage", 5.0);
    }
}  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void ApplyDamage(float damage)
    {
        print(damage);
    }
}

```

Additional resources: [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), [GameObject.SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SendMessage.html)
* * *
