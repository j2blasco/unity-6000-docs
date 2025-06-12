* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-ctor.html

# Color Constructor
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
public Color(float r, float g, float b, float a); 
### Parameters
Parameter | Description  
---|---  
r | Red component.  
g | Green component.  
b | Blue component.  
a | Alpha component.  
### Description
Constructs a new Color with given r,g,b,a components.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) newColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.3f, 0.4f, 0.6f, 0.3f);
    }
}

```

* * *
## Declaration
public Color(float r, float g, float b); 
### Parameters
Parameter | Description  
---|---  
r | Red component.  
g | Green component.  
b | Blue component.  
### Description
Constructs a new Color with given r,g,b components and sets `a` to 1.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) newColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.3f, 0.4f, 0.6f);
    }
}

```

Note: If the Color Constructor is called and no r,g,b,a components are given, all r,g,b,a components default to a value of 0.
* * *
