* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StopAllCoroutines.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).StopAllCoroutines
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
## Declaration
public void StopAllCoroutines(); 
### Description
Stops all coroutines running on this behaviour.
A MonoBehaviour can execute zero or more coroutines. Created coroutines can execute for a range of times. In the script example below two coroutines are created and run without stopping. However, [StopAllCoroutines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StopAllCoroutines.html) is used to stop both of them. This action can be made to happen on a script that runs multiple coroutines. No arguments are needed because all coroutines on a script are stopped.  
**Note:** [StopAllCoroutines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.StopAllCoroutines.html) operates only on the one script it is attached to. 
```
using UnityEngine;
using System.Collections;  
  
// Create two coroutines that run at different speeds.
// When the space key is pressed stop both of them.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //coroutine 1
    IEnumerator DoSomething1()
    {
        while (true)
        {
            print("DoSomething1");
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.0f);
        }
    }  
  
    //coroutine 2
    IEnumerator DoSomething2()
    {
        while (true)
        {
            print("DoSomething2");
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.5f);
        }
    }  
  
    void Start()
    {
        StartCoroutine("DoSomething1");
        StartCoroutine("DoSomething2");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
        {
            StopAllCoroutines();
            print("Stopped all Coroutines: " + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        }
    }
}

```

* * *
