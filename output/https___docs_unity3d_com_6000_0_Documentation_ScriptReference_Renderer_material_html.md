* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).material
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
[Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material; 
### Description
Returns the first instantiated [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) assigned to the renderer.
Modifying `material` will change the material for this object only.  
  
If the material is used by any other renderers, this will clone the shared material and start using it from now on.  
  
**Note:**  
This function automatically instantiates the materials and makes them unique to this renderer. It is your responsibility to destroy the materials when the game object is being destroyed. [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) also destroys the materials but it is usually only called when loading a new level.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) m_Material;  
  
    void Start()
    {
        //Fetch the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) from the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Material = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material;
        print("Materials " + Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html))).Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.A[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.A.html)))
        {
            //Output the amount of materials before GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is destroyed
            print("Materials " + Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html))).Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html));
            //Destroy GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
            Destroy(gameObject);
        }
    }  
  
    void OnMouseOver()
    {
        // Change the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) when the mouse hovers over it
        m_Material.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    }  
  
    void OnMouseExit()
    {
        //Change the Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) back to white when the mouse exits the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Material.color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    }  
  
    void OnDestroy()
    {
        //Destroy the instance
        Destroy(m_Material);
        //Output the amount of materials to show if the instance was deleted
        print("Materials " + Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html))).Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html));
    }
}

```

* * *
