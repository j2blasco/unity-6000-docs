* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/null-reference-exception.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Null references


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html)
Using randomness
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-attributes.html)
Unity attributes
# Null references
A `NullReferenceException` in C# happens when you try to access a member on a type whose value is `null`. A `NullReferenceException` at runtime often means you’ve forgotten to initialize an object reference variable before using it. For a complete explanation of common coding errors that produce null references, refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/api/system.nullreferenceexception?view=net-8.0).
The null reference error message looks something like:
```
NullReferenceException: Object reference not set to an instance of an object
    at Example.Start () [0x0000b] in /Unity/projects/nre/Assets/Example.cs:10 

```

This error message says that a `NullReferenceException` happened on line 10 of the script file `Example.cs`, and that the exception happened inside the `Start()` function. This makes the Null Reference Exception easy to find and fix. In this example, the code is:
```
using UnityEngine;
using System.Collections;

public class Example : MonoBehaviour {

    // Use this for initialization
    void Start () {
        GameObject myGameObject = GameObject.Find("exampleGameObject");
        Debug.Log(myGameObject.name);
    }
    
}

```

The code looks for a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) called “exampleGameObject”. In this example there is no GameObject with that name, so the `Find()` function returns `null`. On the next line (line 9) the script uses the `myGameObject` variable to print out the name of the GameObject it references. Because it is trying to access a GameObject that doesn’t exist, Unity returns a `NullReferenceException`
## Null checks
The solution in this example is to include an outcome for situations where the GameObject with the given name does not exist. The following script checks whether the `go` variable returns `null`, and displays a message if so:
```
using UnityEngine;
using System.Collections;

public class Example : MonoBehaviour {

    void Start () {
        GameObject myGameObject = GameObject.Find("exampleGameObject");
        if (myGameObject == null) {
            Debug.Log("No GameObject called exampleGameObject found");
        } else {
            Debug.Log(myGameObject.name);
        }
    }
        
}

```

### Custom == operator
For types that inherit from [UnityEngine.Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html), Unity uses a custom version of the C# [equality and inequality operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators). This means the null check in the previous example (`myGameObject == null`) can evaluate `true` (and conversely `myGameObject != null` can evaluate `false`) even if `myGameObject` technically holds a valid C# object reference. This happens in two cases:
  1. The object can be a so-called “fake null” or placeholder object which Unity uses in the Editor only to populate uninitialized MonoBehaviour fields. These objects store useful debugging information to help you locate the source of these fields if you try to reference them.
  2. The object can be a managed (C#) object which has not yet been garbage collected but which should be considered null because the unmanaged (C++) counterpart object has been destroyed.


## Try/Catch blocks
Unity also calls `NullReferenceException` if you use a variable that needs to be initialized in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window. If you forget to do this, then the variable is `null`. A different way to deal with `NullReferenceException` is to use `try`/`catch` blocks. For example:
```
using UnityEngine;
using System;
using System.Collections;

public class Example2 : MonoBehaviour {

    public Light myLight; // set in the inspector
    
    void Start () {
        try {
            myLight.color = Color.yellow;
        }       
        catch (NullReferenceException ex) {
            Debug.Log("myLight was not set in the inspector");
        }
    }
    
}

```

In this code example, the variable called `myLight` is a `Light` which you need to set in the Inspector window. If this variable is not set, then it defaults to `null`. 
Attempting to change the color of the light in the `try` block causes a `NullReferenceException`. If this happens, the `catch` block code displays a message reminding you to set the Light in the inspector.
## Additional resources
  * [UnityEngine.Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html)
Using randomness
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-attributes.html)
Unity attributes
