* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.AddMeshGenerationJob.html

#  [MeshGenerationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html).AddMeshGenerationJob
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
public void AddMeshGenerationJob([Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) jobHandle); 
### Parameters
Parameter | Description  
---|---  
jobHandle | JobHandle to wait for.  
### Description
Instructs the renderer to wait for the completion of the provided JobHandle before beginning processing the meshes. 
The following code example shows how to use a job to generate a mesh: 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;
using UnityEngine.UIElements;  
  
class CheckerboardElement : VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
{
    struct CheckerboardJob : IJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
    {
        [WriteOnly] public NativeSlice<Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)> vertices;
        [WriteOnly] public NativeSlice<ushort> indices;  
  
        public int horizontalCount;
        public int verticalCount;
        public float divisions;
        public Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color1;
        public Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color2;  
  
        public void Execute()
        {
            Span<Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)> colors = stackalloc Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)[2];
            colors[0] = color1;
            colors[1] = color2;
            int colorIndex = 0;  
  
            int vCount = 0;
            int iCount = 0;  
  
            float left = 0;
            float right = divisions;
            for (int i = 0; i < horizontalCount; ++i)
            {
                float top = 0;
                float bottom = divisions;
                for (int j = 0; j < verticalCount; ++j)
                {
                    colorIndex = (i ^ j) & 1;  
  
                    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color = colors[colorIndex];  
  
                    vertices[vCount + 0] = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) { position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(left, bottom), tint = color };
                    vertices[vCount + 1] = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) { position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(left, top), tint = color };
                    vertices[vCount + 2] = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) { position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(right, top), tint = color };
                    vertices[vCount + 3] = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) { position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(right, bottom), tint = color };  
  
                    indices[iCount + 0] = (ushort)(vCount + 0);
                    indices[iCount + 1] = (ushort)(vCount + 1);
                    indices[iCount + 2] = (ushort)(vCount + 2);
                    indices[iCount + 3] = (ushort)(vCount + 2);
                    indices[iCount + 4] = (ushort)(vCount + 3);
                    indices[iCount + 5] = (ushort)(vCount + 0);  
  
                    vCount += 4;
                    iCount += 6;
                    top += divisions;
                    bottom += divisions;
                }  
  
                left += divisions;
                right += divisions;
            }
        }
    }  
  
    int m_Divisions;
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) m_Color1;
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) m_Color2;  
  
    public CheckerboardElement(int divisions, Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color1, Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color2)
    {
        generateVisualContent = OnGenerateVisualContent;
        m_Divisions = divisions;
        m_Color1 = color1;
        m_Color2 = color2;
    }  
  
    void OnGenerateVisualContent(MeshGenerationContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html) mgc)
    {
        int horizontalCount = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(layout.width / m_Divisions);
        int verticalCount = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(layout.height / m_Divisions);  
  
        if (horizontalCount == 0 || verticalCount == 0)
            return;  
  
        var job = new CheckerboardJob
        {
            horizontalCount = horizontalCount,
            verticalCount = verticalCount,
            divisions = m_Divisions,
            color1 = m_Color1,
            color2 = m_Color2
        };  
  
        int quads = horizontalCount * verticalCount;  
  
        mgc.AllocateTempMesh(quads * 4, quads * 6, out job.vertices, out job.indices);
        mgc.DrawMesh(job.vertices, job.indices);  
  
        JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) jobHandle = job.Schedule();
        mgc.AddMeshGenerationJob(jobHandle);
    }
}

```

* * *
