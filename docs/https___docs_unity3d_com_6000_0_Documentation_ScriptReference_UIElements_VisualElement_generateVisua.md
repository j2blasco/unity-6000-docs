* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-generateVisualContent.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).generateVisualContent
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
generateVisualContent; 
### Description
Delegate function to generate the visual content of a visual element. 
Use this delegate to generate custom geometry in the content region of the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).   
  
This delegate is called during the initial creation of the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) and whenever a repaint is needed. This delegate isn't called on every frame refresh. To force a repaint, call [VisualElement.MarkDirtyRepaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.MarkDirtyRepaint.html).   
  
**Note** : When you execute code in a handler to this delegate, don't update any property of the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html), as this can alter the generated content and cause unwanted side effects, such as lagging or missed updates. To avoid this, treat the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) as read-only within the delegate.   
  
Additional resources: [MeshGenerationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html)   
  

```
//This example creates a custom element that dynamically renders a textured rectangle 
//based on the element’s size.   
  
using UnityEngine;
using UnityEngine.UIElements;  
  
public class TexturedElement : VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
{
    static readonly Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)[] k_Vertices = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)[4];
    static readonly ushort[] k_Indices = { 0, 1, 2, 2, 3, 0 };  
  
    static TexturedElement()
    {
        k_Vertices[0].tint = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        k_Vertices[1].tint = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        k_Vertices[2].tint = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        k_Vertices[3].tint = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
        k_Vertices[0].uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0);
        k_Vertices[1].uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1);
        k_Vertices[2].uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1);
        k_Vertices[3].uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0);
    }  
  
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) m_Texture;  
  
    public TexturedElement()
    {
        //This element grows to fill the available space.
        style.flexGrow = 1.0f;
        
        //Subscribes the OnGenerateVisualContent method to the generateVisualContent delegate.
        generateVisualContent += OnGenerateVisualContent;  
  
        //Create a simple 2x2 checkerboard texture.
        m_Texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(2, 2);
        m_Texture.SetPixels(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] {
            Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html), Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html),
            Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html), Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html)
        });
        m_Texture.Apply();  
  
        //You can also load a texture from a file.
        //m_Texture = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/tex.png");
    }  
  
    //This method is called when the element needs to render its content.
    void OnGenerateVisualContent(MeshGenerationContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html) mgc)
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r = contentRect;
        if (r.width < 0.01f || r.height < 0.01f)
            return; // Skip rendering when too small.  
  
        float left = 0;
        float right = r.width;
        float top = 0;
        float bottom = r.height;  
  
        k_Vertices[0].position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(left, bottom, Vertex.nearZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-nearZ.html));
        k_Vertices[1].position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(left, top, Vertex.nearZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-nearZ.html));
        k_Vertices[2].position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(right, top, Vertex.nearZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-nearZ.html));
        k_Vertices[3].position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(right, bottom, Vertex.nearZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-nearZ.html));  
  
        MeshWriteData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshWriteData.html) mwd = mgc.Allocate(k_Vertices.Length, k_Indices.Length, m_Texture);  
  
        mwd.SetAllVertices(k_Vertices);
        mwd.SetAllIndices(k_Indices);
    }
}

```

* * *
