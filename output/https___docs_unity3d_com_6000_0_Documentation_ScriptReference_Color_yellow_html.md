* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).yellow
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) yellow; 
### Description
Yellow. RGBA is (1, 0.92, 0.016, 1), but the color is nice to look at!
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) (go to **Create**>**3D Object** and select one of the first 6 options to create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) automatically attached).
//This script changes the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) when your mouse hovers over it in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html).  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) m_Renderer;  
  
    void Start()
    {
        //Fetch the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    //Run your mouse over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to change the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)'s material color to yellow
    void OnMouseOver()
    {
        m_Renderer.material.color = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
    }  
  
    //Change the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)'s Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) back to white when the mouse exits the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    void OnMouseExit()
    {
        m_Renderer.material.color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    }
}

```

* * *
