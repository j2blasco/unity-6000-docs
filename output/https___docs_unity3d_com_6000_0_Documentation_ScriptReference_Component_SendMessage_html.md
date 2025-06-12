* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).SendMessage
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
public void SendMessage(string methodName); 
## Declaration
public void SendMessage(string methodName, object value); 
## Declaration
public void SendMessage(string methodName, object value, [SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) options); 
## Declaration
public void SendMessage(string methodName, [SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
methodName | Name of the method to call.  
value | Optional parameter for the method.  
options | Should an error be raised if the target object doesn't implement the method for the message?  
### Description
Calls the method named `methodName` on every [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) in this game object.
The receiving method can choose to ignore the argument by having zero arguments. If options is set to [SendMessageOptions.RequireReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.RequireReceiver.html) an error is printed when the message is not picked up by any component.  
  
Note that messages will not be sent to inactive objects (ie, those that have been deactivated in the editor or with the [GameObject.SetActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetActive.html) function).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        /// Calls the function ApplyDamage with a value of 5
        SendMessage("ApplyDamage", 5.0);
    }  
  
    // Every script attached to the game object
    // that has a ApplyDamage function will be called.
    void ApplyDamage(float damage)
    {
        print(damage);
    }
}

```

* * *
