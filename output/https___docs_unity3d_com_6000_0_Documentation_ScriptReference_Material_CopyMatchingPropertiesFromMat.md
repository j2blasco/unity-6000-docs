* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.CopyMatchingPropertiesFromMaterial.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).CopyMatchingPropertiesFromMaterial
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public void CopyMatchingPropertiesFromMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat); 
### Parameters
Parameter | Description  
---|---  
mat | The [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to copy from.  
### Description
Copies properties, keyword states and settings from `mat` to this material, but only if they exist in both materials.
This method copies the following properties if they exist in both materials: 
  * Serialized material properties.
  * Keyword states, if the keywords exist in both shaders.
  * Material settings: [Material.doubleSidedGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-doubleSidedGI.html), [Material.enableInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enableInstancing.html), [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html) and [Material.globalIlluminationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-globalIlluminationFlags.html).


```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has a renderer.
    // Copies any property from mat and assigns it to this transform's material, if the property exists in both materials.  
  
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;  
  
    void Start()
    {
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.CopyMatchingPropertiesFromMaterial(mat);
    }
}
```

* * *
