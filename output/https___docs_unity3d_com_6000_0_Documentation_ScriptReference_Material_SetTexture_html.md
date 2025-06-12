* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetTexture
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
public void SetTexture(string name, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) value); 
## Declaration
public void SetTexture(int nameID, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) value); 
## Declaration
public void SetTexture(string name, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) value, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
## Declaration
public void SetTexture(int nameID, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) value, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_MainTex".  
value | Texture to set.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
### Description
Sets a named texture.
Many shaders use more than one texture. Use SetTexture to change the texture (identified by shader property name, or unique property name ID).  
  
When setting textures on materials using the Standard Shader, you should be aware that you may need to use [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html) to enable features of the shader that were not previously in use. For more detail, read [Accessing Materials via Script](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialsAccessingViaScript.html).  
  
Common texture names used by Unity's builtin shaders:   
`"_MainTex"` is the main diffuse texture. This can also be accessed via [mainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html) property.   
`"_BumpMap"` is the normal map.  
  
The shader properties also show some of the keywords needed to set the Texture of a Material. To see this, go to your Material and right click on the **Shader** dropdown at the top. Next, pick **Select Shader**.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data to set from the RenderTexture. The possible options are: [RenderTextureSubElement.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Color.html), [RenderTextureSubElement.Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Depth.html), and [RenderTextureSubElement.Stencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [mainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html) property, [GetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTexture.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html), [Properties in Shader Programs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html), [RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html).
```
//Attach this script to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (make sure it has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component)
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Attach your own Textures in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Inspector.  
  
//This script takes your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s material and changes its Normal Map, Albedo, and Metallic properties to the Textures you attach in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Inspector. This happens when you enter Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    //Set these Textures in the Inspector
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) m_MainTexture, m_Normal, m_Metal;
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) m_Renderer;  
  
    // Use this for initialization
    void Start () {
        //Fetch the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();  
  
        //Make sure to enable the Keywords
        m_Renderer.material.EnableKeyword ("_NORMALMAP");
        m_Renderer.material.EnableKeyword ("_METALLICGLOSSMAP");  
  
        //Set the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) you assign in the Inspector as the main texture (Or Albedo)
        m_Renderer.material.SetTexture("_MainTex", m_MainTexture);
        //Set the Normal map using the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) you assign in the Inspector
        m_Renderer.material.SetTexture("_BumpMap", m_Normal);
        //Set the Metallic Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) as a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) you assign in the Inspector
        m_Renderer.material.SetTexture ("_MetallicGlossMap", m_Metal);
    }
}

```

* * *
