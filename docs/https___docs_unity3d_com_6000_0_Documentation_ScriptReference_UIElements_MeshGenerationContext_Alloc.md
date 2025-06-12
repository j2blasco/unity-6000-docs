* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.Allocate.html

#  [MeshGenerationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html).Allocate
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
public [UIElements.MeshWriteData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshWriteData.html) Allocate(int vertexCount, int indexCount, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
### Parameters
Parameter | Description  
---|---  
vertexCount | The number of vertices to allocate. The maximum is 65535 (or UInt16.MaxValue).  
indexCount | The number of triangle list indices to allocate. Each 3 indices represent one triangle, so this value should be multiples of 3.  
texture | An optional texture to be applied on the triangles allocated. Pass null to rely on vertex colors only.  
### Description
Allocates and draws the specified number of vertices and indices required to express geometry for drawing the content of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). 
See [Vertex.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-position.html) for details on geometry generation conventions. If a valid texture was passed, then the returned [MeshWriteData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshWriteData.html) will also describe a rectangle for the UVs to use to sample the passed texture. This is needed because textures passed to this API can be internally copied into a larger atlas.   
  
If a valid texture was passed, then the [Vertex.uv](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex-uv.html) values should be used to map the texture to the geometry.   
  
You can call `MeshGenerationContext.Allocate()` multiple times for the same element or context. To optimize performance, minimize the number of calls whenever possible.   
  
Additional resources: [MeshWriteData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshWriteData.html)   
  

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
