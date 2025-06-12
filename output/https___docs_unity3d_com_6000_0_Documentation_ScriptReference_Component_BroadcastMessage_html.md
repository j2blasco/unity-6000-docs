* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).BroadcastMessage
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
public void BroadcastMessage(string methodName, object parameter = null, [SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) options = SendMessageOptions.RequireReceiver); 
## Declaration
public void BroadcastMessage(string methodName, [SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
methodName | Name of the method to call.  
parameter | Optional parameter to pass to the method (can be any value).  
options | Should an error be raised if the method does not exist for a given target object?  
### Description
Calls the method named `methodName` on every [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) in this game object or any of its children.
The receiving method can choose to ignore `parameter` by having zero arguments. if options is set to [SendMessageOptions.RequireReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.RequireReceiver.html) an error is printed when the message is not picked up by any component.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        /// Calls the function ApplyDamage with a value of 5
        BroadcastMessage("ApplyDamage", 5.0);
    }  
  
    // Every script attached to the game object and all its children
    // that has a ApplyDamage function will be called.
    void ApplyDamage(float damage)
    {
        print(damage);
    }
}

```

* * *
