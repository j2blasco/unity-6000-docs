* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).name
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
name; 
### Description
The name of the object.
Components share the same name with the game object and all attached components. If a class derives from MonoBehaviour it inherits the "name" field from [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html). If this class is also attached to GameObject, then "name" field is set to the name of that GameObject.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleOne;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleTwo;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleThree;  
  
    void Start()
    {
        //Sets the name of GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) One.
        exampleOne.name = "Ben";
        //Sets the name of GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Two.
        exampleTwo.name = "Ryan";
        //Sets the name of GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Three.
        exampleThree.name = "Oscar";  
  
        //Displays their names in the console.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The names of these three objects are " + exampleOne.name + exampleTwo.name + exampleThree.name);
    }
}

```

* * *
