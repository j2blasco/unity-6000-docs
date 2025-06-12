* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).Awake()
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
### Description
Unity calls `Awake` when an enabled script instance is being loaded.
Unity calls `Awake` on scripts derived from `MonoBehaviour` in the following scenarios: 
  * The parent GameObject is active and initializes on Scene load
  * The parent GameObject goes from inactive to active
  * After initialization of a parent GameObject created with [Object.Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html)


Use `Awake` to initialize variables or states before the application starts.  
  
Unity calls `Awake` only once during the lifetime of the script instance. A script's lifetime lasts until the Scene that contains it is unloaded. If the Scene is loaded again, Unity loads the script instance again and calls `Awake` again. If the Scene is loaded multiple times additively, Unity loads several script instances, and `Awake` is called once for each instance.  
  
For active GameObjects placed in a Scene, Unity calls `Awake` after all active GameObjects in the Scene are initialized, so you can safely use methods such as [GameObject.FindWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html) to query other GameObjects.  
  
The order in which Unity calls each GameObject's `Awake` is not deterministic. Because of this, you should not rely on `Awake` being called on one GameObject before or after another. For example, you should not assume that a reference set up by one GameObject's `Awake` will be usable in another GameObject's `Awake`. Instead, you should use `Awake` to set up references between scripts, and use [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html), which is called after all `Awake` calls are finished, to pass any information back and forth.  
  
`Awake` is always called before any [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html) functions. This allows you to order initialization of scripts. `Awake` is called even if the script is a disabled component of an active GameObject. If a script component's `Awake` throws an exception, Unity disables the component. `Awake` cannot act as a coroutine.  
  
Use `Awake` instead of the constructor for initialization, as the serialized state of the component is undefined at construction time. `Awake` is called once, just like the constructor. 
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) target;  
  
    void Awake()
    {
        target = GameObject.FindWithTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html)("Player");
    }
}

```

An inactive [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can be activated when [GameObject.SetActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetActive.html) is called on it.  
  
  
The following two example scripts **Example1** and **Example2** work together, and illustrate two timings when Awake() is called.  
To reproduce the example, create a scene with two GameObjects Cube1 and Cube2. Assign Example1 as a script component to Cube1, and set Cube1 as inactive, by unchecking the Inspector top-left check box (Cube1 will become invisible). Assign Example2 as a script component to Cube2, and set Cube1 as its `GO` variable.  
Enter Play mode: pressing the space key will execute code in Example2.Update that activates Cube1, and causes Example1.Awake() to be called.
```
using UnityEngine;  
  
// Make sure that Cube1 is assigned this script and is inactive at the start of the game.  
  
public class Example1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        // Prints first
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Example1.Awake() was called");
    }  
  
    void Start()
    {
        // Prints second
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Example1.Start() was called");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("b"))
        {
            // Prints Last if "b" is pressed
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("b key was pressed");
        }
    }
}

```

Example2. This causes Example1.Awake() to be called. The Space key is used to perform this:
```
using UnityEngine;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Assign Cube1 to this variable GO before running the example
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) GO;  
  
    void Awake()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Example2.Awake() was called");
    }  
  
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Example2.Start() was called");
    }  
  
    // track if Cube1 was already activated
    private bool activateGO = true;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (activateGO == true)
        {
            if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("space key was pressed");
                GO.SetActive(true);
                activateGO = false;
            }
        }
    }
}

```

* * *
