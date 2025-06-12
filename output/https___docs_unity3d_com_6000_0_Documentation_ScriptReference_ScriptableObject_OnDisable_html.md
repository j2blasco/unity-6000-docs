* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html

#  [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html).OnDisable()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html "Go to ScriptableObject Component in the Manual")
### Description
This function is called when the scriptable object goes out of scope.
This is also called when the object is destroyed and can be used for any cleanup code. When scripts are reloaded after compilation has finished, OnDisable will be called, followed by an OnEnable after the script has been loaded.
```
// A ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) example script.
// The A and B members implement features which
// are unrelated to MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).  
  
using UnityEngine;  
  
public class ScriptObj : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    int a = 10;
    int[] b = new int[5] {0, 17, 34, 42, 67};  
  
    public int A
    {
        get {return a; }
    }  
  
    // return value in b array, or -1 if x is out-of-range
    public int B(int x)
    {
        if (x >= 0 && x < 5)
            return b[x];
        else
            return -1;
    }  
  
    public void Awake()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Awake");
    }  
  
    public void OnEnable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnEnable");
    }  
  
    public void OnDisable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDisable");
    }  
  
    public void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDestroy");
    }
}

```

The following script makes use of the above ScriptableObject script. 
```
// create and access the ScriptObj  
  
using UnityEngine;  
  
public class ScriptObjExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ScriptObj test;  
  
    void Start()
    {
        test = (ScriptObj)ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)(typeof(ScriptObj));  
  
        print(test.A);
        print(test.B(3));
        print(test.B(-3));
    }
}

```

OnDisable cannot be a co-routine.
* * *
