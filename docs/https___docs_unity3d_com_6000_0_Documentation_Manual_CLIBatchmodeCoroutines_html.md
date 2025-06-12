* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CLIBatchmodeCoroutines.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Command-line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html)
  * Batch mode and built-in coroutine compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html)
Unity Standalone Player command line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextSceneFormat.html)
Text-Based Scene Files
# Batch mode and built-in coroutine compatibility
This page describes the supported features when running the Unity Editor and Standalone Player in batch mode. 
When running Unity, the following built-in [coroutine](https://docs.unity3d.com/6000.0/Documentation/Manual/Coroutines.html) operators add functionality:
  * [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html)
  * [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)
  * [WaitForFixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForFixedUpdate.html)
  * [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)
  * [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html)
  * [WaitUntil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html)
  * [WaitWhile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html)


The following table shows which of these operators Unity supports inside the Editor and Standalone Player, and when running each of them in batch mode using the [-batchmode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#batchmode) command line argument:
| Editor | Editor -batchmode | Unity Standalone Player | Unity Standalone Player -batchmode  
---|---|---|---|---  
`AsyncOperation` | Yes | Yes | Yes | Yes  
`WaitForEndOfFrame` | Yes | No* | Yes | Yes  
`WaitForFixedUpdate` | Yes | Yes | Yes | Yes  
`WaitForSeconds` | Yes | Yes | Yes | Yes  
`WaitForSecondsRealtime` | Yes | Yes | Yes | Yes  
`WaitUntil` | Yes | Yes | Yes | Yes  
`WaitWhile` | Yes | Yes | Yes | Yes  
* You cannot use `WaitForEndOfFrame` when running the Editor with `-batchmode`, because systems like animation, physics and timeline might not work correctly in the Editor. This is because Unity does not currently update these systems when using `WaitForEndOfFrame`. 
## Running coroutines
### Inside the Editor
In the Editor, press the “Play” button to run your code with coroutines.
### Editor in batch mode
To run coroutines when launching the Editor in batch mode from the command line, enter:
C:\Program Files\Unity\Editor\Unity.exe **-projectPath** PROJECT_PATH **-batchMode**
### Inside the Standalone Player
Launch your Standalone Player to run your code. The Player loads and then waits for your coroutines to complete.
### Standalone Player in batch mode
To run coroutines when launching the Player in batch mode from the command line, enter:
PATH_TO_STANDALONE_BUILD **-projectPath** PROJECT_PATH **-batchMode**
For example, on Windows:
C:\projects\myproject\builds\myproject.exe **-batchMode**
On Mac:
~/UnityProjects/myproject/builds/myproject **-batchMode**
## Example coroutine scripts
### AsyncOperation
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_AsyncTests());
    }

    public IEnumerator Example_AsyncTests()
    {
        Debug.Log("Start of AsyncLoad Example");
        
        var load = UnityEngine.Resources.LoadAsync("");
        yield return load;
        yield return null;
        
        Debug.Log("End of AsyncLoad Example");
    }
}

```

### WaitForEndOfFrame
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitForEndOfFrame_Coroutine());
    }

    public IEnumerator Example_WaitForEndOfFrame_Coroutine()
    {
        Debug.Log("Start of WaitForEndOfFrame Example");
        
        yield return new WaitForEndOfFrame();
        
        Debug.Log("End of WaitForEndOfFrame Example");
    }
}

```

### WaitForFixedUpdate
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitForFixedUpdate_Coroutine());
    }

    public IEnumerator Example_WaitForFixedUpdate_Coroutine()
    {
        Debug.Log("Start of WaitForFixedUpdate Example");
        
        yield return new WaitForFixedUpdate();
        
        Debug.Log("End of WaitForFixedUpdate Example");
    }
}

```

### WaitForSeconds
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitForSeconds_Coroutine());
    }

    public IEnumerator Example_WaitForSeconds_Coroutine()
    {
        Debug.Log("Start of WaitForSeconds Example");
        
        yield return new WaitForSeconds(1.5f);
        
        Debug.Log("End of WaitForSeconds Example");
    }
}

```

### WaitForSecondsRealtime
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitForSecondsRealtime_Coroutine());
    }

    public IEnumerator Example_WaitForSecondsRealtime_Coroutine()
    {
        Debug.Log("Start of WaitForSecondsRealtime Example");
        
        yield return new WaitForSecondsRealtime(1.5f);
        
        Debug.Log("End of WaitForSecondsRealtime Example");
    }
}

```

### WaitUntil
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitUntil_Coroutine());
    }

    public IEnumerator Example_WaitUntil_Coroutine()
    {
        Debug.Log("Start of WaitUntil Example");
        
        yield return new WaitUntil(() => Time.time > 5.0f);
        
        Debug.Log("End of WaitUntil Example");
    }
}

```

### WaitWhile
```
using System.Collections;
using UnityEngine;

[ExecuteInEditMode]
public class ExampleClass : MonoBehaviour
{
    public void Start()
    {
        StartCoroutine(Example_WaitWhile_Coroutine());
    }

    public IEnumerator Example_WaitWhile_Coroutine()
    {
        Debug.Log("Start of WaitWhile Example");
        
        yield return new WaitWhile(() => Time.time < 5.0f);
        
        Debug.Log("End of WaitWhile Example");
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html)
Unity Standalone Player command line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextSceneFormat.html)
Text-Based Scene Files
